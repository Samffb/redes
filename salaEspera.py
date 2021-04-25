from quiz import *
from newserver import *


class Room:

    def __init__(self,server,timerResponse,maxPlayer,timerStart):
        self.lista_jogadores=[]
        self.server = server
        self.timerResponse = timerResponse
        self.timerStart = timerStart
        self.maxPlayer = maxPlayer
        self.quiz = None
        self.listResponse ={} 

        #self.placar = { k: 0 for k in self.lista_jogadores }

    def timerResponse(self):
        sleep(self.timerResponse)

    def timerStart(self):
        sleep(self.timerStart)

    def startQuiz(self):
        self.quiz = Quiz()
        self.questions = self.quiz.questions()

        


        

    def getRanking(self,dic):
        pass

    def placar(self):
        pass       

