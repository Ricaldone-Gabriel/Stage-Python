#Acquisizione dati da sensore AOSONG AM2302 tramite Arduino nano
#Ambiente LINUX
#Una misura al minuto di Temperatura e Umidità relativa
#Elio Bertacco INRIM 2023

import time
import serial
from pathlib import Path
from serial.tools.list_ports import comports
import socket

# Crea un socket client
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Indirizzo IP del server
port = 8081       # Porta a cui il client si connette

while client_socket.connect_ex((host,port)) != 0:
    try:
        time.sleep(2)
    except KeyboardInterrupt:
        exit()
# Trova tutte le porte seriali disponibili
ports = list(comports())

if ports:
    # Se sono disponibili porte seriali, seleziona la prima porta trovata
    porta = ports[0].device
    print(f"Connesso alla porta: {porta}")
    ser1 = serial.Serial(	        #configuro UART1
        port=porta,	        #modificare ttyS1 con nome porta seriale utilizzata
        baudrate =9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=5
    )
    ser1.flush()      #Pulizia del buffer della porta seriale (USB) di Arduino
    time.sleep(2)     #Attesa necessaria per permettere ad Arduino di completare le operazioni di setup
    while 1:
        try:
            ser1.write(b'MEAS?') #Chiedi all'arduino i dati relativi Temp e Umid.
            time.sleep(0.1)
            x1=ser1.readline().decode('utf-8')	#leggo UART1
            date = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())	#legge data e ora (cambiare ordine dei valori se serve)
            f = open(Path.cwd() / 'Data.txt', "a+")	
            f.write(date + "\t" + x1)	#timestamp + TAB + temp/hum + return carrier
            f.close()
            print(date + "\t" + x1)
            message = date + "\t" + x1
            client_socket.send(message.encode())
            time.sleep(2)  #Attesa di 10 s. 1 s è circa il tempo di lettura del sensore
        except KeyboardInterrupt:
            f.close()
            ser1.close()
            print("ho finito")
    else:
        print("Nessuna porta seriale disponibile")

