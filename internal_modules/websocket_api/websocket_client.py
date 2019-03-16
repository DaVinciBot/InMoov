#!/usr/bin/python3

import websockets, asyncio, json, argparse
DEBUG = False

async def send(uri, data):
	async with websockets.connect(uri) as websocket:
		await websocket.send(data)
		if DEBUG: print("> %s" % data)
		received = await websocket.recv()
		if DEBUG: print("< %s" % received)
		return json.loads(received)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='InMoov Command Line Client |  AUTHOR : DaVinciBot')
	parser.add_argument('ip', help='InMoov IP Address',metavar='ip')
	parser.add_argument('command', help='Command to execute : info or move',metavar='command', choices=['move', 'info'])
	parser.add_argument('-f', help='File containing the move request for "move" command or the output for "info" command',metavar='file', required=True)
	parser.add_argument('-x', help='InMoov Addon Token',metavar='token', required=True)
	parser.add_argument('-p', help='InMoov API Port (default : 8765)',metavar='port', type=int, default=8765, required=False)
	parser.add_argument('-v', help='Verbose', action='store_true', required=False)
	args = parser.parse_args()	

	if args.v == True:
		DEBUG = True

	if args.command == "info":
		data = json.dumps({"action":"info","argument":"","addon_token":"%s" % args.x})
		received = asyncio.get_event_loop().run_until_complete(send('ws://%s:%d' % (args.ip, args.p), data))
		if received['status'] == 'OK':
			print('Actual position received : \n%s' % received['msg'])
			if args.f is not None:
				with open(args.f, 'w') as f:
					f.write(str(received['msg']).replace('\'', '"') + "\n")
		else:
			print('Error : %s' % received['msg'])
			exit(1)
	else:
			try:
				if args.f is None:
					move_request = json.loads(input("Please manually input your move request JSON (or specify a file with -f)"))

				else:
					with open(args.f, 'r') as f:
						move_request = json.loads(f.read())
			except ValueError:
				print("Error : Input is not a valid JSON.")
				exit(1)
			except IOError:
				print("Error : File not found")
				exit(1)
			data = json.dumps({"action":"move","argument":move_request,"addon_token":"%s" % args.x})
			received = asyncio.get_event_loop().run_until_complete(send('ws://%s:%d' % (args.ip, args.p), data))
			if received['status'] == 'OK':
				print('Move goal reached !')
			else:
				print('Error : %s' % received['msg'])
				exit(1)
	exit(0)
