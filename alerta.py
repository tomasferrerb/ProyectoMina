from tkinter import *
from tkinter import messagebox


def accion():
   msg = messagebox.showinfo( "Hola", "seré weon?")


def main():
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
	image11 = PhotoImage(file="boton11.png")
	image12 = PhotoImage(file="boton12.png")
	image13 = PhotoImage(file="boton13.png")

	scale_w = 1
	scale_h = 1
	image11.zoom(scale_w, scale_h)
	image12.zoom(scale_w, scale_h)
	image13.zoom(scale_w, scale_h)

	l1=Label(master, text="ALERTA DE TORMENTA DE VIENTO",bg="white").place(relx=0.5,rely=0.1,anchor=CENTER)
	boton11 = Button(master, text="Alerta de Tormenta de Viento",image=image11,bg="white",command=master.quit).place(relx=0.17, rely=0.3, anchor=CENTER)
	boton12 = Button(master, text="Alerta de Tormenta Eléctrica",bg="white",image=image12,command=accion).place(relx=0.5, rely=0.3, anchor=CENTER)
	boton13 = Button(master, text="Alerta de Tormenta Eléctrica2",bg="white",image=image13 ).place(relx=0.83, rely=0.3, anchor=CENTER)



	l2=Label(master,text="ALERTA DE TORMENTA ELÉCTRICA").place(relx=0.5,rely=0.5,anchor=CENTER)
	boton21 = Button(master, text="Alerta de Tormenta de Viento",image=image11,bg="white",bd=0,command=master.quit).place(relx=0.3, rely=0.7, anchor=CENTER)
	boton22 = Button(master, text="Alerta de Tormenta Eléctrica", command=accion).place(relx=0.5, rely=0.7, anchor=CENTER)
	boton23 = Button(master, text="Alerta de Tormenta Eléctrica2",bg="white").place(relx=0.7, rely=0.7, anchor=CENTER)


	master.mainloop()

if __name__ == "__main__":
    main()

 
