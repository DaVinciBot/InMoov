#!/usr/bin/python3

import websockets, asyncio, sys

async def send(uri, data):
	async with websockets.connect(uri) as websocket:
		await websocket.send(data)
		print("> %s" % data)
		received = await websocket.recv()
		print("< %s" % received)
if len(sys.argv) != 2:
	print("Usage : %s <data>" % sys.argv[0])
	exit(0)
asyncio.get_event_loop().run_until_complete(send('ws://192.168.1.107:8765',sys.argv[1]))
