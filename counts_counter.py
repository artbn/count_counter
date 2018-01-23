import websocket
import config
import praw
import json
import time
import datetime


def bot_login():
	print("Logging In...")
	login = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "Tracks counts in /r/livecounting")
	print("Logged in!")
	return login

def thread_about():
	#Returns the live thread's about.json data, including the WebSocket (wss) URL, sidebar (resources) contents, etc.
	
	# Get websocket_url from about.json
	response = login.request(
		method = 'GET',
		path = 'live/' + config.thread + '/about',
		params = { 'raw_json': 1 }
	);

	# Return websocket_url from response
	return response;


def reset():
	with open('count.txt','w') as count_file, open('counts.txt', 'w') as counts_file:
		count_file.write('0')

def get_count_vars():
	with open('count.txt') as count_file, open('counts.txt') as counts_file:
		count = int(count_file.readline())
		counts = counts_file.readlines()

	return count, counts

def write_count_vars(count, name=""):
	with open('count.txt', 'w') as count_file, open('counts.txt', 'a') as counts_file:
		count = count_file.write(str(count))
		counts_file.write('%s\n' % name)

def on_message(ws,data): 
	request = json.loads(data) # converts from string to array

	if request['type'] == 'activity': return

	count, counts = get_count_vars()

	if request['type'] == 'update':
		author = request['payload']['data']['author']
		name = request['payload']['data']['name']
		body = request['payload']['data']['body']

		if author == config.username:
			if body[0].isnumeric():
				count = count + 1

				print(count)
				write_count_vars(count, name)

	elif request['type'] == 'strike':
		if request['payload'] + "\n" in counts:
			count = count - 1
			print("%s (count stricken)" % count)
			write_count_vars(count)

reset()

login = bot_login()

# Retrieve WebSocket URL
websocket_url = (thread_about())['data']['websocket_url'];

def on_close(ws):
	print('WebSocket connection attempting to close')
	ws.run_forever()

def on_open(ws):
	print('WebSocket connection opened')

def connect():
	# Now connect to the websocket
	ws = websocket.WebSocketApp(
	    websocket_url,
	    on_open = on_open,
	    on_close = on_close,
	    on_message = on_message
	)
	ws.run_forever();

while 1:
	try:
		connect()
	except:
		time.sleep(3)
		connect()
		print("Tracker is back on!")