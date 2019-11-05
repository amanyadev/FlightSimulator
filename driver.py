'''import serial
import time
import random
from Arduino import Arduino
ser = serial.Serial()
board = Arduino("9600",port='COM3')

board.Servos.attach(0)
time.sleep(1)

for i in range(270):
    angle = random.randint(0,180)
    board.Servos.write(0,angle)
    print(angle)
    time.sleep(1)
print(board.Servos.read(0))

board.Servos.detach(0)
'''
from random import randint
from time import sleep
import pyfirmata
board = pyfirmata.Arduino("COM3")
right = board.get_pin('d:10:s')

it = pyfirmata.util.Iterator(board)
it.start()

for i in range(100000):
    
    angle = randint(0,180)
    if angle>90:
        sleep(.5)
    elif angle < 90:
        sleep(.25)
    if angle > 150:
        sleep(1)
    right.write(angle)
    print(angle)
