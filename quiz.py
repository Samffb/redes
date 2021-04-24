import random

class Quiz:
    def selectSequence(self):
        # retorna qual será a sequencia das perguntas
        return [random.randrange(0,2) for x in range(0,5)]

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

    def questions(self):
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

