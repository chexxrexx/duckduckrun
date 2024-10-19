from settings import *
from player import Player

class CollisionSprite(pygame.sprite.Sprite):
    def __init__(self, pos, size, groups):
        super().__init__(groups)
        self.image.fill('blue') # Fills the image with a blue colour
        self.rect = self.image.get_rect(center = pos) # Creates the rectangle and positions it at center pos
        self.ground = True #This allows the ground to be layered correctly beneath other elements
