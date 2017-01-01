import pygame
import random
import time

pygame.init()


#Screen Var
width = 800
height = 600

#Colour Var
white = (255,255,255)
green =(0, 255, 0)
blue = (0, 190, 255)
red = (255, 0, 0)
black = (0, 0, 0)

#Game Var
clock = pygame.time.Clock()
gameExit = False

#Player Var
shipWidth = 60
shipHeight = 60


    

####### -- Basic Functions -- #######

#Draw screen
gameDisplay = pygame.display.set_mode((width, height))
gameDisplay.fill(black)
pygame.display.set_caption("Space Shooter")

#Draw text
def draw_text(message, colour, x, y, size):
    textFont = pygame.font.Font('freesansbold.ttf', size)
    renderMapText = textFont.render(message, 0, (colour))
    gameDisplay.blit(renderMapText, (x, y))
    

def game_over(message, colour, x, y, size):
    textFont = pygame.font.Font('freesansbold.ttf', size)
    renderMapText = textFont.render(message, 0, (colour))
    gameDisplay.blit(renderMapText, (x, y))

    pygame.display.update()

    time.sleep(2)

    game_loop()

#Draw rectangle
def draw_rect(colour, x, y, width, height):
    pygame.draw.rect(gameDisplay, colour, (x, y, width, height), fill)


#Load image
def load_image(img, width, height, x, y):
    imgSurface = pygame.image.load(img)
    imgSurface = pygame.transform.scale(imgSurface, (width, height))        

    gameDisplay.blit(imgSurface, (x, y))

#loads data from text file
def load_data(name):
    textFile = open(name, 'r')
    data = textFile.readline()
        
    textFile.close()
    print(data)



####### -- Background Functions -- #######
def background(y1, y2):
    load_image('Images/Stars-Nebulae/Stars.png', width, (height*2), 0, y1)
    load_image('Images/Stars-Nebulae/Nebula3.png', width, height, 0, y2)
   

####### -- Player Functions -- #######
def draw_player(x, y):
    load_image('Images/Example_ships/1.png', shipWidth, shipHeight, x, y)


def player_crash():
    game_over('GAME OVER!', green, (width/4), (height/4), 60)

 
 

####### -- Enemy Functions -- #######

def game_loop():
    ship_x = (width * 0.45)
    ship_y = (height * 0.8)

    bullet_x = (width * 0.45)
    bullet_y = (ship_y - 10)

    playerSpeed = 10
    bulletSpeed = 20
    
    xChange = 0
    yChange = 0
    
    backgroundScroll1 = -(height*2)
    backgroundScroll2 = -(height)
    

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                playerHit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    xChange = -(playerSpeed)
                elif event.key == pygame.K_RIGHT:
                    xChange = playerSpeed
                elif event.key == pygame.K_UP:
                    yChange = -(playerSpeed)
                elif event.key == pygame.K_DOWN:
                    yChange = playerSpeed
                
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    xChange = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    yChange = 0
                

        ship_x += xChange
        ship_y += yChange
        

        #Background Scroll 1
        if backgroundScroll1 > (height):
            backgroundScroll1 = -(height*2)
        else:
            backgroundScroll1 = backgroundScroll1 + 10

        #Background Scroll 2
        if backgroundScroll2 > height:
            backgroundScroll2 = -(height)
        else:
            backgroundScroll2 = backgroundScroll2 + 10           
        
        gameDisplay.fill(black)
        background(backgroundScroll1, backgroundScroll2)
        draw_player(ship_x, ship_y)
        
        

        if ship_x > width - shipWidth or ship_x < 0 or ship_y > height - shipHeight or ship_y < 0:
            player_crash()
                               
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()

            
                    
                

  


