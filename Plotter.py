from pathlib import Path
import time
import plotly.graph_objects as go
import pandas
import socket

# Crea un socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'  # Indirizzo IP del server
port = 8081       # Porta su cui il server ascolta

server_socket.bind((host, port))
server_socket.listen(1)  # Il server accetta una connessione alla volta

print(f"In attesa di connessioni su {host}:{port}")
conn, addr = server_socket.accept()
print(f"Connesso a {addr}")
arrayDatiRicevuti = []
arrayTempo = []
arrayTemperatura = []
arrayUmidita = []
datiSingoli = []

while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Ricevuto: {data}")
    arrayDatiRicevuti.append(data)

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
fig.show()
