import pygame

class Projectil(pygame.sprite.Sprite):
    def __init__(self, user):
        super().__init__()
        img = pygame.image.load(r'res/stella.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.rect = self.image.get_rect()
        self.rect.x = user.getX()
        self.rect.y = user.getY()
        self.direction = user.getDirection()
        
        
    def update(self):
        self.rect.x += int(self.direction['x'])
        self.rect.y += int(self.direction['y'])
        

