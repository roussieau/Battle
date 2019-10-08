import pygame
import random
from datetime import datetime, timedelta
from settings import *

POS = [-2, -1, 0, 1, 2, 1, 0, -1]    

class User(pygame.sprite.Sprite):

    def __init__(self, x=randX(), y=randY()):
        super().__init__()
        img = pygame.image.load(r'res/adrien.png')
        self.image = pygame.transform.scale(img, (USER_HEIGHT, USER_HEIGHT))
    self.rect = self.image.get_rect()
        #Random spawn
        self.rect.x = x 
        self.rect.y = y
        self.directionX = 2
        self.directionY = 0 
        self.lastShot = datetime.now() 
        
    # Movements     
    def moveUp(self):
        if self.rect.y - USER_SPEED >= 0:
            self.rect.y -= USER_SPEED 
        else:
            self.rect.y = 0

    def moveDown(self):
        if self.rect.y + USER_SPEED < MAP_HEIGHT_LIMIT: 
            self.rect.y += USER_SPEED
        else: 
            self.rect.y = 0

    def moveLeft(self):
        if self.rect.x - USER_SPEED >= 0:
            self.rect.x -= USER_SPEED
        else:
            self.rect.x = 0  

    def moveRight(self):
        if self.rect.x + USER_SPEED < MAP_WIDTH_LIMIT:
            self.rect.x += USER_SPEED
        else:
            self.rect.x = 0


    def getDirection(self):
        return {
            'x': POS[self.directionX],
            'y': POS[self.directionY]
        }

    def updateDirectionLeft(self):
        self.directionX = (self.directionX + 1) % 8
        self.directionY = (self.directionY + 1) % 8

    def updateDirectionRight(self):
        self.directionX = (self.directionX - 1) % 8
        self.directionY = (self.directionY - 1) % 8
        
    def canShot(self):
        canShot = datetime.now() - self.lastShot > INTERVAL_BETWEEN_SHOT
        if canShot:
            self.lastShot = datetime.now()
        return canShot
        
    def getX(self):
        x = self.rect.centerx
        return x 

    def getY(self):
        y = self.rect.centery
        return y 

def randX():
    return random.randrange(0, MAP_WIDTH_LIMIT)

def randY():
    return random.randrange(0, MAP_WIDTH_LIMIT) 
