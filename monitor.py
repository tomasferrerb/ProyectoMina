#!/usr/bin/env python3
from tkinter import *
from tkinter import Label
import time
import re
import time
import argparse


    
def makeWindow(msg,color,time):
	
	root = Tk()
	root.configure(background=color)
	w = Label(root, text='\n'+msg,bg=color,font=('Helvetica',200))
	w.pack()	
	#root.overrideredirect(True)  #barra de tareas
	#root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
	#root.focus_set()  # <-- move focus to this widget
	root.attributes('-fullscreen', True)
	#root.bind('Esc', lambda e: root.quit())
	root.after(time*1000, lambda: root.destroy())
	#root.after(time*1000, lambda: salir())
	root.mainloop()



#vcgencmd display_power 0/1 ########################PRENDER Y APAGAR PANTALLA POR CONSOLA#########################3
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fullscreen messages displayer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--message', type=str,help='message')
    parser.add_argument('--color',type=str,default='green',help='colo of background') 
    parser.add_argument('--time',type=int,default=5, help='time to show the message in seconds')

    args = parser.parse_args()

    try:
        makeWindow(args.message,args.color,args.time)
    except KeyboardInterrupt:
        pass

