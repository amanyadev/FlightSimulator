from selenium import webdriver
from random import randint
from time import sleep
 #used this for entering data to the arduino
import pyfirmata
import time
import re
def main():
    #setup
    driver = webdriver.Chrome()
    driver.get("http://localhost:8111")
    #needed states.
    states = {
    'stt-H, m':'',
    'stt-TAS, km/h':'',
    'stt-IAS, km/h':'',
    'stt-M':'',
    'stt-AoA, deg':'',
    'stt-AoS, deg':'',
    'stt-Ny':'',
    'stt-Vy, m/s':'',
    'stt-Wx, deg/s':'',
    'stt-elevator, %':'',
    'stt-rudder, %':'',
    'stt-flaps, %':'',
    'stt-gear, %':'',
    'stt-airbrake, %':'',
    }

    time.sleep()
    board = pyfirmata.Arduino("COM3")
    right = board.get_pin('d:10:s')

    it = pyfirmata.util.Iterator(board)
    it.start()

    while True:
       # elements = driver.find_element_by_id("stt-IAS, km/h")
        #for key in states:
        #   states[key] = driver.find_element_by_id(key).text
        #print(states)
        TAS = driver.find_element_by_id('stt-TAS, km/h').text
        print(type(TAS))                   #
        nu = re.findall("(\d+)",TAS)
        print(nu)
        angle = (int(nu[0])/500)*180
        right.write(angle)




















if __name__ == "__main__":
    main()