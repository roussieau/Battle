import pygame
from settings import *

class Projectil(pygame.sprite.Sprite):
    def __init__(self, direction, user, net=None):
        super().__init__()
        if user.id >= 2:
            img = pygame.image.load(r'res/letter.png')
            self.image = pygame.transform.scale(img, (40,25))
        else: 
            img = pygame.image.load(r'res/stella.png')
            self.image = pygame.transform.scale(img, (25,40))

        self.rect = self.image.get_rect()
        self.direction = direction
        if POS_X[direction] < 0:
            self.rect.centerx = user.getX() - 80
        elif POS_X[direction] > 0: 
            self.rect.centerx = user.getX() + 80
        else: 
            self.rect.centerx = user.getX()
        if POS_Y[direction] < 0:
            self.rect.centery = user.getY() - 80
        elif POS_Y[direction] > 0:
            self.rect.centery = user.getY() + 80 
        else:
            self.rect.centery = user.getY()

        if net != None:
            data = "p:{}:{}:{}".format(direction, user.getX(), user.getY())
            net.send(data)
        
        
    def update(self):
        self.rect.x += POS_X[self.direction]
        self.rect.y += POS_Y[self.direction] 

    def stillOnMap(self):
        return self.rect.x >= 0 and self.rect.x < SCREENWIDTH \
            and self.rect.y >= 0 and self.rect.y < SCREENHEIGHT
