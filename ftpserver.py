import socket

HOST = "127.0.0.1"
PORT = 64000
ADDR = (HOST,PORT)
FORMAT ="utf-8"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as server:
    server.bind(ADDR)
    server.listen()
    print("[SERVER] LISTENING")
    conn,addr = server.accept()
    with conn:
        print(f"CONNECTED BY {addr}")
        filename = conn.recv(1024).decode()
        print(f"filename : {filename} recived")
        file = open("server-data/"+filename,"w")
        data = conn.recv(1024).decode()
        print("File data recived")
        file.write(data)
        file.close()
