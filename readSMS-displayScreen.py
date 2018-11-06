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

#os.system('vcgencmd display_power 0') #Turn off HDMI signal

def lastPart(str,i):
    l=str.split('\n',50)
    return l[i]

def extraerCampo(str,i):
    l=str.split('-',50)
    return l[i]

def cualOpcion(str): 
    if 'password' in str:  
        tmp=''
        opciones=['1a', '1b', '1c', '2a','2b','2c']
        for i in opciones: 
            if i in msg:
                tmp=i
                return tmp
    return 'no sms' #

#######PASSWORD#####
###contrasenia=password
#    0      1     2
##password-opt-tiempo

reply = ser.read(ser.inWaiting()) # Clean buf
print ("Listening for incomming SMS...")
while True:
    msg=''
    tiempo=0
    reply = ser.read(ser.inWaiting())
    if reply != "":


        ser.write("AT+CMGR=1\n") 
        time.sleep(1)
        reply = ser.read(ser.inWaiting())
        print("SMS received. Content:")
        print(reply)
        
        try:
        	msg=lastPart(reply,4) #contenido de texto es la 5ta linea del SMS
        except: 
			print('Wrong SMS')
        print(msg)
        
        
        tmp=cualOpcion(msg)	#identificar opcion de SMS 
        try:
            tiempo=int(extraerCampo(msg,2)) #el campo 2 es el de tiempo
        except:
            print('time is not an integer')
            tiempo='time error'
        print(tiempo)
        if ((tmp != 'no sms') and isinstance(tiempo, int)):
           # os.system('vcgencmd display_power 1') #Turn on HDMI signal
            time.sleep(1)
    
            command='python /home/pi/Documents/ProyectoMina/displayScreen-sinfotos-apagar.py --imagen '+tmp+ ' --tiempo '+str(tiempo)
	 
            os.system(command)
            #os.system('vcgencmd display_power 0') #Turn off HDMI signal
        else: print('Format error')    
        time.sleep(.500)
        ser.write('AT+CMGDA="DEL ALL"\n') # delete all
        time.sleep(.500)
        ser.read(ser.inWaiting()) # Clear buffer
        time.sleep(.500)  
#os.system('vcgencmd display_power 1') #Turn on HDMI signal no pasa al final
