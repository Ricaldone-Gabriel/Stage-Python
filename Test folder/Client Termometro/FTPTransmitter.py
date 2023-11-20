import socket
IP = "127.0.0.1"
PORT = 8080
ADDR = (IP, PORT)
FORMAT = "utf-8"
SIZE = 1024

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    while True:
        message = client.recv(1024).decode()
        response = "Start"
        if(message == "Prepare"):
            file = open("Data/Recent.txt", "r")
            data = file.read()
            client.send(response.encode())
            message = client.recv(1024).decode()
            if(message == "Request"):
                response = "Recent"
                client.send(response.encode())
                if(message == "Request"):
                    response = "Recent"
                    client.send(data.encode())
                    message = client.recv(1024).decode()
                    if(message == "Finish"):
                        file.close()


if __name__ == "__main__":
    main() 
