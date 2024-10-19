from settings import *

from player import Player

from sprites import *

from pytmx.util_pygame import load_pygame

from groups import AllSprites

from random import randint, choice 

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
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()

        # spit timer (edited as there's no gun)  
        self.can_shoot = True
        self.spit_time = 0
        self.spit_cooldown = 100

        # enemy timer 
        self.enemy_event = pygame.event.custome_type()
        pygame.time.set_timer(self.enemy_event, 300)
        self.spawn_positions = []

        # setup
        self.load_images()
        self.setup()

    def load_images(self):
        self.bullet_surf = pygame.image.load(join('images', 'gun', 'bullet.png)).convert_alpha()

        # COME BACK AND CHANGE FILE NAMES                                          
        folders = list(walk(join('images', 'enemies')))[0] [1]
        self.enemy_frames = {}            
        for folder in folders:
                for folder_path, _, file_names in walk(join('images', 'enemies', folder)):
                    self.enemy_frames[folder] = []
                    for file_name in sorted(file_name, key = lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.enemy_frames[folder].append(surf)

    def input(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            Bullet(self.bullet_surf, pos, (self.all.sprites, self.bullet_sprites))
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    # slightly changed from gun_timer as there's no gun
    def spit_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time >= self.spit_cooldown:
                self.can_shoot = True
        
        def setup(self):
        # map is not affected by overlap as it's always on the bottom
        map = load_pygame(join('data', 'map', 'world.tmx'))

        for x, y, image in map.get_layer_by_name('Ground').tiles():
            Sprites ((x * TILE_SIZE,y *TILE_SIZE), image, self.all_sprites)

        for obj in map.get_layer_by_name('Objects'):
            CollisionSprite((obj.x, obj.y), obj.image, (self.all_sprites, self.collision_sprites))

        for obj in map.get_layer_by_name('Collisions'):
            CollisionSprite((obj.x, obj.y), pygame.Surface((obj.width, obj.height)), self.collision_sprites_sprites)

        for obj in map.get_layer_by_name('Entities'):
            if obj.name == 'Player':
                 self.player = Player((obj.x, obj.y), self.all_sprites, self.collision_sprites)
                 
    def bullet_collision(self):
         if self.bullet_sprites:
             for bullet in self.bullet_sprites:
                 collision_sprites = pygame.sprite.spritecollide(bullet, self.enemy_sprites, False, pygame.sprite.collide_mask)
                 if collision_sprite:
                     for sprite in collision_sprites:
                         sprite.destroy()
                    bullet.kill()

    def player_collision(self):
        if pygame.sprite.spritecollide(self.player, self.enemy_sprites, False, pygame.sprite.collide_mask):
            self.running = False
    
            
    def run(self):
        while self.running:
            dt = self.clock.tick()/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == self.enemy_event:
                    Enemy(choice(self.spawn_positions), choice(list(self.enemy_frames.values())), (self.all_sprites, self.enemy_sprites), self.player, self.collision_sprites)

            # update 
            self.gun_timer()
            self.input()
            self.all_sprites.update(dt)
            self.bullet_collision()
            # self.player_collision()

            # draw
            self.display_surface.fill('black')
            self.all_sprites.draw(self.player.rect.center)
            pygame.display.update()

        pygame.quit()

if __name__ == '__main__':
    game = Game()
    game.run()

