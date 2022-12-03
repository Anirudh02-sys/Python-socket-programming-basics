import socket

HOST = "127.0.0.1"
PORT = 20001

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as u:
    print("START CHAT")
    while True:
        msg = input()
        if msg == "quit":
            break
        u.sendto(msg.encode(),(HOST,PORT))
        data = u.recvfrom(1024)#data[0] is msg , data[1] is addr of sender
        if data[0].decode() == "quit":
            break
        print(f"SERVER : {data[0].decode()}")

