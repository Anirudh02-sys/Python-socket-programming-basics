import socket
HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    print("START CHAT")
    while True:
        msg = input()
        s.send(msg.encode())
        data = s.recv(1024)
        if data.decode() == "quit":
            print("connection terminated")
            s.close()
            break
        print(f"SERVER : {data.decode()}")
        print("---Your turn to type---")
        

        