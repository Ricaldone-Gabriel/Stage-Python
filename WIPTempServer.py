import socketio
import socket
import asyncio
from pathlib import Path
import time
import os
import plotly.graph_objects as go
import pandas
dir_path = os.path.dirname(os.path.realpath(__file__))
#Necessita: websocket-client, python-socketio, aiohttp==3.9.0b1, C++ 14.0 (Minimo)

#               Server termometri
# Ancora da sviluppare, necessita: Termometro! (E anche più di uno possibilmente)
#
#
async def serverTermometri():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '127.0.0.1'  # Indirizzo IP del server
    port = 8081       # Porta su cui il server ascolta
    server_socket.settimeout(10) #Dopo N secondi, crea un errore di timeout

    arrayDatiRicevuti = []

    server_socket.bind((host, port))
    server_socket.listen(1)

    print(f"In attesa di connessioni su {host}:{port}")
    conn, addr = server_socket.accept()
    while True:
        async with open(dir_path + "/Data/" + "Data.txt", "a") as file:
            data = conn.recv(1024).decode()
            #if not data:
            #    break
            print(f"Ricevuto: {data}")
            file.write(data)

#               Crea Plot
# Legge il file data e crea un plot 👍
#

async def creaPlot():
    file = open(dir_path + "/Data/" + "data.txt", "r")
    
    lines = file.readlines()
    arrayTempo = []
    arrayTemperatura = []
    arrayUmidita = []
    datiSingoli = []

    for line in lines:
        if line != "\n":
            datiSingoli = line.split("\t")  
            datiSingoli[1] = datiSingoli[1].strip()
            arrayTempo.append(datiSingoli[0])
            arrayTemperatura.append(datiSingoli[1].split(",")[1])
            arrayUmidita.append(datiSingoli[1].split(",")[2])

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=arrayTempo, y=arrayUmidita, mode="lines",name="Umidità"))
    fig.add_trace(go.Scatter(x=arrayTempo, y=arrayTemperatura, mode="lines",name="Temperatura"))
    fig.update_layout(
        xaxis_title = "Tempo",
        yaxis_title = "Valori Raccolti"
    )
    """
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
#               Main
# Creo un socket per comunicare col server NodeJs, questo programma qua è un client relativo a nodejs.
# Il server plotter rimane in ascolto per richieste del server nodejs, in caso arrivasse una richiesa crea un plot.

async def main():
    sio = socketio.AsyncClient()
    print("Test")
    @sio.event
    async def connect():
        print('Connected')

    @sio.event
    async def disconnect():
        print('Disconnected')

    @sio.event
    async def message(data):
        print("Richiesta")
        await creaPlot()

    #serverTermometro = asyncio.create_task(serverTermometri())
    await sio.connect('http://localhost:8080', transports=["websocket"])
    await sio.wait()
    #await serverTermometro

if __name__ == '__main__':
    asyncio.run(main())

#
#  ---------       ----------
#  |  Web  | <---- | Python | <---- Term
#  | Server| ----> | Server | <---- Term
#  ---------       ----------
#
#  Il server python raccoglie dati dai termometri, quando il web server richiede dei plot nuovi il server python risponde.

# Crea un socket server per i termometri
