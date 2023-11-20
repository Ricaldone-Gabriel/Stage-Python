#Acquisizione dati da sensore AOSONG AM2302 tramite Arduino nano
#Ambiente LINUX
#Una misura al minuto di Temperatura e Umidità relativa
#Elio Bertacco INRIM 2023

import time
import serial
import os
from pathlib import Path
from serial.tools.list_ports import comports

# Crea un socket client
dir_path = os.path.dirname(os.path.realpath(__file__))

ports = list(comports()) # Trova tutte le porte seriali disponibili
print(ports)
if ports:
    # Se sono disponibili porte seriali, seleziona la prima porta trovata
    porta = ports[1].device #Non funziona sempre, trovare un modo per identificare il dispositivo.
    print(f"Connesso alla porta: {porta}")
    ser1 = serial.Serial(	        #configuro UART1
        port=porta,	        #modificare ttyS1 con nome porta seriale utilizzata
        baudrate =9600,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=10
    )
    ser1.flush()      #Pulizia del buffer della porta seriale (USB) di Arduino
    time.sleep(2)     #Attesa necessaria per permettere ad Arduino di completare le operazioni di setup
    while 1:
        try:
            ser1.write(b'MEAS?') #Chiedi all'arduino i dati relativi Temp e Umid.
            time.sleep(20)
            print(ser1.readline().decode('utf-8'))
            time.sleep(2)  #Attesa di 10 s. 1 s è circa il tempo di lettura del sensore
        except KeyboardInterrupt:
            print("ho finito")
            exit()
    else:
        print("Nessuna porta seriale disponibile")

