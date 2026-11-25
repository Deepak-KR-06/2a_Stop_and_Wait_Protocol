import socket

s = socket.socket()
s.connect(('localhost', 8000))

while True:
    data = s.recv(1024).decode()

    if not data:
        break

    if data.lower() == "exit":
        print("Server disconnected")
        break

    print("Received data:", data)

    ack = "ACK: Data received"
    s.send(ack.encode())

s.close()