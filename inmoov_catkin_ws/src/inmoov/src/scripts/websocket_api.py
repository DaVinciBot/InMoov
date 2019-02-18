#!/usr/bin/python3
#-*- coding: utf-8 -*-

import rospy, json, websockets, asyncio, sys
from std_msgs.msg import String

CONTROL_JSON_FILE = '/addons/config/control_json.json'

def get_reference_keys():
	with open(CONTROL_JSON_FILE) as f:
		ref = f.read()
	try:
		ref = json.loads(ref)
	except:
		exit(0)
	print(ref)
	return ref.keys()

def is_valid_message(message):
	ref_keys = get_reference_keys().append('api_token')
	new_keys = message.keys()
	if set(ref_keys) == set(new_keys):
		return True
	else:
		return False

class WSServer:
	def __init__(self, host, port, dispatcher_topic):
		self.host = host
		self.port = port
		self.publisher = rospy.Publisher(dispatcher_topic, String, queue_size=10)

	def start(self):
		return websockets.serve(self.handler, self.host, self.port)
	async def handler(self, websocket, path):
		received = await websocket.recv()
		rospy.loginfo('[Websocket API] Received : %s' % received)
		try:
			data = json.loads(received)
			self.publisher.publish(str(data))
			rospy.loginfo("[Websocket API] Sent '%s' to Dispatcher" % str(data))
			sent = '{"status":"OK", "msg":"Well received"}'
		except:
			sent = '{"status":"failed", "msg":"Data is not JSON"}'
		await websocket.send(sent)
		rospy.loginfo("[Websocket API] Response : %s" % sent)

if __name__ == '__main__':
	try:
		rospy.init_node('websocket_api_node', anonymous=True, disable_signals=True)
		rospy.loginfo("[Websocket API] Starting ...")
		ws = WSServer('0.0.0.0', 8765, "dispatcher_topic")
		asyncio.get_event_loop().run_until_complete(ws.start())
		asyncio.get_event_loop().run_forever()
	except rospy.ROSInterruptException:
		pass
