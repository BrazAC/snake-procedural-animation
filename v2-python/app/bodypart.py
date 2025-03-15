import pygame
import math

class BodyPart:
    def __init__(self,x,y,radius,angle):
        self.x = x
        self.y = y
        self.radius = radius
        self.angle = angle
    
    def drawBodyPart(self, surface):
        #Desenhar circunferencia
        pygame.draw.circle(surface, "white", (self.x, self.y), self.radius)

        #Desenhar segmento guia
        #pygame.draw.line(surface, "red", (self.x, self.y), (self.x - self.radius, self.y), 2)
    
    def updateBodyPart(self, next):
        #Coordenadas
        x1, y1 = next.x, next.y
        x2, y2 = self.x, self.y
        #Distancia
        distanceNext = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        #Angulo
        angleRadians = math.atan2((y2 - y1) , (x2 - x1))
        #Mover centro
        if distanceNext > self.radius:
            deltaDisplacement = distanceNext - self.radius
            self.x -= deltaDisplacement * math.cos(angleRadians)
            self.y -= deltaDisplacement * math.sin(angleRadians)


        