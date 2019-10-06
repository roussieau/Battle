import pygame

class Projectil(pygame.sprite.Sprite):
    def __init__(self, direction):
        super().__init__()
        img = pygame.image.load(r'stella.png')
        self.image = pygame.transform.scale(img, (50,50))
        self.pos = self.image.get_rect()
        self.direction = direction
        
        
    def update(self):
        self.pos.x += int(self.direction['x'])
        self.pos.y += int(self.direction['y'])
        

