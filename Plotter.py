from pathlib import Path
import time
import plotly.graph_objects as go
import pandas
import socket

# Crea un socket server
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
    f = open(Path.cwd() / 'Data.txt', "r")	
    fileLetto = f.readlines()
    leggi = True
    for line in fileLetto:
        if leggi:
            arrayDatiRicevuti.append(line)
            leggi = False
        else:
            leggi = True

     


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

fig.add_trace(go.Scatter(x=arrayTempo, y=arrayUmidita, mode="lines",name="Umidità"))
fig.add_trace(go.Scatter(x=arrayTempo, y=arrayTemperatura, mode="lines",name="Temperatura"))
fig.update_layout(
    xaxis_title = "Tempo",
    yaxis_title = "Valori Raccolti"
)

print(Path.cwd() / time.strftime("%Y-%m-%d", time.gmtime())/'.txt')

nomeFile = arrayTempo[0].split(" ")[0] + '.html'

fig.write_html(Path.cwd() / nomeFile)
fig.show()
