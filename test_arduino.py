#/usr/bin/python

import serial, requests, json

port = '/dev/ttyUSB0'
baudrate = 9600

webhook = "https://ieee.rocket.chat/hooks/QyENddBsodbMzyKz3/G6XB6iyCgbbgPwf9BaZAtP7pDFzaFFuiiXig9rZ2Mo2diCRN"
token = "QyENddBsodbMzyKz3/G6XB6iyCgbbgPwf9BaZAtP7pDFzaFFuiiXig9rZ2Mo2diCRN"

# curl -X POST -H 'Content-Type: application/json' --data '{"text":"Example message","attachments":[{"title":"Rocket.Chat","title_link":"https://rocket.chat","text":"Rocket.Chat, the best open source chat","image_url":"https://rocket.chat/images/mockup.png","color":"#764FA5"}]}' https://ieee.rocket.chat/hooks/QyENddBsodbMzyKz3/G6XB6iyCgbbgPwf9BaZAtP7pDFzaFFuiiXig9rZ2Mo2diCRN
headers = {"Content-Type": "application/json"}
data = {}

sensorport = serial.Serial(port,baudrate)

# Ler Primeira Linha
sensorport.readline();

# Ler os dados
while sensorport.isOpen():
	'''Ler Arduino e Separa dados dos sensores'''
    
	try:
		line = sensorport.readline()
    		raw_reading = line.rstrip('\r\n').split(";")
    		sensor_reading = map(float, raw_reading)
	except:
		# retorna
		# [float(temp),float(luminosidade)]
		# [celsius, 0:5]
   	 	print sensor_reading
		data = { "temp": sensor_reading[0], "lum": sensor_reading[1]}
    		response = requests.post(webhook, data=json.dumps(data), headers=headers)

sensorport.close()
