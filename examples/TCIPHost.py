import socket as socket


TCP_IP = '172.30.254.65'

TCP_PORT = 22

BUFFER_SIZE = 1024  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


s.bind((TCP_IP, TCP_PORT))


s.listen(1)


conn, addr = s.accept()

print('Connection address:', addr)

while True:

    data = input("komenda: ")

    if data == "non":
        conn.send("non".encode("utf8"))
        break

    conn.send(data.encode("utf8"))  # echo

conn.close()