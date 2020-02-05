import time
import serial
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT)

ser = serial.serial("/dev/serial0", 115200)

while True:
	GPIO.output(8, False)
	print(ser)

