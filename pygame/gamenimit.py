#!/usr/bin/env python3
import os
import warnings

# 1. Set environment variables BEFORE importing pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
# This tells pygame you've acknowledged the AVX2 situation
os.environ['PYGAME_DETECT_AVX2'] = "1" 

# 2. Silence the warning via the warnings module (as a backup)
warnings.filterwarnings('ignore', category=RuntimeWarning, message=".*AVX2.*")

 

import pygame

pygame.init()
print("ok")

font = pygame.font.SysFont('Arial', 100)

screen = pygame.display.set_mode((1000, 600))
pygame.display.set_caption("Cambodia vs Thailands")



soldiersRight = [pygame.image.load('tile000.png'), pygame.image.load('tile001.png'), pygame.image.load('tile002.png'), pygame.image.load('tile003.png')]
soldiersLeft = [pygame.image.load('1.png'), pygame.image.load('2.png'), pygame.image.load('3.png')]
bomb = [pygame.image.load('bomb.png')]
##pygame.image.load('4.png')]


background = pygame.image.load('warbg.png')

plane = [pygame.image.load('jet.webp')]

tank = [pygame.image.load('tankright.png')]
tank1 = [pygame.image.load('Tankleft.png')]

bomb2 = [pygame.image.load('bomb.png')]
bomb3 = [pygame.image.load('bomb.png')]
bomb4 = [pygame.image.load('bomb.png')]
bomb5 = [pygame.image.load('bomb.png')]

missle = [pygame.image.load('missle.png')]

fireball = [pygame.image.load("fireball.png")]

explosion = [pygame.image.load('1explosion.webp')]

run = True

x1 = 800
x2 = 50
x3 = 400
x4 = 800
x5 = 350
x6 = 325
x7 = 300

xplane1 = 1000
xplane2 = 1050
xplane3 = 1100
xplane4 = 1150
xplane5 = 1200

bomb1_x = -300
bomb2_x = -600
bomb3_x = -850
bomb4_x = -1100
bomb5_x = -400

missle_y = 500

leftSoldier = False
rightSoldier = True


leftTank = False
rightTank = True

countsoldier = 0



shootTank = False

fireballX = 0
fireballY = 0


def endGame():
    print('a b c d e f g h i j k l m n o p q r s t u v w x y z')
    screen.fill((0,0,0))
    text_end_game = font.render('Game over!', True, (255, 255, 255))
    screen.blit(text_end_game, (100, 100))
    pygame.display.flip()

    pygame.display.update() 
    pygame.time.wait(2000)

    pygame.quit()

