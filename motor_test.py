#May have to import another library depending on what pulsewidth the Vex  ESC accept
#Will have backwards funtionality one of two ways
#Way one is wiring the rear motors opposite of front motors making it rear wheel drive in either direction
#Way two is dependent on how the ESC accepts the pulsewidths and at what ranges
#Pulse width is determined by duty cycle and Frequency


import RPi.GPIO as GPIO #Pin setup for Entire Pi
import time
import curses #User Interface
import serial
#pin setup, allows the code to reference these pins later in the code
GPIO.setmode(GPIO.BOARD) #.BOARD lets the pi know you are using the board numbers
GPIO.setup(13, GPIO.OUT) #Declare GPIO pin 13
GPIO.setup(22, GPIO.OUT) #Declare GPIO pin 22
GPIO.setup(15, GPIO.OUT) #Declare GPIO pin 15
GPIO.setup(18, GPIO.OUT) #Declare GPIO pin 18



#motor varibles, PWM is pulse width modulation
FR= GPIO.PWM(13,50)#Front Right Motor #The value 50 is the Frequency (The front right motor must be connected to GPIO 13)
FL= GPIO.PWM(22,50)#Front Left Motor #The value 22 is the GPIO pin
RR= GPIO.PWM(15,50)#Rear Right Motor
RL= GPIO.PWM(18,50)#Rear Left Motor
FR.start(100) #100 is the duty cycle
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
  char = screen.getch() # Get user input
#  dy = str(ser.readline())[30:36]
#  y = (dy)
#  print(y)
#  Takes input and tests if it is equal to the ASCII value, if so it moves in the direction printed
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
#cleanup and wraps up the curses
GPIO.cleanup
curses.nobreak()
screen.keypad(0)
curses.echo()
curses.endwin()
