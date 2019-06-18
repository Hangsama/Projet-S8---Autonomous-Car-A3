import serial
import time

ser = serial.Serial('/dev/ttyACM0',115200)
time.sleep(2)
while 1:
    str = raw_input("saisir : ")
    ser.write(str)
    #ser.write('a')
    #time.sleep(0.4)
    #ser.write('d')
    #time.sleep(0.4)

    #reponse = ser.readline()   #lire dans serial
    #print reponse
