"""
This code strictly follows the pseudocode from topic three of the paper:
'FABRIK: A fast, iterative solver for the Inverse Kinematics problem.
"""

import pygame
import math

#Init joints and segments
#joints
jointAm = 0
#segments
totalD = 0
#target
t = [] 
#tolerance
tol = 0


def designThings(screen, p):
    for i in range(0, jointAm, 1):
        pygame.draw.circle(screen, "white", (p[i][0], p[i][1]), 10)
        
        if i < (jointAm - 1):
            pygame.draw.line(screen, "white", (p[i][0], p[i][1]), (p[i+1][0], p[i+1][1]), 10)

def fabrik(p, d):
    global jointAm, totalD, t, tol

    dist = math.dist(t, p[0])
    print(dist, totalD, dist > totalD)
    if dist > totalD:
        for i in range(0, jointAm - 1, 1):
            r = math.dist(p[i], t)
            k = d[i] / r
            p[i+1][0] = (1-k)*p[i][0] + k*t[0]
            p[i+1][1] = (1-k)*p[i][1] + k*t[1]
    else:
        b = p[0][:]
        diffA = math.dist(p[jointAm - 1], t)

        while diffA > tol:
            #Foward reaching
            p[jointAm - 1] = t[:]
            for i in range(jointAm - 2, -1, -1):
                r = math.dist(p[i], p[i+1])
                k = d[i] / r
                p[i][0] = (1-k)*p[i+1][0] + k*p[i][0]
                p[i][1] = (1-k)*p[i+1][1] + k*p[i][1]
            #Backward reaching
            p[0] = b[:]
            for i in range(0, jointAm - 1, 1):
                r = math.dist(p[i], p[i+1])
                k = d[i] / r
                p[i+1][0] = (1-k)*p[i][0] + k*p[i+1][0]
                p[i+1][1] = (1-k)*p[i][1] + k*p[i+1][1]
        
            diffA = math.dist(p[jointAm - 1], t)

def main():
    global jointAm, totalD, t, tol

    #Init pygame
    pygame.init()

    #Screen configs
    info = pygame.display.Info()
    WIDTH = info.current_w
    HEIGHT = info.current_h
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("F.A.B.R.I.K")

    #Pygame settings
    clock = pygame.time.Clock()
    FPS = False

    #Init joints and segments
    #joints
    p = []
    jointAm = 100
    tempDist = 0
    for i in range(0, jointAm):
        p.append([WIDTH/2, HEIGHT - tempDist])
        tempDist += 100
    jointAm = len(p)

    #segments
    d = [] 
    d = [10] * (jointAm - 1)
    totalD = sum(d)

    #target
    t = [0, 0] 
    #tolerance
    tol = 10

    #Aux vars
    running = True
    canDraw = False
    canUpdate= False

    while running:
        screen.fill("black")
        clock.tick(FPS)  

        for event in pygame.event.get():
            #Keyboard
            if event.type == pygame.QUIT:  
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:  
                running = False 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:  
                canDraw = not canDraw
            #Mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                canUpdate = True
            if event.type == pygame.MOUSEBUTTONUP:
                canUpdate = False

        #Get mouse position, update target
        t[0], t[1] = pygame.mouse.get_pos()

        #Update joints position (call FABRIK)
        #if canUpdate: 
        fabrik(p, d)

        #Design joints and segments
        #if canDraw:
        designThings(screen, p)
        
        #Update screen
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()