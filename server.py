import socket

s = socket.socket()
s.bind(('localhost', 8000))
s.listen(5)

print("Server waiting for client...")
c, addr = s.accept()

while True:
    i = input("Enter a data: ")

    if i.lower() == "exit":
        break

    c.send(i.encode())

    ack = c.recv(1024).decode()

    if ack:
        print("Acknowledgement:", ack)
    else:
        break

c.close()
s.close()