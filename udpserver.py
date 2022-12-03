import socket

HOST = "127.0.0.1"
PORT = 20001

with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as u:
    u.bind((HOST,PORT))
    print("CONNECTION ESTABLISHED WITH CLIENT\n")
    while True:
        data = u.recvfrom(1024) # data[0] is msg , data[1] is addr of sender
        if data[0].decode() == "quit":
            print("CONNECTION TERMINATED")
            break
        if not data[0]:
            break
        print(f"CLIENT : {data[0].decode()} ")
        print("Your turn to type :")
        msg = input()
        u.sendto(msg.encode(),data[1])
        if msg == "quit":
            break