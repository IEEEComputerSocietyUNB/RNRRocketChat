#/usr/bin/python

import serial

port = '/dev/ttyUSB0'
baudrate = 9600

sensorport = serial.Serial(port,baudrate)

# Ler Primeira Linha
sensorport.readline();

# Ler os dados
while sensorport.isOpen():
    '''Ler Arduino e Separa dados dos sensores'''
    line = sensorport.readline()
    raw_reading = line.rstrip('\r\n').split(";")
    sensor_reading = map(raw_reading,float)

    # @todo Colocar API rocketchat
    print sensor_reading

sensorport.close()