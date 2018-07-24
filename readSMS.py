#This is an open-source code
#Created by Noel S. Orbong Jr. 
#16 january 2017

#import RPi.GPIO as GPIO
import serial
import os, time, sys
import datetime

#def setup():
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setwarnings(False)
    #GPIO.setup(23, GPIO.OUT)
    #GPIO.setup(24, GPIO.OUT)
    #GPIO.setup(25, GPIO.OUT)

SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port

ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
#setup()
ser.write('AT+CMGF=1'+'\r\n') # set to text mode
time.sleep(1)
ser.write('AT+CMGDA="DEL ALL"\n') # delete all SMS
time.sleep(1)
reply = ser.read(ser.inWaiting()) # Clean buf
print ("Listening for incomming SMS...")
while True:
    reply = ser.read(ser.inWaiting())
    if reply != "":
		ser.write('AT'+'\r\n')
		time.sleep(5)
		ser.write('AT+CMGF=1'+'\r\n') # set to text mode
        #time.sleep(1)
        ser.write("AT+CMGR=1\n") 
        time.sleep(1)
        reply = ser.read(ser.inWaiting())
        print("SMS received. Content:")
        print(reply)
        command='python3 monitor.py --message "'+reply+'"'
        os.system(command)
	
 	#if "ON" in reply.upper():
	    #if "LED1" in reply.upper():
                #print "LED 1 ON"
                #GPIO.output(23,GPIO.HIGH)
	    #if "LED2" in reply.upper():
                #print "LED 2 ON"
                #GPIO.output(24,GPIO.HIGH)
            #if "LED3" in reply.upper():
                #print "LED 3 ON"
                #GPIO.output(25,GPIO.HIGH)
            #if "ALL" in reply.upper():
		#print ("ALL LED ON")
                #GPIO.output(23,GPIO.HIGH)
                #GPIO.output(24,GPIO.HIGH)
                #GPIO.output(25,GPIO.HIGH)
	#if "OFF" in reply.upper():
	    #if "LED1" in reply.upper():
                #print "LED 1 OFF"
                #GPIO.output(23,GPIO.LOW)
	    #if "LED2" in reply.upper():
                #print "LED 2 OFF"
                #GPIO.output(24,GPIO.LOW)
            #if "LED3" in reply.upper():
                #print "LED 3 OFF"
                #GPIO.output(25,GPIO.LOW)
            #if "ALL" in reply.upper():
                #print "ALL LED OFF"
                #GPIO.output(23,GPIO.LOW)
                #GPIO.output(24,GPIO.LOW)
                #GPIO.output(25,GPIO.LOW)
        
        time.sleep(.500)
        ser.write('AT+CMGDA="DEL ALL"\n') # delete all
        time.sleep(.500)
        ser.read(ser.inWaiting()) # Clear buffer
        time.sleep(.500)  
