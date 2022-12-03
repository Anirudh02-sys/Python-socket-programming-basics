import socket

HOST = "127.0.0.1"
PORT = 9000

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as s:
    s.bind((HOST,PORT))
    s.listen()
    conn,addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if data.decode() == "quit":
                print("Connection terminated")
                break
            elif not data:
                break
            print(f"CLIENT : {data.decode()}")
            print("---Your turn to type---")
            msg = input()
            conn.send(msg.encode())
            
            
        

