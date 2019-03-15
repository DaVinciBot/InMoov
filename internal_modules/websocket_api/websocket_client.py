#!/usr/bin/python3

import websockets, asyncio, sys, json

async def send(uri, data):
	async with websockets.connect(uri) as websocket:
		await websocket.send(data)
		print("> %s" % data)
		received = await websocket.recv()
		print("< %s" % received)
if len(sys.argv) != 2:
	print("Usage : %s <data>" % sys.argv[0])
	exit(0)
with open(sys.argv[1], 'r') as f:
	data = f.read()
	print(data.encode('utf-8'))
asyncio.get_event_loop().run_until_complete(send('ws://192.168.1.107:8765', data))
