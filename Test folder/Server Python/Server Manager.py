import threading
import queue
import time
import socketio
import socket
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

ipNodeJS = "127.0.0.1"
hostIP = '127.0.0.1'
portJS = 8080
portSocket = 8081 
address = "http://" + ipNodeJS + ":" +  str(portJS)

QueueRichiesta = queue.Queue()
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def SlowThread():
    time.sleep(5)
    print("Finito!")
def FastThread():
    for x in range(0, 100):
        pass
    print("Fast thread Done!")
def SocketNodeJS():
    sio = socketio.Client()

    @sio.event
    def connect():
        print('Connected')

    @sio.event
    def disconnect():
        print('Disconnected')

    @sio.event
    def message(data):
        print("Richiesta")

    sio.connect(address,transports=["websocket"])
    sio.wait()

def FileTransfer(clientSocket):
    message = "Received"
    FileName = clientSocket.recv(1024).decode()
    clientSocket.send(message.encode())
    FileReceived = clientSocket.recv(1024).decode()
    clientSocket.send(message.encode())
    
    File = open(dir_path + "/Data/" + FileName + ".txt", "w")
    File.writelines(FileReceived)
    File.close()


def onNewClient(clientSocket,addr):
    message = ""
    response = ""
    while True:
        response = clientSocket.recv(1024).decode()
        
        if(response == "Send Daily"):
            message = "Confirm"
            clientSocket.send(message.encode())
            FileTransfer(clientSocket)

        if not QueueRichiesta.empty():
            if(QueueRichiesta.get() == "Request"):
                message = "Prepare"
                clientSocket.send(message.encode())
                response = clientSocket.recv(1024).decode()
                if(response == "Start"):
                    FileTransfer(clientSocket)
                
        if not response:
            break

        #Maybe some code to compute the last digit of PI, play game or anything else can go here and when you are done.

    clientSocket.close()

def Ricevitore():
    arrayDatiRicevuti = []

    serverSocket.bind((hostIP, portSocket))
    serverSocket.listen(5)
    
    print(f"In attesa di connessioni su {hostIP}:{portSocket}")

    while True:
        c, addr = serverSocket.accept()     # Establish connection with client.
        threading.thread.start_new_thread(onNewClient,(c,addr))
    serverSocket.close()


def Plotter():
    pass


def main():

    SocketNodeJS_thread = threading.Thread(target=SocketNodeJS)
    slow_thread = threading.Thread(target=SlowThread)

    slow_thread.start()
    SocketNodeJS_thread.start()

    SocketNodeJS_thread.join()
    slow_thread.join()
    # Crea due thread
    #fast_thread = threading.Thread(target=FastThread)

    # Avvia i thread
    #fast_thread.start()

    # Attendi che entrambi i thread abbiano terminato l'esecuzione
    #fast_thread.join()

    print("Main Done!")

if __name__ == "__main__":
    main()
