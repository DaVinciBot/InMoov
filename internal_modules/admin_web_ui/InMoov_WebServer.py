#!/usr/bin/env python
#-*- coding: utf-8 -*-

from flask import Flask,jsonify,render_template,redirect,session,url_for,request, make_response
from flask_socketio import SocketIO,emit,disconnect
import hashlib, rospy, logging, sys, os, eventlet, random, string, json
from std_msgs.msg import String
from pymongo import MongoClient
from roslib import message as roslib_message
from bson.json_util import dumps

sys.path.append('/inmoov/catkin_ws/src/inmoov/scripts')
from inmoov_db.inmoov_db import InMoov_DB

eventlet.monkey_patch()

""" 
Here is all the ROS related stuff
"""

#Callback function
def emit_topicupdate(msg, topic_name):
	print("Got something on topic <%s> : %s" % (topic_name, str(msg.data)))
	socketio.emit('update_tp', json.dumps({'topic_name':topic_name, 'msg':str(msg.data)}), namespace='/websocket')

def emit_topiclist(SUBSCRIBERS_LIST):
	print("New topic list : ", SUBSCRIBERS_LIST)
	emit('get_tplist', json.dumps(SUBSCRIBERS_LIST) ,namespace='/websocket')

#rospy.Subscriber("/test", String, emit_topicupdate, callback_args='yolo')

def update_subscribers(SUBSCRIBERS_LIST):
	for topic in rospy.get_published_topics():
	        topic_name = topic[0]
        	if topic_name in SUBSCRIBERS_LIST or 'robot' not in topic_name:
                	continue
        	msg_type = roslib_message.get_message_class(topic[1])
        	rospy.Subscriber(topic_name, msg_type, emit_topicupdate, callback_args=topic_name)
        	print "Sub to %s" % topic_name
		SUBSCRIBERS_LIST.append(topic_name)

#Node initialisation INUTILE !!
rospy.init_node('web_node', anonymous = True, log_level = rospy.INFO, disable_signals = True)

""" 
Here is all the WebServer related stuff
"""
#App Initialisation
app = Flask(__name__)
socketio = SocketIO(app)

app.config.from_pyfile('./config/App.cfg', silent=True)

inmoovdb = InMoov_DB()

db = MongoClient(app.config['DB_ADDRESS'], port=app.config['DB_PORT'])[app.config['DB_NAME']]

db.sessions.delete_many({})

SUBSCRIBERS_LIST = []

@app.before_first_request
def before_first_request():
	update_subscribers(SUBSCRIBERS_LIST)

@app.errorhandler(Exception)
def handle_error(e):
	print("Error !", e)
	return (render_template('error.html'), 404)

@app.route('/', methods=['GET'])
def home():
	return (render_template('home.html'),200)

@app.route('/admin', methods=['GET'], strict_slashes=False)
def admin():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		return (render_template('admin.html'),200)
	else:
		resp = make_response(redirect(url_for('login')))
		resp.set_cookie('inmoov_session', '', expires=0)
		return (resp,302)

@app.route('/admin/addons', methods=['GET'], strict_slashes=False)
def manage_addons():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		return (render_template('addons.html'), 200)
	else:
		resp = make_response(redirect(url_for('login')))
		resp.set_cookie('inmoov_session', '', expires=0)
		return (resp,302)

@app.route('/admin/addons/manage', methods=['GET','POST', 'DELETE'], strict_slashes=False)
def addon_edit():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		if request.method == 'GET':
			return dumps({'msg':list(inmoovdb.get_all_addons()), 'code':'success'})
		elif request.method == 'POST':
			if request.form["name"] != "" and request.form['email'] != "" and inmoovdb.create_addon(request.form['name'], request.form['email']):
				return jsonify({'msg':'Successfully created !', 'code':'success'})
			else:
				return jsonify({'msg':'Addon failed to create : maybe this name already exists', 'code':'error'})
		else:
			if request.args['token'] != "" and inmoovdb.delete_addon(request.args['token']):
				return jsonify({'msg':'Successfully deleted !', 'code':'success'})
			else:
				return jsonify({'msg':"We can't delete this addon", 'code':'error'})
	else:
		resp = make_response(redirect(url_for('login')))
		resp.set_cookie('inmoov_session', '', expires=0)
		return (resp,302)

