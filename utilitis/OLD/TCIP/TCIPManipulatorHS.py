import socket


class TCIPManipulatorHS:
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5005
    BUFFER_SIZE = 20

    def __init__(self):
        super(TCIPManipulatorHS, self).__init__()

    def __enter__(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.bind((self.TCP_IP, self.TCP_PORT))

        s.listen(1)

        self.conn, addr = s.accept()

        data = self.conn.recv(self.BUFFER_SIZE)

        print("received data:", data.decode())

        self.conn.send(data)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

    def decode(self, data):
        data = data.decode("utf-8")
        "0123,5678,abcd"
        self.goto(data[0:4], data[5:9], data[10:])

    def goto(self, x, y, z):
        pass
