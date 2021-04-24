import socket, random
from threading import Thread
from time import sleep

class serverudp:

    def __init__(self,ip='localhost',porta=3000):
        self.addr = (ip,porta)
        self.connectionUdp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        #faz a conexão
        self.connectionUdp.bind(self.addr)

        print('Servidor iniciado')

        # flag indica se a partida já começou
        self.flag_startMatch = False
        
        #quantos jogadores estão conectados e o código para identificação
        self.codplayer=[]

        #Thread(target=self.receive(),args=()).start()

        # lendo as mensagens
        while True:
            """('qualquer coisa',('127.0.0.1',65000)) """

            self.client = self.connectionUdp.recvfrom(2048)
            self.message = self.client[0].decode()
            self.address_client = self.client[1]
            print (f'Cliente {self.address_client}, Mandou: {self.message}')
        
            if self.message.lower() == 'play' and self.address_client[1] not in self.codplayer and len(self.codplayer) <=4:
                self.codplayer.append((self.address_client[1])) 
                # print(f'O jogador {self.address_client[1]} entrou na sala')
                # print(f'tamanho da lista de jogadores {len(self.codplayer)}')
                if len(self.codplayer) == 1:
                    self.message_check = 'Voce entrou na sala. Aguarde pelo menos um jogador'
                    self.connectionUdp.sendto(self.message_check.encode(), self.address_client)
                
                elif len(self.codplayer) == 2:
                    Thread(target=self.timer,args=()).start()
                    self.message_check = 'Voce entrou na sala. Em instantes a partida irá começar...'
                    self.connectionUdp.sendto(self.message_check.encode(), self.address_client)

                else:    
                    self.message_check = 'Voce entrou na sala. Em instantes a partida irá começar...'
                    self.connectionUdp.sendto(self.message_check.encode(), self.address_client)
            
                
            elif self.address_client[1] in self.codplayer:
                self.message_error = 'Voce ja esta na sala'.encode()
                self.connectionUdp.sendto(self.message_error, self.address_client)

            
            #ajeitar o flag da partida iniciada
            elif self.message.lower() == 'play' and len(self.codplayer) >= 5 or self.flag_startMatch == True:
                self.message_error = 'A sala já está cheia ou a partida já começou. Aguarde...'.encode()
                self.connectionUdp.sendto(self.message_error, self.address_client)


            elif self.message.lower() == '001' and self.address_client[1] in self.codplayer:
                print('chegou aqui')
                self.codplayer.remove(self.address_client[1])
                self.message_error = '101'.encode()
                self.connectionUdp.sendto(self.message_error, self.address_client)
                print(f'menos 1 agora {len(self.codplayer)}')


            else:
                self.msg = f'Sua mensagem foi: {self.message} '
                self.connectionUdp.sendto(self.msg.encode(),self.address_client)

    


    def timerGame(self):
        #timer para tempo de resposta
        sleep(10)

    def timer(self):
        # timer de espera para começar o jogo
        print('iniciamos')
        sleep(5)
        self.startGame()
        
    def startGame(self):
        self.flag_startMatch = True
        print('começamos...')
        self.trivia = self.questionGame()
        
        self.message = f'Rodada 1 \n\n {self.trivia[0][1]}'.encode()
        for x in self.codplayer:
            self.connectionUdp.sendto(self.message,('localhost',x))
        #if rec


    #def check_reposta(self,)
    #def placar(self,)
        
    def selectSequence(self):
        # retorna qual será a sequencia das perguntas
        return [random.randrange(0,2) for x in range(0,5)]
        #[0,1,0,1,0]

    def selectQuestion (self):

        # abre o arquivo e pega as linhas
        self.arq = open('question.txt', 'r')
        self.allask = self.arq.readlines()
        self.arq.close()

        # vetores para armaenzar os indíces e perguntas
        self.indicador = []
        self.perguntas = []

        # faz o sorteio aleatório do numeros de quais perguntas serão selecionadas
        while len(self.indicador) != 5:
            self.number = random.randrange(0,27)
            if self.number not in self.indicador:
                self.indicador.append(self.number)

        #adiciona as perguntas em relaçãos aos números 
        for x in self.indicador:
            self.perguntas.append(self.allask[x])

        # transformas as strings em tuplas
        for i in range(0,5):
            self.broken=self.perguntas[i].split(',')
            self.a = self.broken[0][2:-1]
            self.b = self.broken[1][2:-3]
            self.junto = (self.a,self.b)
            self.perguntas.append(self.junto)

        #retira as strings
        for x in range(0,5):
            self.perguntas.pop(0)

        #retorna a lista com as tuplas de respostas
        return self.perguntas

    def questionGame(self):
        self.respostas = self.selectQuestion()
        self.sequencia = self.selectSequence()
        self.gabarito =[]
        self.questionario =[]

        for x in range(0,5):
            if self.sequencia[x] == 0:
                self.pergunta = f'Qual a capital do estado {self.respostas[x][0]}: ______________ ?'
                self.questionario.append(self.pergunta)
                self.gabarito.append(self.respostas[x][1])
            else:
                self.pergunta = f'Qual a estado tem a capital {self.respostas[x][1]}: ______________ ?'
                self.questionario.append(self.pergunta)
                self.gabarito.append(self.respostas[x][0])

        return [self.questionario,self.gabarito]
        # retorno da função acima 
        """[['Qual a capital do estado Sergipe: ______________ ?', 
        'Qual a estado tem a capital Rio de Janeiro: ______________ ?', 
        'Qual a estado tem a capital Belém: ______________ ?', 
        'Qual a capital do estado Rondônia: ______________ ?', 
        'Qual a capital do estado Amapá: ______________ ?'], 
        ['Aracaju', 'Rio de Janeiro', 'Pará', 'Porto Velho', 'Macapá']]"""









    def receive(self):
        while True:
            self.received = self.connectionUdp.recvfrom(1024)
            self.message_received =self.received[0].decode()


serverudp()