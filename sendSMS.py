
import serial
import os, time, sys
import datetime
import argparse





##ser.write('AT'+'\r\n')
##time.sleep(10)



def SendMessage(number, txt):
  SERIAL_PORT = "/dev/ttyS0"    # Rasp 3 UART Port
  ser = serial.Serial(SERIAL_PORT, baudrate = 9600, timeout = 5)
  time.sleep(8)
  
  ser.write('AT+CMGF=1'+'\r\n') # set to text mode
  time.sleep(1)


  ser.write('AT+CMGDA="DEL ALL"\r\n') # delete all SMS
  time.sleep(1)


  ser.write('AT+CMGS= " ' + number + '"\r\n') #Mobile phone number to send message
  time.sleep(1)
  reply2 = ser.read(ser.inWaiting())
  print(reply2)


  ser.write(txt+'\r\n');
  time.sleep(.500)
  

  ser.write(str(unichr(26))+'\r\n')
  #ser.write((char)26)  #ASCII code of CTRL+Z
  # revisar este link https://bytes.com/topic/python/answers/696448-how-write-ctrl-z-serial-port

  time.sleep(1)
  





if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='code to send a SMS',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--number', type=str,help='number +569...')
    parser.add_argument('--txt',type=str,help='texto in the SMS') 


    args = parser.parse_args()

    try:
        SendMessage(args.number,args.txt)
    except KeyboardInterrupt:
        pass




