import socket

HOST = "127.0.0.1"
PORT = 64000
ADDR = (HOST,PORT)
FORMAT = "utf-8"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as client:
    client.connect(ADDR)

    file = open("data/msg.txt","r")
    data = file.read()
    client.send("msg.txt".encode())
    #Now to send data
    client.send(data.encode())
    file.close()