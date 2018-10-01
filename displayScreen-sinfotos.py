from tkinter import *
from tkinter import messagebox
import os
import argparse
import time


def displayScreen(opt):

	master = Tk()
	A=master.winfo_screenwidth()
	B=master.winfo_screenheight()
	master.geometry("100x100+10+186")
	#master.attributes('-fullscreen', True)
	
	if 'a' in opt:
		color='blue' 
	if 'b' in opt: 
		color='yellow' 
	if 'c' in opt: 
		color='red'   
	tiempo=5 #tiempo de mustra en segundos
	master.configure(background=color)
	l1=Label(master, text=opt,fg="black", font=(None,20),bg=color).place(relx=0.5,rely=0.5,anchor=CENTER)
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