@app.route('/admin/power', methods=['GET'], strict_slashes=False)
def manage_power():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		if request.args.get('control') == "shutdown":
			os.system('sudo shutdown -h')
			return jsonify({'msg':'Shuting down in 60 seconds', 'code':'success'})
		elif request.args.get('control') == "reboot":
			os.system('sudo shutdown -r')
			return jsonify({'msg':'Rebooting in 60 seconds', 'code':'success'})
		else:
			return jsonify({'msg':'You must specify the "control" parameter', 'code':'error'})
	else:
		resp.set_cookie('inmoov_session', '', expires=0)
		return jsonify({'msg':'You must authenticate first','code':'error'})

@app.route('/admin/ssh', methods=['GET'], strict_slashes=False)
def manage_ssh():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		if request.args.get('state') == "on":
			os.system('sudo service ssh start')
			return jsonify({'msg':'Successfully started SSH', 'code':'success'})
		elif request.args.get('state') == "off":
			os.system('sudo service ssh stop')
			return jsonify({'msg':'Successfully stopped SSH', 'code':'success'})
		else:
			return jsonify({'msg':'You must specify the "state" parameter', 'code':'error'})
	else:
		resp.set_cookie('inmoov_session', '', expires=0)
		return jsonify({'msg':'You must authenticate first','code':'error'})

@socketio.on('connect', namespace='/websocket')
def websocket_connect():
	cookie = request.cookies.get('inmoov_session')
	result = db.sessions.find_one({"nonce":cookie})
	if result is not None:
		print('[WEBSOCKET] User connected !')
		update_subscribers(SUBSCRIBERS_LIST)
		emit_topiclist(SUBSCRIBERS_LIST)
	else:
		print('[WEBSOCKET] User failed to connect !')
		disconnect()
	return

@socketio.on('disconnect', namespace='/websocket')
def websocket_disconnect():
	disconnect()
    	print('User disconnected from websocket !')

@app.route('/admin/login', methods=['POST','GET'], strict_slashes=False)
def login():
	if request.method == 'GET':
		cookie = request.cookies.get("inmoov_session")
		result = db.sessions.find_one({"nonce":cookie})
		if result is not None:
			return (redirect(url_for('admin')),302)
		else:
			resp = make_response(render_template('login.html', msg=""))
			resp.set_cookie('inmoov_session', '', expires=0)
			return (resp,200)
	else:
		result = db.users.find_one({"username":request.form["username"]})
		if result is not None and hashlib.sha256(request.form['password']).hexdigest() == result['password']:
			nonce = ''.join(random.choice(string.letters + string.digits) for _ in range(64))
			db.sessions.insert_one({"username":result["username"],"nonce":nonce})
			resp = make_response(redirect(url_for('admin')))
			resp.set_cookie('inmoov_session', nonce)
			return (resp,302)
		else:
			resp = make_response(render_template('login.html', msg='Invalid username/password'))
			resp.set_cookie('inmoov_session', '', expires=0)
			return(resp,200)

@app.route('/admin/logout', methods=['GET'], strict_slashes=False)
def logout():
	cookie = request.cookies.get("inmoov_session")
	result = db.sessions.delete_one({"nonce":cookie})
	resp = make_response(render_template('logout.html'))
	resp.set_cookie('inmoov_session', '', expires=0)
	return (resp, 200)

##Si on lance direct le programme via python
if __name__ == '__main__':
		eventlet.wsgi.server(eventlet.listen(('0.0.0.0',5000)),app)
