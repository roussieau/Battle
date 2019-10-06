import pygame

POS = [-2, -1, 0 , 1, 2, 1 , 0, -1]    

class User(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        img = pygame.image.load(r'cat.png')
        self.image = pygame.transform.scale(img, (100,100))
        self.pos = self.image.get_rect()
        self.directionX = 2
        self.directionY = 0 
        
        
    def moveUp(self):
        self.pos.y -= 5 if self.pos.y-5 >= 0 else 0

    def moveDown(self):
        self.pos.y += 5 if self.pos.y+5 < 900 else 0

    def moveLeft(self):
        self.pos.x -= 5 if self.pos.x-5 >= 0 else 0  

    def moveRight(self):
        self.pos.x += 5 if self.pos.x+5 < 900 else 0

    def getDirection(self):
        return {
            'x': POS[self.directionX],
            'y': POS[self.directionY]
        }

    def updateDirectionLeft(self):
        self.directionX = (self.directionX + 1) % 8
        self.directionY = (self.directionY + 1) % 8
        
