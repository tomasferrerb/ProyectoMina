#! /usr/bin/env python
from tkinter import *
from tkinter import messagebox
import os

def accion(title,msg,command):
    MsgBox = messagebox.askquestion (title,msg,icon = 'warning')
    if MsgBox == 'yes':
       os.system(command)   #Desplegar mensaje en pantalla
       #master.quit()
       #root.destroy()
    #else:
        #messagebox.showinfo('Return','You will now return to the application screen')
     #   print("chao")


master = Tk()
A=master.winfo_screenwidth()
B=master.winfo_screenheight()
#master.geometry("{0}x{1}+0+0".format(A,B))
master.attributes('-fullscreen', True)
master.configure(background='white')

###IMAGENES DE BOTONES###
image1a = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton1a.png")
image1b = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton1b.png")
image1c = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton1c.png")

image2a = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton2a.png")
image2b = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton2b.png")
image2c = PhotoImage(file="/home/pi/Documents/ProyectoMina/boton2c.png")
##########################
#####COMANDOS A EJECUTAR##############
a="sudo sendSMS.py --number '+56959557124' --txt "
#+56976425035 alexis
#+56979017964 sim claro
#+56959557124 sim claro 2

command1a=a+'1a'
command1b=a+'1b'
command1c=a+'1c'

command2a=a+'2a'
command2b=a+'2b'
command2c=a+'2c'

###TITULOS DE VENTANAS EMERGENTES##########3
title1="TORMENTA DE VIENTO"
title2="TORMENTA ELÉCTRICA"
#########
###MENSAJES VENTANAS EMERGENTES#######
msgini="¿Está seguro que quiere mostrar el siguiente mensaje en las pantallas: '"
msgfin="'?"
msg1a="USO OBLIGATORIO DE BARBIQUEJO PROTECCION VISUAL HERMETICA"
msg1b="PERMITIDO CIRCULAR SOLO PERSONAL AUTORIZADO    (GERENTES,SUPERINTENDENTES,JEFES GENERALES,JEFES DE TURNO,PROTECCION INDUSTRIAL,GERENCIA SSO,VEHICULOS DE EMERGENCIA Y LOS AUTORIZADOS POR EL COMITÉ DE EMERGENCIA)"
msg1c="PROHIBICION DE CIRCULAR PEATONES Y VEHICULOS(TODOS REFUGIADOS) SOLO AUTORIZADOS VEHICULOS DE EMERGENCIA (AMBULANCIA,CARRO BOMBA,CARRO RESCATE,ENC EMERGENCIA,GERENCIA DE SEGURIDAD,PROTECCION INDUSTRIAL,EMERGENCIA OPERACIONAL,AUTORIZADO POR EL COMITE DE EMERGENCIA)"
msg2a="PERSONAL EN ESTADO DE ALERTA  PROHIBICION DE INGRESO DE VISITAS Y PROVEEDORES"
msg2b="RESTRICCION DE LA CIRCULACION DE PEATONES           PERMITIDO CIRCULAR SOLO VEHICULOS AUTORIZADOS (GERENTES,SUPERINTENDENTES,JEFES GENERALES,JEFES DE TURNO,PROTECCION INDUSTRIAL,GERENCIA SSO,VEHICULOS DE EMERGENCIA Y LOS AUTORIZADOS POR EL COMITÉ DE EMERGENCIA)"
msg2c="PROHIBICION ABSOLUTA DE CIRCULAR PEATONES Y VEHICULOS(TODOS REFUGIADOS) SOLO AUTORIZADOS VEHICULOS DE EMERGENCIA (AMBULANCIA,CARRO BOMBA,CARRO RESCATE,ENC EMERGENCIA,GERENCIA DE SEGURIDAD,PROTECCION INDUSTRIAL,EMERGENCIA OPERACIONAL,AUTORIZADO POR EL COMITE DE EMERGENCIA)"

#####LABELS
labelfont= ('arial', 24, 'bold')
l1=Label(master, text="ALERTA DE TORMENTA DE VIENTO",bg="white",font=labelfont).place(relx=0.5,rely=0.1,anchor=CENTER)
boton1a = Button(master,	bg="white",	bd=0,	image=image1a,	command=lambda:accion(title1,msgini+msg1a+msgfin,command1a)).place(relx=0.17, rely=0.3, anchor=CENTER)
boton1b = Button(master,	bg="white",	bd=0,	image=image1b,	command=lambda: accion(title1,msgini+msg1b+msgfin,command1b)).place(relx=0.5, rely=0.3, anchor=CENTER)
boton1c = Button(master,	bg="white",	bd=0,	image=image1c ,	command=lambda:accion(title1,msgini+msg1c+msgfin,command1c)).place(relx=0.83, rely=0.3, anchor=CENTER)



l2=Label(master,	text="ALERTA DE TORMENTA ELÉCTRICA",	bg="white",	font=labelfont).place(relx=0.5,rely=0.6,anchor=CENTER)
boton2a = Button(master,	image=image2a,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2a+msgfin,command2a)).place(relx=0.17, rely=0.8, anchor=CENTER)
boton2b = Button(master,	image=image2b,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2b+msgfin,command2b)).place(relx=0.5, rely=0.8, anchor=CENTER)
boton2c = Button(master,	image=image2c,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2c+msgfin,command2c)).place(relx=0.83, rely=0.8, anchor=CENTER)


master.mainloop()
