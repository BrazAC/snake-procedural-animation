import pygame

def drawCircle(screen, position, radius, width):
    pygame.draw.circle(screen, "white", position, radius, width) 


def main():
    #Pygame setup
    pygame.init()

    #Screen setup
    screenInfo = pygame.display.Info()
    screen = pygame.display.set_mode((screenInfo.current_w - 10, screenInfo.current_h - 50))
    pygame.display.set_caption("Procedural Animation")

    #Clock setup
    clock = pygame.time.Clock()
    fps = 60
    running = True

    


    #Setting some variables
    xPosition = screenInfo.current_w // 2
    yPosition = screenInfo.current_h // 2
    animalSpeed = 1.5

    xMouse = 0
    yMouse = 0

    while running:
        screen.fill("black")
        clock.tick(fps)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        #Obter posicao onde clicou
                        xMouse, yMouse = pygame.mouse.get_pos()
                        #Desenhar circulo onde clicou
                        drawCircle(screen, (xMouse, yMouse), 5, 0)
                        
                        
        #Update positions
        """xPosition = xMouse
        yPosition = yMouse"""
        
        #Drawing circle
        drawCircle(screen, (xPosition, yPosition), 75, 5)
        pygame.display.flip()
        

pygame.quit()

if __name__ == "__main__":
    main()