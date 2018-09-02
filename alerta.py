from tkinter import *
from tkinter import messagebox


def accion(title,msg):
    MsgBox = messagebox.askquestion (title,msg,icon = 'warning')
    if MsgBox == 'yes':
       master.quit()
       #Desplegar mensaje en pantalla
       #root.destroy()
    #else:
        #messagebox.showinfo('Return','You will now return to the application screen')
     #   print("chao")


master = Tk()
A=master.winfo_screenwidth()
B=master.winfo_screenheight()
#master.geometry("{0}x{1}+0+0".format(A,B))
master.attributes('-fullscreen', True)
#ma=0.5*A #margen en eje X
#mb=0.2*B #margen en eje Y
#a=0.25*A   #variacion x
#b=0.3*B   #variacion y
master.configure(background='white')
image1a = PhotoImage(file="boton1a.png")
image1b = PhotoImage(file="boton1b.png")
image1c = PhotoImage(file="boton1c.png")

image2a = PhotoImage(file="boton2a.png")
image2b = PhotoImage(file="boton2b.png")
image2c = PhotoImage(file="boton2c.png")

title1="TORMENTA DE VIENTO"
title2="TORMENTA ELÉCTRICA"
msgini="¿Está seguro que quiere mostrar el siguiente mensaje en las pantallas: '"
msgfin="'?"
msg1a="USO OBLIGATORIO DE BARBIQUEJO PROTECCION VISUAL HERMETICA"
msg1b="PERMITIDO CIRCULAR SOLO PERSONAL AUTORIZADO    (GERENTES,SUPERINTENDENTES,JEFES GENERALES,JEFES DE TURNO,PROTECCION INDUSTRIAL,GERENCIA SSO,VEHICULOS DE EMERGENCIA Y LOS AUTORIZADOS POR EL COMITÉ DE EMERGENCIA)"
msg1c="PROHIBICION DE CIRCULAR PEATONES Y VEHICULOS(TODOS REFUGIADOS) SOLO AUTORIZADOS VEHICULOS DE EMERGENCIA (AMBULANCIA,CARRO BOMBA,CARRO RESCATE,ENC EMERGENCIA,GERENCIA DE SEGURIDAD,PROTECCION INDUSTRIAL,EMERGENCIA OPERACIONAL,AUTORIZADO POR EL COMITE DE EMERGENCIA)"

msg2a="PERSONAL EN ESTADO DE ALERTA  PROHIBICION DE INGRESO DE VISITAS Y PROVEEDORES"
msg2b="RESTRICCION DE LA CIRCULACION DE PEATONES           PERMITIDO CIRCULAR SOLO VEHICULOS AUTORIZADOS (GERENTES,SUPERINTENDENTES,JEFES GENERALES,JEFES DE TURNO,PROTECCION INDUSTRIAL,GERENCIA SSO,VEHICULOS DE EMERGENCIA Y LOS AUTORIZADOS POR EL COMITÉ DE EMERGENCIA)"
msg2c="PROHIBICION ABSOLUTA DE CIRCULAR PEATONES Y VEHICULOS(TODOS REFUGIADOS) SOLO AUTORIZADOS VEHICULOS DE EMERGENCIA (AMBULANCIA,CARRO BOMBA,CARRO RESCATE,ENC EMERGENCIA,GERENCIA DE SEGURIDAD,PROTECCION INDUSTRIAL,EMERGENCIA OPERACIONAL,AUTORIZADO POR EL COMITE DE EMERGENCIA)"


labelfont= ('arial', 24, 'bold')


l1=Label(master, text="ALERTA DE TORMENTA DE VIENTO",bg="white",font=labelfont).place(relx=0.5,rely=0.1,anchor=CENTER)
boton1a = Button(master,	bg="white",	bd=0,	image=image1a,	command=lambda:accion(title1,msgini+msg1a+msgfin)).place(relx=0.17, rely=0.3, anchor=CENTER)
boton1b = Button(master,	bg="white",	bd=0,	image=image1b,	command=lambda: accion(title1,msgini+msg1b+msgfin)).place(relx=0.5, rely=0.3, anchor=CENTER)
boton1c = Button(master,	bg="white",	bd=0,	image=image1c ,	command=lambda:accion(title1,msgini+msg1c+msgfin)).place(relx=0.83, rely=0.3, anchor=CENTER)



l2=Label(master,	text="ALERTA DE TORMENTA ELÉCTRICA",	bg="white",	font=labelfont).place(relx=0.5,rely=0.5,anchor=CENTER)
boton2a = Button(master,	image=image2a,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2a+msgfin)).place(relx=0.17, rely=0.7, anchor=CENTER)
boton2b = Button(master,	image=image2b,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2b+msgfin)).place(relx=0.5, rely=0.7, anchor=CENTER)
boton2c = Button(master,	image=image2c,	bg="white",	bd=0,	command=lambda:accion(title2,msgini+msg2c+msgfin)).place(relx=0.83, rely=0.7, anchor=CENTER)


master.mainloop()