from tkinter import *
from tkinter import messagebox
import os
import argparse
import time


def displayScreen(opt):

	master = Tk()
	A=master.winfo_screenwidth()
	B=master.winfo_screenheight()
	#master.geometry("{0}x{1}+0+0".format(A,B))
	master.attributes('-fullscreen', True)
	master.configure(background='white')
	nombre = "/home/pi/Documents/ProyectoMina/boton"+ opt +".png"
	print(opt)
	print(nombre)
###IMAGENES A MOSTRAR###
	imagen = PhotoImage(file=nombre)
	imagen=imagen.zoom(4, 4)
	
	boton1a = Button(master,bg="white",bd=0,text='X',command=lambda:master.quit()).place(relx=0.1, rely=0.9, anchor=CENTER)
        
	tiempo=5 #tiempo de mustra en segundos
	l1=Label(master, image=imagen,bg="white").place(relx=0.5,rely=0.5,anchor=CENTER)
	master.after(tiempo*1000, lambda: master.destroy())
	master.mainloop()





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='mostrar imagen en pantalla completa',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--imagen', type=str,help='seleccionar imagen, opciones: 1a, 1b, 1c, 2a, 2b, 2c')



    args = parser.parse_args()

    try:
        displayScreen(args.imagen)
    except KeyboardInterrupt:
        pass

