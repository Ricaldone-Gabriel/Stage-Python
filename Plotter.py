from pathlib import Path
import time
import plotly

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


while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print(f"Ricevuto: {data}")