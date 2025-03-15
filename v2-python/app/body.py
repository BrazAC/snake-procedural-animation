from .bodypart import BodyPart
import math

class Body:
    def __init__(self):
        self.len = 40
        self.body = None
        self.head = None
        self.speed = 1
    
    def initBody(self):
        xDin,yDin = 960, 540
        radius = 35

        if self.body is None:
            self.body = []

            for i in range(self.len):
                #Criar e adicionar parte do corpo
                radiusu = radius - i * (radius/(self.len - 1))
                self.body.append(BodyPart(xDin, yDin, radiusu, 0))

                #Atualizar posicao do proximo centro
                xDin += radius

        self.head = self.body[0]
    
    def drawBody(self, surface):
        for bodypart in self.body:
            bodypart.drawBodyPart(surface)
            #print(bodypart.x)
    
    def updateBody(self, mouse):
        #MOVER A CABECA
        #Coordenadas
        x1, y1 = mouse[0], mouse[1]
        x2, y2 = self.head.x, self.head.y

        #Angulo
        angleRadians = math.atan2((y2 - y1) , (x2 - x1))
        #Tornar a curva mais atenuada
        deltaAngleRadians = angleRadians - self.head.angle
        while deltaAngleRadians < -3.14 : 
            deltaAngleRadians += 2*3.14
        while deltaAngleRadians > 3.14 : 
            deltaAngleRadians -= 2*3.14
        self.head.angle += deltaAngleRadians * 0.003

        #Mover centro da cabeca um uma certa distancia (velocidade)
        self.head.x -= self.speed * math.cos(self.head.angle)
        self.head.y -= self.speed * math.sin(self.head.angle)
        
        #MOVER OS SEGMENTOS
        for i in range(1, self.len):
            self.body[i].updateBodyPart(self.body[i - 1])


            