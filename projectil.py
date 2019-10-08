import pygame

class Projectil(pygame.sprite.Sprite):
    def __init__(self, user):
        super().__init__()
        img = pygame.image.load(r'res/stella.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.direction = user.getDirection()
        if self.direction['x'] < 0:
            self.rect.centerx = user.getX() - 65 
        elif self.direction['x'] > 0: 
            self.rect.centerx = user.getX() + 65 
        else: 
            self.rect.centerx = user.getX()
        if self.direction['y'] < 0:
            self.rect.centery = user.getY() - 65 
        elif self.direction['y'] > 0:
            self.rect.centery = user.getY() + 65 
        else:
            self.rect.centery = user.getY()
        
        
    def update(self):
        self.rect.x += int(self.direction['x'])
        self.rect.y += int(self.direction['y'])
        

