import pygame
import math

def drawCircle(screen, position, radius, width, color):
    pygame.draw.circle(screen, color, position, radius, width) 

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
    #Get the target coordinates
    xMouse = mousePosition[0]
    yMouse = mousePosition[1]

    #Get the vector circle/target
    xVector = xMouse - xCircle
    yVector = yMouse - yCircle
    #Get the module of the vector
    module = math.sqrt((xVector)**2 + (yVector)**2)

    if module != 0:
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

    animalSpeed = 2.5
    clicked = False

    #-----------ANIMAL CREATION SECTION----------------
    #THE FISH
    #fish head
    fishHead = BodyPart()
    fishHead.radius = 25
    fishHead.color = "red"
    fishHead.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    #fish "rest"
    fish0 = BodyPart()
    fish0.radius = 45
    fish0.color = "white"
    fish0.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish1 = BodyPart()
    fish1.radius = 55
    fish1.color = "white"
    fish1.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish2 = BodyPart()
    fish2.radius = 55
    fish2.color = "white"
    fish2.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish3 = BodyPart()
    fish3.radius = 45
    fish3.color = "white"
    fish3.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish4 = BodyPart()
    fish4.radius = 45
    fish4.color = "white"
    fish4.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish5 = BodyPart()
    fish5.radius = 25
    fish5.color = "white"
    fish5.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish6 = BodyPart()
    fish6.radius = 25
    fish6.color = "white"
    fish6.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish7 = BodyPart()
    fish7.radius = 25
    fish7.color = "white"
    fish7.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish8 = BodyPart()
    fish8.radius = 25
    fish8.color = "white"
    fish8.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish9 = BodyPart()
    fish9.radius = 25
    fish9.color = "white"
    fish9.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    fish10 = BodyPart()
    fish10.radius = 25
    fish10.color = "white"
    fish10.coordinates = (screenInfo.current_w // 2, screenInfo.current_h // 2)

    #Setup body parts
    bodyFISH = AnimalBody()
    bodyFISH.body.append(fishHead)
    bodyFISH.body.append(fish0)
    bodyFISH.body.append(fish1)
    bodyFISH.body.append(fish2)
    bodyFISH.body.append(fish3)
    bodyFISH.body.append(fish4)
    bodyFISH.body.append(fish5)
    bodyFISH.body.append(fish6)
    bodyFISH.body.append(fish7)
    bodyFISH.body.append(fish8)
    bodyFISH.body.append(fish9)
    bodyFISH.body.append(fish10)
    
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
                    
        #=================================================================
        #Update head: center and anchor
        #Updating the head position towards the mouse
        if clicked:
            if xCircle != xMouse or yCircle != yMouse:
                xCircle, yCircle= updateCirclePositionVector(circlePosition, mousePosition, animalSpeed)
                circlePosition = (xCircle, yCircle)

                #Passing the head coordinates to the register
                bodyFISH.body[0].coordinates = circlePosition

                #Design trajectory line
                #pygame.draw.line(screen, "green", (xCircle, yCircle), (xMouse, yMouse))

                #Update anchor
                #Geting the main vector angle (already taking care of the quadrant)
                angle = math.atan2((yMouse - bodyFISH.body[0].coordinates[1]),(xMouse - bodyFISH.body[0].coordinates[0]))
                angle += math.radians(180)

                #Setting the circle vector second point
                xSecondPoint = bodyFISH.body[0].coordinates[0] + bodyFISH.body[0].radius * math.cos(angle)
                ySecondPoint = bodyFISH.body[0].coordinates[1] + bodyFISH.body[0].radius * math.sin(angle)
                
                #Passing the anchor coordinates to the register
                bodyFISH.body[0].anchorCoordinates = (xSecondPoint, ySecondPoint)

                #Design circle vector second point
                #drawCircle(screen, (xSecondPoint, ySecondPoint), 5, 0, "red")
                #Design radius line
                #pygame.draw.line(screen, "white", (xCircle, yCircle), (xSecondPoint, ySecondPoint))

            #Design the head    
            drawCircle(screen, bodyFISH.body[0].coordinates, fishHead.radius, 1, "red")

            #Iterate throw animalBody from the second body part
            for aPIndex in range(1, len(bodyFISH.body)):
                #If the distance betwn centers are bigger than the radius

                #Get the distance bwetn the centers:
                #Get the vector circle/target
                currentCoords = bodyFISH.body[aPIndex].coordinates
                previousCoords =  bodyFISH.body[aPIndex - 1].coordinates
                xVector = previousCoords[0] - currentCoords[0]
                yVector = previousCoords[1] - currentCoords[1]
                #Get the module of the vector
                module = math.sqrt((xVector)**2 + (yVector)**2)

                #If the distance btewn centers is bigger than the previous body radius
                if module > (bodyFISH.body[aPIndex - 1].radius + bodyFISH.body[aPIndex].radius):
                    #Update the current bodyPart position
                    bodyFISH.body[aPIndex].coordinates = updateCirclePositionVector(currentCoords, previousCoords, animalSpeed)
        
                #Design the bodyPart
                bodyPartColor = bodyFISH.body[aPIndex].color
                drawCircle(screen, bodyFISH.body[aPIndex].coordinates, bodyFISH.body[aPIndex].radius, 1, bodyPartColor)
            #=================================================================

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