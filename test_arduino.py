#/usr/bin/python

import serial, requests, json

port = '/dev/ttyACM1'
baudrate = 9600
UP = 10

webhook = 'https://ieee.rocket.chat/hooks/QyENddBsodbMzyKz3/G6XB6iyCgbbgPwf9BaZAtP7pDFzaFFuiiXig9rZ2Mo2diCRN'

# curl -X POST -H 'Content-Type: application/json' 
# --data '{"text":"Example message", "attachments": 
# [{"title":"Rocket.Chat", 
# "title_link":"https://rocket.chat", 
# "text":"Rocket.Chat, the best open source chat",
# "image_url":"https://rocket.chat/images/mockup.png","color":"#764FA5"}]}' 
# https://ieee.rocket.chat/hooks/QyENddBsodbMzyKz3/G6XB6iyCgbbgPwf9BaZAtP7pDFzaFFuiiXig9rZ2Mo2diCRN
headers = {"Content-Type": "application/json"}
data = {}

sensorport = serial.Serial(port,baudrate)

# Ler Primeira Linha
sensorport.readline()

last_sensor = [0, 11]
# Ler os dados
while sensorport.isOpen():
	'''Ler Arduino e Separa dados dos sensores'''

	try:
		line = sensorport.readline()
    		raw_reading = line.rstrip('\r\n').split(';')
    		# return [float(temp), float(lum)]
		# [celsius, 0:5]
		sensor_reading = map(float, raw_reading)
		
		if sensor_reading[1] >= UP and last_sensor[1] < UP:
			print sensor_reading[0], 'ACESO'
			last_sensor = sensor_reading
			data = { "temp": sensor_reading[0], "lum": 1}
	                response = requests.post(webhook, data=json.dumps(data), headers=headers)
		elif sensor_reading[1] < UP and last_sensor[1] >= UP:	
			print sensor_reading[0], 'DESLIGADO'
			last_sensor = sensor_reading
			data = { "temp": sensor_reading[0], "lum": 0}
                        response = requests.post(webhook, data=json.dumps(data), headers=headers)			
	except:
		pass

sensorport.close()
