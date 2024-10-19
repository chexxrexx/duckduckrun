from settings import *

from player import Player

from sprites import *

from pytmx.util_pygame import load_pygame

from groups import AllSprites

from random import randint

class Game:
    def __init__(self):
        # setup
        pygame.init()
        self.display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("duck duck run")
        self.clock = pygame.time.Clock()
        self.running = True

        # groups
        self.all.sprites == AllSprites()
        self.collision_sprites = pygame.sprite.Group()
        self.setup()

        def setup(self):
        # map is not affected by overlap as it's always on the bottom
        map = load_pygame(join('data', 'map', 'world.tmx'))

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprites ((x * TILE_SIZE,y *TILE_SIZE), image, self.all.sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                 self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)

        # unsure of neccessity of this
        self.player = Player((400,300), self.all_sprites, self.collision_sprites)
        for i in range(6):
            x, y = randint(0, WINDOW_WIDTH), randint(0, WINDOW_HEIGHT)
            w, h = randint(60,100), randint(50,100)
            CollisionSprite((x,y), (w,h), (self.all_sprites, self.collision_sprites))
            
    def run(self):
        while self.running:
            dt = self.clock.tick()/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.display_surface.fill('black)

            self.all_sprites.update(dt)

            #following code makes it so the camera follows the player
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

