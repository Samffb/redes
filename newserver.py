from threading import Thread
import socket


class ServerUDP:
    def __init__(self,ip='localhost',porta=3000):
        self.addr = (ip,porta)
        self.connection_udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.connection_udp.bind(self.addr)

        Thread(target=self.received, args=()).start()
        Thread(target=self.send, args=()).start()


    def send(self,data, addr):
        self.connection_udp(data.encode(),addr)


    def received(self):
        while True:
            dados = self.connection_udp.recv(2048)
            print(f'O cliente mandou: {dados[0].decode()}')

ServerUDP()