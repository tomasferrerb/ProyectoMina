Gestor de Mensajes a Pantallas led, Através de SMS y Web Server

Links referenciales:
https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/10


Configuración de puerto serial para conexión con SIM800L

Link configuración: http://www.electronicwings.com/raspberry-pi/raspberry-pi-uart-communication-using-python-and-c

Link conexiones: https://www.connectedcities.com.ph/blogs/tutorial/sim800l-and-raspberry-pi-3-b-controlled-3-led-tutorial

link envio y  recibo: http://miliohm.com/sim800l-arduino-tutorial/

link Script autostart: https://jackbarber.co.uk/blog/2017-03-02-automatically-run-a-python-script-at-boot-in-raspbian

link sleeptime: http://chamaras.blogspot.com/2013/03/how-to-deactivate-monitor-sleep-in.html


Indice de archivos:

alerta.py : Interfaz gráfica de panel touch, muestra 6 opciones de botones, al apretar uno se envía el SMS con la instrucción. 

readSMS-displayScreen.py : Espera permanentemente un SMS, al recibirlo, revisa si corresponde a una instrucción, de ser así, despliega mensaje en pantalla. 

botonXX.png: imágenes de botones para alerta.py

displayLED.py : código para desplegar mensaje en matriz led pequeña. 

displayScreen.py código para desplegar mensaje en pantalla. 

pruebaLecturaSMS.py : muestra SMS recibido. 

readSMS.py : lee SMS y ejecuta un comando

readSMSled.py : lee SMS y ejecuta displayLed.py

sendSMS.py : Envía un SMS con alguna opción de los mensajes de alerta. 