def redrawGameWindow():
    ##print(xplane1)

    global walkCount
    if walkCount + 1 >= 27:
        walkCount = 0

    global walkCountTank
    if walkCountTank + 1 >= 27:
        walkCountTank = 0
    
    screen.blit(background, (0,0))  

    if leftSoldier == True:
        screen.blit(soldiersLeft[walkCount//3], (x4,500))
        walkCount+=1
    elif rightSoldier == True:
        screen.blit(soldiersRight[walkCount//3], (x4,500))
        walkCount+=1
      
    if leftTank == True:
        screen.blit(tank1[walkCountTank//2], (x1,500))
        walkCountTank+=1
    elif rightTank == True:
        screen.blit(tank[walkCountTank//2], (x1,500))
        walkCountTank+=1
       


    
    #screen.blit(explosion[0], (10,10))

    ##screen.blit(tank[0], (x1,500))
    screen.blit(plane[0], (xplane1,50))
    screen.blit(plane[0], (xplane2,100))
    screen.blit(plane[0], (xplane3,150))
    screen.blit(plane[0], (xplane4,200))
    screen.blit(plane[0], (xplane5,250))
    
    ##pygame.draw.rect(screen, (255, 0, 0), (x4, 500, 16, 24)) 

    if shootTank == True:
        screen.blit(fireball[0], (500, missle_y)) 
      
        


 
    if xplane1 < 800:
        screen.blit(bomb[0], (800 , bomb1_x))
    if xplane2 < 700:
        screen.blit(bomb2[0], (700 , bomb2_x))
    if xplane3 < 600:
        screen.blit(bomb3[0], (600 , bomb3_x))
    if xplane4 < 500:
        screen.blit(bomb4[0], (500 , bomb4_x))
    if xplane5 < 400:
        screen.blit(bomb5[0], (400 , bomb5_x))        




     
    pygame.display.update() 

while run:
    walkCount = 0
    walkCountTank = 0
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:  # 1 = Left Click, 2 = Middle, 3 = Right
                print(f"Left click detected at position: {event.pos}")
                shootTank = True
                screen.blit(fireball[0], (x1,missle_y))
                pygame.display.update() 



    keys = pygame.key.get_pressed()
        
    #if x3 == bomb1:
        #print("You lose!  1")
        #pygame.quit()

    print("x3:",x3)
    print("xbomb:",bomb1_x)
    if bomb1_x == 500 and x4 == 800:
       print("You lose!(soldier)")
       screen.blit(explosion[0], (800,500))
       pygame.display.update() 
       pygame.time.wait(2000)
       endGame()

    if bomb2_x == 500 and x4 == 700:
       print("You lose!(soldier)")
       screen.blit(explosion[0], (690,500))
       pygame.display.update() 
       pygame.time.wait(2000)
       endGame()

    if bomb3_x == 500 and x4 == 600:
       print("You lose!(soldier)")
       screen.blit(explosion[0], (590,500))
       pygame.display.update() 
       pygame.time.wait(2000)
       endGame()

    if bomb4_x == 500 and x4 == 500:
       print("You lose!(soldier)")
       screen.blit(explosion[0], (490,500))
       pygame.display.update() 
       pygame.time.wait(2000)
       endGame()

    if bomb5_x == 500 and x4 == 400:
       print("You lose!(soldier)")
       screen.blit(explosion[0], (390,500))
       pygame.display.update() 
       pygame.time.wait(2000)
       endGame()

    if bomb1_x == 500 and x1 == 800:
        print("You lose!(Tank)")
        screen.blit(explosion[0], (800,500))
        pygame.display.update() 
        pygame.time.wait(2000)
        endGame()

    if bomb2_x == 500 and x1 == 700:
        print("You lose!(Tank)")
        screen.blit(explosion[0], (700,500))
        pygame.display.update() 
        pygame.time.wait(2000)
        endGame()

    if bomb3_x == 500 and x1 == 600:
        print("You lose!(Tank)")
        screen.blit(explosion[0], (600,500))
        pygame.display.update() 
        pygame.time.wait(2000)
        endGame()

    if bomb4_x == 500 and x1 == 500:
        print("You lose!(Tank)")
        screen.blit(explosion[0], (500,500))
        pygame.display.update() 
        pygame.time.wait(2000)
        endGame()

    if bomb5_x == 500 and x1 == 400:
        print("You lose!(Tank)")
        screen.blit(explosion[0], (400,500))
        pygame.display.update() 
        pygame.time.wait(2000)
        endGame()

    fireballX = 500
    fireballY = missle_y

    if xplane3 == 500 and fireballY :
        print('ach')



    if keys[pygame.K_LEFT] and x1 > 0:
        x1-= 5
        print("left")
        leftTank = True
        RightTank = False
    if keys[pygame.K_RIGHT] and x1 > 0:
        x1-= -5
        print("right")
        leftTank = False
        rightTank = True
    if keys[pygame.K_a] and x2 > 0:
        x2-=5
        print("a")
    if keys[pygame.K_d] and x2 > 0:
        x2-=-5
        print("d")
    
    if keys[pygame.K_j] and x2 > 0:
        x3-=5
        x4-=5
        print("j")
        leftSoldier =True
        rightSoldier = False
    elif keys[pygame.K_k] and x2 > 0:
        x3-=-5
        x4-=-5
        print("k")
        leftSoldier = False
        rightSoldier = True
    else:
        walkCount = 0
    xplane1 -=5
    xplane2 -=5
    xplane3 -=5
    xplane4 -=5
    xplane5 -=5

    bomb1_x +=10
    bomb2_x +=10
    bomb3_x +=10
    bomb4_x +=10
    bomb5_x +=10

    missle_y -=3




    
    
    screen.fill((0,0,0))
    ##bomb
    ##pygame.draw.rect(screen, (0, 87, 12), (400, bomb1, 45, 20))
    ##tank
    pygame.draw.rect(screen, (0, 87, 12), (x1, 700, 40, 20))
    pygame.draw.rect(screen, (0, 87, 12), (x2, 500, 40, 20))
    pygame.draw.rect(screen, (0, 87, 12), (250, 500, 40, 20))
    pygame.draw.rect(screen, (0, 87, 12), (200, 500, 40, 20))
    pygame.draw.rect(screen, (0, 87, 12), (150, 500, 40, 20)) 
    ##jet
    pygame.draw.rect(screen, (255, 255, 255), (xplane1, 50, 45, 20))
    pygame.draw.rect(screen, (255, 255, 255), (xplane2, 100, 45, 20))
    pygame.draw.rect(screen, (255, 255, 255), (xplane3, 150, 45, 20))
    pygame.draw.rect(screen, (255, 255, 255), (xplane4, 200, 45, 20))
    pygame.draw.rect(screen, (255, 255, 255), (xplane5, 250, 45, 20)) 
    ##soldier
    ##pygame.draw.rect(screen, (255, 0, 0), (x4, 500, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x4, 475, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x4, 450, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x4, 425, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x4, 400, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x3, 500, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x3, 475, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x3, 450, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x3, 425, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (x3, 400, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (350, 500, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (350, 475, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (350, 450, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (350, 425, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (350, 400, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (325, 500, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (325, 475, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (325, 450, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (325, 425, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (325, 400, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (300, 500, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (300, 475, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (300, 450, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (300, 425, 16, 24))
    pygame.draw.rect(screen, (255, 0, 0), (300, 400, 16, 24)) 


 





    redrawGameWindow()

pygame.quit()
