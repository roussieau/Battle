import pygame, random
from user import User, DrawUser
from projectil import Projectil
from settings import * 
from network import Network
from _thread import *
import time
import sys

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
pygame.display.set_caption("The battle of CI")

red = (255,0,0)

MY_ID = int(sys.argv[1])

def move():
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_q]:
        playerUser.moveLeft() 
    if keys[pygame.K_d]:
        playerUser.moveRight() 
    if keys[pygame.K_z]:
        playerUser.moveUp() 
    if keys[pygame.K_s]:
        playerUser.moveDown() 
    if keys[pygame.K_LEFT]:
        playerUser.updateDirectionLeft() 
    if keys[pygame.K_RIGHT]:
        playerUser.updateDirectionRight() 
    if keys[pygame.K_SPACE]:
        shot(keys)
    if keys[pygame.K_ESCAPE]:
        carryOn = False
        pygame.quit()

def shot(keys):
    if not playerUser.canShot():
        return
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        projectils.add(Projectil(NORTH_EAST, playerUser, net))  
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        projectils.add(Projectil(SOUTH_EAST, playerUser, net))  
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        projectils.add(Projectil(SOUTH_WEST, playerUser, net))  
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        projectils.add(Projectil(NORTH_WEST, playerUser, net))  
    elif keys[pygame.K_UP]:
        projectils.add(Projectil(NORTH, playerUser, net))  
    elif keys[pygame.K_RIGHT]:
        projectils.add(Projectil(EAST, playerUser, net))  
    elif keys[pygame.K_DOWN]:
        projectils.add(Projectil(SOUTH, playerUser, net))  
    elif keys[pygame.K_LEFT]:
        projectils.add(Projectil(WEST, playerUser, net))  




def addPlayer(id, x, y):
    if users[id] == None:
        users[id] = DrawUser(id, x, y)
        players.add(users[id])
    else: 
        users[id].setPosition(x, y)

def drawProjectils():
    for p in projectils:
        p.update()
        if not p.stillOnMap():
            projectils.remove(p)
        else:
            screen.blit(p.image, p.rect)

def drawPlayers():
    for p in players: 
        screen.blit(p.image, p.rect) 

def text_objects(text, font):
    textSurface = font.render(text, True, red) 
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREENWIDTH/2),(SCREENHEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()


def iAmDead():
    blocks_hit_list = pygame.sprite.spritecollide(playerUser, projectils, True)
    if len(blocks_hit_list) != 0:
        message_display("Take a shot and press enter !")
        net.send('d')
        while True:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    break
        playerUser.respawn()


net = Network(MY_ID)

users = [None] * 10

playerUser = User(MY_ID)
players = pygame.sprite.Group()
players.add(playerUser)

projectils = pygame.sprite.Group()
carryOn = True
clock = pygame.time.Clock()


bg = pygame.image.load(r'res/bg.png')

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
    move()
    events = pygame.event.get()
    
    try:
        reply = net.send(playerUser.position())
        print(reply)
        for r in reply.split(";"):
            arr = r.split(':')
            if len(arr) > 1:
                id = int(arr[0])
                if id != MY_ID:
                    if arr[1] == 'd':
                        players.remove(users[id])
                        users[id] = None    
                    elif arr[1] == 'p':
                        projectils.add(Projectil(int(arr[2]), users[id]))  
                    else:
                        addPlayer(id, int(arr[1]), int(arr[2]))

    except Exception as e:
        print("exception: " + str(e))


   
    screen.blit(bg, [0, 0])
    drawPlayers()
    drawProjectils()
    iAmDead()

    #Refresh Screen
    pygame.display.flip()

    #Number of frames per secong e.g. 60
    clock.tick(30)

pygame.quit()
