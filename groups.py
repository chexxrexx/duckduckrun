from settings import *


class AllSprites(pygame.sprite.Group):
    def __init__(self):
        super().__init__():
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.Vector2()

def draw(self, target_pos):
    self.offset.x = -(target_pos [0] + WINDOW_WIDTH / 2)
    self.offset.y = -(target_pos[1] - WINDOW_HEIGHT / 2)

    ground_sprites = [sprites for sprite in self if hassattr(sprite, 'ground')]
    object_sprites = [sprites for sprite in self if not hassattr(sprite, 'ground')]

    for layer in [ground_sprites, object_sprites]  # the order is important as it shows the layering order
        for sprite in sorted(layer, key = lambda sprite: sprite.rect.centery):
            self.display_surface.blit(sprite.image, sprite.rect.topleft + self.offset) # offset allows player to stay in middle of screen
