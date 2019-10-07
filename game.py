import pygame, random
from user import User 
from projectil import Projectil
pygame.init()


GREEN = (128,128,128)

SCREENWIDTH=1000
SCREENHEIGHT=1000

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
    if keys[pygame.K_SPACE]:
       if playerUser.canShot():
           p = Projectil(playerUser)
           projectils.append(p)


def stillOnMap(x, y):
    return x >= 0 and x < SCREENWIDTH and y >= 0 and y < SCREENHEIGHT



playerUser = User()
objects = []
objects.append(playerUser)

projectils = []
carryOn = True
clock=pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
    move()
    events = pygame.event.get()

    screen.fill(GREEN)
    for o in objects: 
        screen.blit(o.image, o.rect) 
    
    for p in projectils:
        p.update()
        if not stillOnMap(p.rect.x, p.rect.y):
            projectils.remove(p)
        else:
            screen.blit(p.image, p.rect)

    #Refresh Screen
    pygame.display.flip()

    #Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()


