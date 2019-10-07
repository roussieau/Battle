import pygame
from datetime import datetime, timedelta

POS = [-2, -1, 0 , 1, 2, 1 , 0, -1]    
INTERVAL_BETWEEN_SHOT = timedelta(seconds=1) 

class User(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        img = pygame.image.load(r'res/adrien.png')
        self.image = pygame.transform.scale(img, (80,80))
        self.rect = self.image.get_rect()
        self.directionX = 2
        self.directionY = 0 
        self.lastShot = datetime.now() 
        
        
    def moveUp(self):
        self.rect.y -= 3 if self.rect.y-3 >= 0 else 0

    def moveDown(self):
        self.rect.y += 3 if self.rect.y+3 < 900 else 0

    def moveLeft(self):
        self.rect.x -= 3 if self.rect.x-3 >= 0 else 0  

    def moveRight(self):
        self.rect.x += 3 if self.rect.x+3 < 900 else 0

    def getDirection(self):
        return {
            'x': POS[self.directionX],
            'y': POS[self.directionY]
        }

    def updateDirectionLeft(self):
        self.directionX = (self.directionX + 1) % 8
        self.directionY = (self.directionY + 1) % 8
        
    def canShot(self):
        canShot = datetime.now() - self.lastShot > INTERVAL_BETWEEN_SHOT
        if canShot:
            self.lastShot = datetime.now()
        return canShot
        
    def getX(self):
        x = self.rect.x
        return x 

    def getY(self):
        y = self.rect.y
        return y 
