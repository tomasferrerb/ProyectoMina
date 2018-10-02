import serial
import os, time, sys
import datetime



#os.system('vcgencmd display_power 0') #Turn off HDMI signal


SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port

ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
#setup()
##ser.write('AT'+'\r\n')
##time.sleep(10)
ser.write('AT+CMGF=1'+'\r\n') # set to text mode
time.sleep(1)
ser.write('AT+CMGDA="DEL ALL"\n') # delete all SMS
time.sleep(1)

os.system('vcgencmd display_power 0') #Turn off HDMI signal

def lastPart(str,i):
    l=str.split('\n',20)
    return l[i]

def lastPartSet(str,i):
    l=str.split(',',20)
    return l[i]

def cualOpcion(str): 
    if 'password' in str:  
        tmp=''
        opciones=['1a', '1b', '1c', '2a','2b','2c']
        for i in opciones: 
            if i in msg:
                tmp=i
                return tmp


#######PASSWORD#####
###contrasenia=password


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
##        for p in range(6):
##            lala=lastPart(reply,p)
##            print(lala+str(p))

        msg=lastPart(reply,4)
        print(msg)
        os.system('vcgencmd display_power 1') #Turn on HDMI signal
        time.sleep(1)

        tmp=cualOpcion(msg)
        
        command='python3 /home/pi/Documents/ProyectoMina/displayScreen-sinfotos.py --imagen '+tmp
 
        os.system(command)
        os.system('vcgencmd display_power 0') #Turn off HDMI signal
        
        time.sleep(.500)
        ser.write('AT+CMGDA="DEL ALL"\n') # delete all
        time.sleep(.500)
        ser.read(ser.inWaiting()) # Clear buffer
        time.sleep(.500)  
#os.system('vcgencmd display_power 1') #Turn on HDMI signal no pasa al final
