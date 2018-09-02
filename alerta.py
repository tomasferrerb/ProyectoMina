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
	image1a = PhotoImage(file="boton1a.png")
	image1b = PhotoImage(file="boton1b.png")
	image1c = PhotoImage(file="boton1c.png")

	image2a = PhotoImage(file="boton2a.png")
	image2b = PhotoImage(file="boton2b.png")
	image2c = PhotoImage(file="boton2c.png")



	labelfont= ('arial', 24, 'bold')


	l1=Label(master, text="ALERTA DE TORMENTA DE VIENTO",bg="white",font=labelfont).place(relx=0.5,rely=0.1,anchor=CENTER)
	boton1a = Button(master,bg="white",bd=0,image=image1a,command=master.quit).place(relx=0.17, rely=0.3, anchor=CENTER)
	boton1b = Button(master,bg="white",bd=0,image=image1b,command=accion).place(relx=0.5, rely=0.3, anchor=CENTER)
	boton1c = Button(master,bg="white",bd=0,image=image1c ).place(relx=0.83, rely=0.3, anchor=CENTER)



	l2=Label(master,text="ALERTA DE TORMENTA ELÉCTRICA",bg="white",font=labelfont).place(relx=0.5,rely=0.5,anchor=CENTER)
	boton2a = Button(master,image=image2a,bg="white",bd=0,command=master.quit).place(relx=0.17, rely=0.7, anchor=CENTER)
	boton2b = Button(master, image=image2b, bg="white",bd=0,command=accion).place(relx=0.5, rely=0.7, anchor=CENTER)
	boton2c = Button(master,image=image2c,bg="white",bd=0).place(relx=0.83, rely=0.7, anchor=CENTER)


	master.mainloop()

if __name__ == "__main__":
    main()

 
