import serial
import numpy as np     
import matplotlib.pyplot as plt 
ser = serial.Serial('COM3')

# Define Variables
Accx = []
Accy = []
Accz = []
while(True):
    len = 51

    for i in range (len):               # Wait until the buffer is filled up to 50 values
        while (ser.inWaiting() == 0):   
            pass                        
            
        arduinoString = ser.readline().decode("utf-8").strip()  
        dataArray = (arduinoString.split(','))      # Since the values are being sent consecutively, 
        print(dataArray[0]);                                            # the values must be split into x,y,and z

        
