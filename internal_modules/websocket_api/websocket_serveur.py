#!/usr/bin/python3
#-*- coding: utf-8 -*-

import rospy, json, websockets, asyncio, sys
from std_msgs.msg import String

sys.path.append('/home/InMoov/inmoov_catkin_ws/src/inmoov/scripts')
from inmoov_controller_client import InMoov_Controller_Client

def get_all_paths(tree, cur=()):
	if not tree or 'items' not in dir(tree):
		yield cur
	else:
		for n, s in tree.items():
			for path in get_all_paths(s, cur+(n,)):
				yield path

class WSServer:
	def __init__(self, host, port):
		self.host = host
		self.port = port
		self.client = InMoov_Controller_Client()

	def start(self):
		return websockets.serve(self.handler, self.host, self.port)

	async def handler(self, websocket, path):
		received = await websocket.recv()
		rospy.loginfo('[Websocket API] Received message !')
		try:
			data = json.loads(received)
			rospy.loginfo(data)
			if self.is_valid_message(data) == False:
				sent = '{"status":"failed", "msg":"Data is not a valid control_json"}'
			elif self.is_authorized_addon(data['api_token']) == False:
				sent = '{"status":"failed", "msg":"Unauthorized API token"}'
			else:
				self.client.send_goal()
				self.client.update_control_json(data)
				sent = '{"status":"OK", "msg":"Well received"}'
		except Exception as e:
			rospy.loginfo("[Websocket API] Error : " + str(e))
			sent = '{"status":"failed", "msg":"Data is not JSON"}'
		await websocket.send(sent)
		rospy.loginfo("[Websocket API] Response : %s" % sent)

	def is_authorized_addon(self, api_token):
		if api_token == 'yolo':
			return True
		return False

	def get_reference_paths(self):
		return list(get_all_paths(self.client.get_control_json()))

	def is_valid_message(self, message):
		ref_paths = self.get_reference_paths() #.append(('api_token',))
		new_paths = list(get_all_paths(message))
		ref_paths.append(('api_token',))
		if set(ref_paths) == set(new_paths):
			return True
		else:
			return False


if __name__ == '__main__':
	try:
		rospy.init_node('websocket_server_node', anonymous=True, disable_signals=True)
		rospy.loginfo("[Websocket API] Starting ...")
		ws = WSServer('0.0.0.0', 8765)
		asyncio.get_event_loop().run_until_complete(ws.start())
		asyncio.get_event_loop().run_forever()
	except rospy.ROSInterruptException:
		pass
