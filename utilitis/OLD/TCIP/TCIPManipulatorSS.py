from manipulator.AbstractManipulator import AbstractManipulator
import socket


class TCIPManipulator(AbstractManipulator):

    TCP_IP = '172.30.254.65'
    TCP_PORT = 22
    BUFFER_SIZE = 1024

    MESSAGE = "MESSAGE"

    def __init__(self):
        super(TCIPManipulator, self).__init__()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.TCP_IP, self.TCP_PORT))

        s.send(self.MESSAGE)
        data = s.recv(self.BUFFER_SIZE)
        print(data.decode())
        s.close()

    def getCurrentPosition(self):
        pass

    def center(self, pozycja):
        pass

    def validateSpeed(self, speed):
        pass

    def goto(self, x, y, z):
        pass
