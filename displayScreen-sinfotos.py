from tkinter import *
from tkinter import messagebox
import os
import argparse
import time


def displayScreen(opt, tiempo):

	master = Tk()
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
	master.after(int(tiempo*1000*60*60), lambda: master.destroy())
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

