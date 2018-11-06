from tkinter import *
from tkinter import messagebox
import argparse
import serial
import os, time, sys
import datetime


master = Tk()

def lastPart(str,i):
    l=str.split('\n',20)
    return l[i]

def lastPartSet(str,i):
    l=str.split(',',20)
    return l[i]

def apagarSMS(): 
	SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port

	ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
	#setup()
	##ser.write('AT'+'\r\n')
	##time.sleep(10)
	ser.write('AT+CMGF=1'+'\r\n') # set to text mode
	time.sleep(1)
	ser.write('AT+CMGDA="DEL ALL"\n') # delete all SMS
	time.sleep(1)
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
			
			if 'password-apagar' in msg:
				master.destroy()
			time.sleep(.500)
			ser.write('AT+CMGDA="DEL ALL"\n') # delete all
			time.sleep(.500)
			ser.read(ser.inWaiting()) # Clear buffer
			time.sleep(.500)

def displayScreen(opt, tiempo):

	A=master.winfo_screenwidth()
	B=master.winfo_screenheight()
	master.geometry("100x100+8+153")
	#master.attributes('-fullscreen', True)
	sizefont=6
	fgcolor="white"
	ATV='TORMENTA DE VIENTO \n'
	ATE='TORMENTA ELÉCTRICA \n'
	if '1a' == opt:
		color='blue'
		sizefont=6
		txt=ATV+'USO OBLIGATORIO\n DE BARBIQUEJO \nPROTECCION\n VISUAL \nHERMETICA'
	if '1b' == opt: 
		color='yellow' 
		#sizefont=8
		fgcolor="black"
		txt=ATV+'PERMITIDO \nCIRCULAR \nSOLO PERSONAL \nAUTORIZADO'
	if '1c' == opt: 
		color='red'  
		#sizefont=7
		txt=ATV+'PROHIBICION DE \nCIRCULAR \nPEATONES Y \nVEHICULOS\n(Todos refugiados)\n SOLO AUTORIZADOS\n VEHICULOS DE \nEMERGENCIA  '
	if '2a' == opt:
		color='blue' 
		#sizefont=7
		txt=ATE+'PERSONAL EN  \n ESTADO DE \n ALERTA \n  Prohibición de \n ingreso  de \nvisitas  y \nproveedores' 		
	if '2b' == opt: 
		color='yellow' 
		#sizefont=7
		fgcolor="black"
		txt=ATE+'RESTRICCION DE LA\n CIRCULACION DE\n PEATONES\n   PERMITIDO \nCIRCULAR\n SOLO VEHICULOS\n AUTORIZADOS'
	if '2c' == opt: 
		color='red'
		sizefont=5
		txt=ATE+'PROHIBICION\n ABSOLUTA DE\n CIRCULAR PEATONES\n Y VEHICULOS\n(Todos refugiados)\n  SOLO AUTORIZADOS\n VEHICULOS DE\n EMERGENCIA '   
	 
	master.configure(background=color)
	l1=Label(master, text=txt,fg=fgcolor, font=(None,sizefont),bg=color).place(relx=0.5,rely=0.5,anchor=CENTER)
	master.after(int(1000), lambda: apagarSMS())
	master.mainloop()





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='mostrar imagen en pantalla completa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--imagen', type=str,help='seleccionar imagen, opciones: 1a, 1b, 1c, 2a, 2b, 2c')
    parser.add_argument('--tiempo', type=float,help='tiempo en horas que se quiere mostrar alerta')


    args = parser.parse_args()

    try:
        displayScreen(args.imagen, args.tiempo)
    except KeyboardInterrupt:
        pass






if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='mostrar imagen en pantalla completa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--imagen', type=str,help='seleccionar imagen, opciones: 1a, 1b, 1c, 2a, 2b, 2c')



    args = parser.parse_args()

    try:
        displayScreen(args.imagen)
    except KeyboardInterrupt:
        pass

