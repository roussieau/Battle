import pygame, random
from user import User, DrawUser
from projectil import Projectil
from settings import * 
from network import Network
from _thread import *

pygame.init()

size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("The battle of CI")

#This will be a list that will contain all the sprites we intend to use in our game.
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

def shot(keys):
    if not playerUser.canShot():
        return
    if keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
        projectils.add(Projectil(NORTH_EAST, playerUser))  
    elif keys[pygame.K_DOWN] and keys[pygame.K_RIGHT]:
        projectils.add(Projectil(SOUTH_EAST, playerUser))  
    elif keys[pygame.K_DOWN] and keys[pygame.K_LEFT]:
        projectils.add(Projectil(SOUTH_WEST, playerUser))  
    elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
        projectils.add(Projectil(NORTH_WEST, playerUser))  
    elif keys[pygame.K_UP]:
        projectils.add(Projectil(NORTH, playerUser))  
    elif keys[pygame.K_RIGHT]:
        projectils.add(Projectil(EAST, playerUser))  
    elif keys[pygame.K_DOWN]:
        projectils.add(Projectil(SOUTH, playerUser))  
    elif keys[pygame.K_LEFT]:
        projectils.add(Projectil(WEST, playerUser))  


def stillOnMap(x, y):
    return x >= 0 and x < SCREENWIDTH and y >= 0 and y < SCREENHEIGHT

def addPlayer(id, x, y):
    if users[id] == None:
        users[id] = DrawUser(x, y)
        objects.add(users[id])
    else: 
        users[id].setPosition(x, y)

def threaded_client(conn):
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                print("no data")
                break
            else:
                arr = reply.split(":")
                id = int(arr[0])
                if len(arr) == 3:
                    addPlayer(id, int(arr[1]), int(arr[2]))

        except Exception as e:
            print("exception: " + str(e))
            break

    print("Connection Closed")
    conn.close()




net = Network()
start_new_thread(threaded_client, (net.client,))

users = [None] * 10

playerUser = User(net)
objects = pygame.sprite.Group()
objects.add(playerUser)

projectils = pygame.sprite.Group()
carryOn = True
clock=pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
    move()
    events = pygame.event.get()

    screen.fill(GREY)
    for o in objects: 
        screen.blit(o.image, o.rect) 
    
    for p in projectils:
        p.update()
        if not stillOnMap(p.rect.x, p.rect.y):
            projectils.remove(p)
        else:
            screen.blit(p.image, p.rect)

    blocks_hit_list = pygame.sprite.spritecollide(playerUser, projectils, True)
    if len(blocks_hit_list) != 0:
        print(blocks_hit_list)
        print('boom')


    #Refresh Screen
    pygame.display.flip()

    #Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()


