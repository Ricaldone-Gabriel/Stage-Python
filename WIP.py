from pathlib import Path
import time
import os
import plotly.graph_objects as go
import pandas
from socketIO_client import SocketIO, LoggingNamespace #Non mi funziona sul mio pc RAAAH
import socket


#
#  ---------       ----------
#  |  Web  | <---- | Python | <---- Term
#  | Server| ----> | Server | <---- Term
#  ---------       ----------
#
#  Il server python raccoglie dati dai termometri, quando il web server richiede dei plot nuovi il server python risponde.

# Crea un socket server per i termometri

async def main():
    return


"""
dir_path = os.path.dirname(os.path.realpath(__file__))
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Indirizzo IP del server
port = 8081       # Porta su cui il server ascolta

server_socket.settimeout(1) #Dopo N secondi, crea un errore di timeout
arrayDatiRicevuti = []

try:
    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"In attesa di connessioni su {host}:{port}")
    conn, addr = server_socket.accept()

    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Ricevuto: {data}")
        arrayDatiRicevuti.append(data)

except socket.timeout:
    print(f"Tempo scaduto")
    try:
        f = open(dir_path + "/Data/" + 'Data.txt', "r")	
        fileLetto = f.readlines()
        leggi = True
        for line in fileLetto:
            if leggi:
                arrayDatiRicevuti.append(line)
                leggi = False
            else:
                leggi = True
    except FileNotFoundError:
        print("File non trovato")
        exit()

     


arrayTempo = []
arrayTemperatura = []
arrayUmidita = []
datiSingoli = []


for dato in arrayDatiRicevuti:
    datiSingoli = dato.split("\t")
    datiSingoli[1] = datiSingoli[1].strip()
    
    arrayTempo.append(datiSingoli[0])
    arrayTemperatura.append(datiSingoli[1].split(",")[1])
    arrayUmidita.append(datiSingoli[1].split(",")[2])

fig = go.Figure()

figTemp = go.Figure()
figHum = go.Figure()

figTemp.add_trace(go.Scatter(x=arrayTempo, y=arrayTemperatura, mode="lines",name="Temperatura"))
figHum.add_trace(go.Scatter(x=arrayTempo, y=arrayUmidita, mode="lines",name="Umidità"))

fig.add_trace(go.Scatter(x=arrayTempo, y=arrayUmidita, mode="lines",name="Umidità"))
fig.add_trace(go.Scatter(x=arrayTempo, y=arrayTemperatura, mode="lines",name="Temperatura"))

figTemp.update_traces(
    line = dict(color='red'),
)
figHum.update_traces(
    line = dict(color='blue'),
)

fig.update_traces(line=dict(color='red'), selector=dict(name='Temperatura'))
fig.update_traces(line=dict(color='blue'), selector=dict(name='Umidità'))

figTemp.update_layout(
    xaxis_title = "Tempo",
    yaxis_title = "Valori Raccolti"
)
figHum.update_layout(
    xaxis_title = "Tempo",
    yaxis_title = "Valori Raccolti"
)

fig.update_layout(
    xaxis_title = "Tempo",
    yaxis_title = "Valori Raccolti"
)

print(Path.cwd() / time.strftime("%Y-%m-%d", time.gmtime())/'.txt')

nomeFile = arrayTempo[0].split(" ")[0] + '.png'

#fig.write_html(dir_path + "/Plots/" + nomeFile) Non funza
fig.write_image(dir_path + "/views/Plots/" + nomeFile) #Necessita kaleido
figHum.write_image(dir_path + "/views/Plots/Hum/" + nomeFile)
figTemp.write_image(dir_path + "/views/Plots/Temp/" + nomeFile)

fig.write_image(dir_path + "/views/Plots/recente.png") #Necessita kaleido
figHum.write_image(dir_path + "/views/Plots/Hum/recente.png")
figTemp.write_image(dir_path + "/views/Plots/Temp/recente.png")
"""