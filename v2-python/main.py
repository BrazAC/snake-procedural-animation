import pygame
from app import Body
from app import BodyPart

def main():
    # Inicializa o Pygame
    pygame.init()

    # Configuração da tela
    LARGURA, ALTURA = 800, 600
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("Procedural Animal")

    # Cores
    white = (255, 255, 255)
    black = (0, 0, 0)

    clock = pygame.time.Clock()
    FPS = False

    # Inicializa corpo
    body = Body()
    body.initBody()
    canDraw = False
    canUpdate = False
    rodando = True
    mouse = [0, 0]

    while rodando:
        screen.fill("black")
        clock.tick(FPS)  

        for evento in pygame.event.get():
            #Keyboard
            if evento.type == pygame.QUIT:  
                rodando = False
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_ESCAPE:  
                rodando = False 
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_a:  
                canDraw = not canDraw
            #Mouse
            """if evento.type == pygame.MOUSEBUTTONDOWN:
                canUpdate = True
            if evento.type == pygame.MOUSEBUTTONUP:
                canUpdate = False"""

        if canDraw:
            body.drawBody(screen)

        """if canUpdate: 
            mouse[0], mouse[1] = pygame.mouse.get_pos()
            body.updateBody(mouse)"""
        mouse[0], mouse[1] = pygame.mouse.get_pos()
        body.updateBody(mouse)
    
        pygame.display.flip()

    pygame.quit()




if __name__ == "__main__":
    main()