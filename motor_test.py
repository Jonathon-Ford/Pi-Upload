
#May have to import another library depending on what pulsewidth the Vex  ESC accept
#Will have backwards funtionality one of two ways
#Way one is wiring the rear motors opposite of front motors making it rear wheel drive in either direction
#Way two is dependent on how the ESC accepts the pulsewidths and at what ranges
#Pulse width is determined by duty cycle and Frequency


import RPi.GPIO as GPIO #Pin setup for Entire Pi
import time
import curses #User Interface
import serial
#pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)



#motor varibles
FR= GPIO.PWM(13,50)#Front Right Motor #The value 50 is the Frequency 
FL= GPIO.PWM(22,50)#Front Left Motor #The value 12 is the GPIO pin
RR= GPIO.PWM(15,50)#Rear Right Motor
RL= GPIO.PWM(18,50)#Rear Left Motor
FR.start(100)
FL.start(100)
RR.start(100)
RL.start(100)
#curses setup
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
#User Interface
#ser = serial.Serial("/dev/ttyUSB0", 115200)
while True:
  char = screen.getch()
#  dy = str(ser.readline())[30:36]
#  y = (dy)
#  print(y)
  if char == ord('k'):
    break
  elif char == ord('x'):
    print('Moving reverse')
    FR.ChangeDutyCycle(8)
    FL.ChangeDutyCycle(6.5)
    RR.ChangeDutyCycle(8)
    RL.ChangeDutyCycle(6.5)
  elif char == ord('w'):
    print('Moving forward')
    FR.ChangeDutyCycle(6.5)
    FL.ChangeDutyCycle(8)
    RR.ChangeDutyCycle(6.5)
    RL.ChangeDutyCycle(8)
  elif char == ord('s'):
    print('Stopping')
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)
  elif char == ord('a'):
    print('Turning Left')
    FR.ChangeDutyCycle(5)
    FL.ChangeDutyCycle(5)
    RR.ChangeDutyCycle(5)
    RL.ChangeDutyCycle(5)
  elif char == ord('d'):
    print('Turning Right')
    FR.ChangeDutyCycle(10)
    FL.ChangeDutyCycle(10)
    RR.ChangeDutyCycle(10)
    RL.ChangeDutyCycle(10)
#  elif y == -800:
#    print("arrived")
#cleanup
GPIO.cleanup
curses.nobreak()
screen.keypad(0)
curses.echo()
curses.endwin()
