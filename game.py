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
       p = Projectil(playerUser.getDirection())
       projectils.append(p)
       print(p)


def stillOnMap(x, y):
    return x >= 0 and x < SCREENWIDTH and y >= 0 and y < SCREENHEIGHT



playerUser = User()
objects = []
objects.append(playerUser)

projectils = []
#Allowing the user to close the window...
carryOn = True
clock=pygame.time.Clock()

while carryOn:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            carryOn=False
    move()
    screen.fill(GREEN)
    events = pygame.event.get()

    for o in objects: 
        screen.blit(o.image, o.pos) 
    
    for p in projectils:
        p.update()
        if not stillOnMap(p.pos.x, p.pos.y):
            projectils.remove(p)
        else:
            screen.blit(p.image, p.pos)
        


    #Now let's draw all the sprites in one go. (For now we only have 1 sprite!)

    #Refresh Screen
    pygame.display.flip()

    #Number of frames per secong e.g. 60
    clock.tick(60)

pygame.quit()


