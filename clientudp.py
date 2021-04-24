import socket, sys
from threading import Thread

class clientudp:

    def __init__(self,ip='localhost',porta=3000):
        self.addr = (ip,porta)
        self.connection = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        #interação com o servidor
        print ('Para encerrar Presssione "exit" e em seguida "Enter"')
        self.msg = input()

        #Thread(target=self.receive,args=()).start()
        #Thread(target=self.receive,args=()).start()
        flag = True
        while flag:

            self.connection.sendto(self.msg.encode(),self.addr)
            self.msg = input('Digite sua mensagem: ')
            self.resposta = self.connection.recvfrom(1024)

            print(f'\nResposta do servidor: {self.resposta[0].decode()}')


            if self.msg == '\x18':
                print ('voce saiu da sala')
                flag = False
                #self.cancel = '001'.encode()
                #self.connection.sendto(self.cancel,self.addr)
                #print('Voce saiu da sala')
        
            # self.connection.close()

    def receive(self):
        while True:
            self.received = self.connection.recvfrom(1024)
            print(f'Server: {self.received[0].decode()}')

    
clientudp()