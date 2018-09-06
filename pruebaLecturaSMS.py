

import serial
import os, time, sys
import datetime




SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port

ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)

##ser.write('AT'+'\r\n')
##time.sleep(10)
ser.write('AT+CMGF=1'+'\r\n') # set to text mode
time.sleep(1)
ser.write('AT+CMGDA="DEL ALL"\n') # delete all SMS
time.sleep(1)


def lastPart(str,i):
    l=str.split('\n',20)
    return l[i]

def lastPartSet(str,i):
    l=str.split(',',20)
    return l[i]

reply = ser.read(ser.inWaiting()) # Clean buf
print ("Listening for incomming SMS...")
while True:
    reply = ser.read(ser.inWaiting())
    if reply != "":


        ser.write("AT+CMGR=1\n") 
        time.sleep(1)
        reply = ser.read(ser.inWaiting())
        print("SMS received. Content:")
        print(reply)


        reply=lastPart(reply,4)
        msg=lastPartSet(reply,0)
        clr=lastPartSet(reply,1)
                        
        os.system("echo "+msg)
        print(clr)

        time.sleep(1)

        
        time.sleep(.500)
        ser.write('AT+CMGDA="DEL ALL"\n') # delete all
        time.sleep(.500)
        ser.read(ser.inWaiting()) # Clear buffer
        time.sleep(.500)  
