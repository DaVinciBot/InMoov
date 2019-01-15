#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask,jsonify,render_template,redirect,session,url_for,request
from flask_socketio import SocketIO,emit,disconnect
import hashlib, rospy, logging, sys, os, eventlet
from std_msgs.msg import String

eventlet.monkey_patch()

""" 
Here is all the ROS related stuff
"""
#Publishers/Services
pub = rospy.Publisher('master_topic',String,queue_size=10)

#Callback function
def multimessage_callback(msg, topic_name):
	print("Got something on topic <%s> : %s" % (topic_name, str(msg.data)))
	socketio.emit('updatetp', msg.data, namespace='/websocket')

#Subscribers
rospy.Subscriber('master_topic', String, multimessage_callback, callback_args="master_topic")

#Node initialisation
rospy.init_node('web_node', anonymous = True, log_level = rospy.INFO, disable_signals = True)

""" 
Here is all the WebServer related stuff
"""
#App Initialisation
app = Flask(__name__)
socketio = SocketIO(app)

#A deplacer dans un fichier de config
action_list = {'left_hand':['open','close'],'right_hand':['open','close'],'left_arm':['raise','lower'],'right_arm':['raise','lower'],'head':['turn_left','turn_right']}

FLASK_ENV = -1

if os.getenv("FLASK_ENV") == "development":
	FLASK_ENV = 0
	app.config.update(
	SECRET_KEY = 'I@SO#cT)K%b"A,N_a/T|9g"ClG§ejN',
	USERNAME = 'inmoov_admin',
	PASSWORD = 'e03df9d3b276ee84e3ec4d8a6adc2f9e050bcaad749465577bf8162df9faceec', #inmoov_admin
	API_TOKEN = 'thisisapikey',
	)
elif os.getenv("FLASK_ENV") == "production":
	FLASK_ENV = 1
	app.config.from_pyfile('./config/App.cfg', silent=True)
else:
	print("Error : You must set FLASK_ENV variable to 'production' or 'development'")
	exit(0)

#Voir si on peut enlever ca d'ici et juste le mettre dans le code normal...
#@app.before_first_request
#def setup_multi_logging():
#	log = logging.getLogger('werkzeug')
#	log.setLevel(logging.INFO)
#	log.addHandler(logging.StreamHandler(stream=sys.stdout))
 #       app.logger.addHandler(logging.StreamHandler(stream=sys.stdout))
  #      app.logger.setLevel(logging.INFO)

#Redirection a utiliser une fois que l'on est sur
#@app.before_request
#def before_request():
#    if request.url.startswith('http://'):
#        url = request.url.replace('https://', 'https://', 1)
#        return redirect(url, code=301)

#Retirer tous les prints quand ca fonctionnera 100%

@app.errorhandler(Exception)
def handle_error(e):
	print("Error !", e)
	return (render_template('error.html'), 404)

@app.route('/', methods=['GET'])
def home():
	return (render_template('home.html'),200)

@app.route('/admin', methods=['GET'], strict_slashes=False)
def admin():
	if session and session['logged_in'] and session['logged_in'] is True:
		return (render_template('admin.html'),200)
	else:
		return (redirect(url_for('login')),302)

@socketio.on('pingws', namespace='/websocket')
def websocket_pingws(message):
	if session and session['logged_in'] and session['logged_in'] is True:
		print('Ping received : ' + message)
		emit('pongws', 'pong', namespace='/websocket')
	else:
		print('Ping received but not logged in')
		disconnect()
		return

@socketio.on('connect', namespace='/websocket')
def websocket_connect():
	if session and session['logged_in'] and session['logged_in'] is True:
		print('[WEBSOCKET] User connected !')
		session['websocket_connected'] = True
	else:
		print('[WEBSOCKET] User failed to connect !')
		disconnect()
		return

@socketio.on('disconnect', namespace='/websocket')
def websocket_disconnect():
	if session and session['websocket_connected']:
		session['websocket_connected'] = False
    	print('User disconnected from websocket !')

@app.route('/api', methods=['POST', 'GET'],  strict_slashes=False)
def api():
	if request.method == 'POST':
		try:
			data = request.get_json(force=True)
		except:
			return (jsonify(msg="Malformed request"),400)
		if 'part' in data and 'move' in data and 'api_token' in data:
			if data['api_token'] == app.config['API_TOKEN']:
				if data['part'] in action_list and data['move'] in action_list[data['part']]:
					pub.publish("{'move' : '" + data['move'] + "', 'part' : '" + data['part'] + "'}")
					#En vrai, on utilisera des services et pas des publisher pour l'API
					return (jsonify(msg="Done"),200)
				else:
					return (jsonify(msg="Invalid request"),400)
			else:
				return (jsonify(msg="Invalid API token"),400)
		else:
			return (jsonify(msg="Malformed request"),400)
	else:
		return (render_template('api_doc.html'),200)

@app.route('/admin/login', methods=['POST','GET'], strict_slashes=False)
def login():
	if request.method == 'GET':
		if session and session['logged_in'] and session['logged_in'] is True:
			return (redirect(url_for('admin')),302)
		else:
			return (render_template('login.html', msg=""),200)
	else:
		if request.form["username"] == app.config['USERNAME'] and hashlib.sha256(request.form['password']).hexdigest() == app.config['PASSWORD']:
			session['logged_in'] = True
			return (redirect(url_for('admin')),302)
		else:
			return(render_template('login.html', msg='Invalid username/password'),200)

@app.route('/admin/logout', methods=['GET'], strict_slashes=False)
def logout():
	session.pop('logged_in', None)
	return (render_template('logout.html'),200)

##Si on lance direct le programme via python
if __name__ == '__main__':
	#socketio.run(app, host = "0.0.0.0", port = 5000)
	eventlet.wsgi.server(eventlet.wrap_ssl(eventlet.listen(('0.0.0.0',5000)),certfile='./config/ssl_cert.pem',keyfile='./config/ssl_key.pem',server_side=True),app)
