import pygame
import math

def drawCircle(screen, position, radius, width):
    pygame.draw.circle(screen, "white", position, radius, width) 

def updateCirclePositionEquation(circlePosition, mousePosition, animalSpeed, angle):
    #Get circle center coordinates
    xCircle = circlePosition[0]
    yCircle = circlePosition[1]
    #Get mouse click coordinates
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]

    #Creating the function: y = m(x - xp) + yp
    m = angle
    xp = xMouse
    yp = yMouse
    x = xCircle
    #y = (m * (x - xp)) - yp

    #Updating the x, to input in the equation
    if xMouse > xCircle:
        x += animalSpeed
    elif xMouse < xCircle:
        x -= animalSpeed
    else:
        return xCircle

    #Get the y coordinate
    y = (m * (x - xp)) + yp

    print("Coordenadas:",x, y)
    return x, y

def updateCirclePosition(circlePosition, mousePosition, animalSpeed):
    #Get circle center coordinates
    xCircle = circlePosition[0]
    yCircle = circlePosition[1]
    #Get mouse click coordinates
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]

    if xMouse > xCircle and yMouse < yCircle:
        xCircle += animalSpeed
        yCircle -= animalSpeed
    elif xMouse < xCircle and yMouse < yCircle:
        xCircle -= animalSpeed
        yCircle -= animalSpeed
    elif xMouse < xCircle and yMouse > yCircle:
        xCircle -= animalSpeed
        yCircle += animalSpeed
    elif xMouse > xCircle and yMouse > yCircle:
        xCircle += animalSpeed
        yCircle += animalSpeed

    return xCircle, yCircle

def updateCirclePositionLERP(circlePosition, mousePosition):
    #Get circle center coordinates
    xCircle = circlePosition[0]
    yCircle = circlePosition[1]
    #Get mouse click coordinates
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]


    xCircle = 400
    yCircle = 400
    print(mousePosition)
    #Get the t value by traveled distance
    t = math.sqrt((xMouse - xCircle)**2 + (yMouse - yCircle)**2)

    #Get the new coordinates by LERP
    xCircle = xCircle + (t * (xMouse - xCircle))
    yCircle = yCircle + (t * (yMouse - yCircle))
    
    return xCircle, yCircle

def updateCirclePositionVector(circlePosition, mousePosition, animalSpeed):
    #Get circle center coordinates
    xCircle = circlePosition[0]
    yCircle = circlePosition[1]
    #Get mouse click coordinates
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]

    #Get the vector circle/mouse
    xVector = xMouse - xCircle
    yVector = yMouse - yCircle
    #Get the module of the vector
    module = math.sqrt((xVector)**2 + (yVector)**2)

    if module != 0 and module > 75:
        #Get the unitary vector
        xUnitVector = xVector / module
        yUnitVector = yVector / module
        #Multiply the unitary vector by the pace (animalSpeed)
        xCircle += xUnitVector * animalSpeed
        yCircle += yUnitVector * animalSpeed

    return xCircle, yCircle

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
    xCircle = screenInfo.current_w // 2
    yCircle = screenInfo.current_h // 2
    circlePosition = (xCircle, yCircle)
    circleRadius = 75

    xMouse = 0
    yMouse = 0
    mousePosition = (xMouse, yMouse)

    animalSpeed = 5
    clicked = False

    #-----------ANIMAL CREATION SECTION----------------
    #THE FISH
    #fish head
    fishHead = BodyPart()
    fishHead.radius = 55
    fishHead.color = "red"
    fishHead.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    #fish "rest"
    fish0 = BodyPart()
    fish0.radius = 75
    fish0.color = "red"
    fish0.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    #Setup body parts
    bodyFISH = AnimalBody()
    bodyFISH.body.append(fishHead)
    bodyFISH.body.append(fish0)

    print(bodyFISH.body)

    while running:
        screen.fill("black")
        clock.tick(fps)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True
                        
        xMouse, yMouse = pygame.mouse.get_pos()
        mousePosition = (xMouse, yMouse)
                        
        #Geting the main vector angle (already taking care of the quadrant)
        angle = math.atan2((yMouse - yCircle),(xMouse - xCircle))
        angle += math.radians(180)

        #Setting the circle vector second point
        xSecondPoint = xCircle + circleRadius * math.cos(angle)
        ySecondPoint = yCircle + circleRadius * math.sin(angle)
        #Passing the second point as the center of the next part
        fish0.coordinates = (xSecondPoint, ySecondPoint)
        
        #Design circle vector second point
        drawCircle(screen, (xSecondPoint, ySecondPoint), 5, 0)
        #Design radius line
        pygame.draw.line(screen, "white", (xCircle, yCircle), (xSecondPoint, ySecondPoint))

        # --------------------------------------------------------------------------------
        #Updating the head position towards the mouse
        if clicked:
            if xCircle != xMouse or yCircle != yMouse:
                xCircle, yCircle= updateCirclePositionVector(circlePosition, mousePosition, animalSpeed)
                circlePosition = (xCircle, yCircle)

                #Design trajectory line
                pygame.draw.line(screen, "green", (xCircle, yCircle), (xMouse, yMouse))

        #Design main circle
        drawCircle(screen, (xCircle, yCircle), circleRadius, 1)
        
        #Design the animal
        #for bodyPart in bodyFISH.body:
            #drawCircle(screen, bodyPart.coordinates, bodyPart.radius, 1)

        pygame.display.flip()
        
pygame.quit()

class BodyPart:
    def __init__(self):
        self.radius = 0
        self.color = "white"
        self.coordinates = ()
        self.anchorCoordinates = ()

class AnimalBody:
    def __init__(self):
        self.body = []
        self.species = ""
    

if __name__ == "__main__":
    main()