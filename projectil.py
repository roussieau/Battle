import pygame
from settings import *

class Projectil(pygame.sprite.Sprite):
    def __init__(self, direction, user):
        super().__init__()
        img = pygame.image.load(r'res/stella.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.direction = direction
        if POS_X[direction] < 0:
            self.rect.centerx = user.getX() - 65 
        elif POS_X[direction] > 0: 
            self.rect.centerx = user.getX() + 65 
        else: 
            self.rect.centerx = user.getX()
        if POS_Y[direction] < 0:
            self.rect.centery = user.getY() - 65 
        elif POS_Y[direction] > 0:
            self.rect.centery = user.getY() + 65 
        else:
            self.rect.centery = user.getY()

        if user.net != None:
            data = "p:{}:{}:{}".format(direction, user.getX(), user.getY())
            user.net.send(data)
        
        
    def update(self):
        self.rect.x += POS_X[self.direction]
        self.rect.y += POS_Y[self.direction] 
