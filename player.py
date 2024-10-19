from settings import * 

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.load_images()
        self.state, self.frame_index = 'right', 0
        self.image = pygame.image.load(join('images', 'player', 'down', '0.png')).convert_alpha()
        self.rect = self.image.get_frect(center = pos)
        self.hitbox_rect = self.rect.inflate(-60, -90) # this is the overlap between player and objects

        # Get the original size of the image
        original_size = self.image.get_size()

        # Scale the image down by half
        new_size = (original_size[0] // 8, original_size[1] // 8)
        self.image = pygame.transform.scale(self.image, new_size)

        # Get the rect and set its center to the position
        self.rect = self.image.get_rect(center=pos)

        self.direction = pygame.Vector2()
        self.speed=500
        self.collision_sprites = collision_sprites

    def load_images(self):
        self.frames = {'left': [], 'right': [], 'up': [], 'down': []}

        for state in self.frames.keys():
            for folder_path, sub_folders, file_names in walk(join('images', 'player', state)):
                if file_names:
                    for file_name in sorted(file_names, key= lambda name: int(name.split('.')[0])):
                        full_path = join(folder_path, file_name)
                        surf = pygame.image.load(full_path).convert_alpha()
                        self.frames[state].append(surf)
    
    def input(self):
        keys=pygame.key.get_pressed()
        self.direction.x = int(keys[pygame.K_RIGHT] or keys[pygame.K_d] - int(keys[pygame.K_LEFT]) or int(keys[pygame.K_w]))
        self.direction.y = int(keys[pygame.K_UP] or keys[pygame.K_w] - int(keys[pygame.K_DOWN]) or int(keys[pygame.K_s]))
        self.direction = self.direction.normalize() if self.direction else self.direction
    
    def move(self,dt):
        self.rect.x += self.direction.x*self.speed*dt #first we move player on the horizontal axis either left or right
        self.collision('horizontal') #then we check for a collision, see if the player is to the left or right of the obsticle, but 1st, we need to get all of the obsticles (done using for loop below)
        self.rect.y += self.direction.y*self.speed*dt
        self.collision('vertical')
        
    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.hitbox_rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.hitbox_rect.right = sprite.rect.left
                    if self.direction.x < 0: self.hitbox_rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.hitbox_rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.hitbox_rect.bottom = sprite.rect.top

    def animate(self, dt):
        # get state 
        if self.direction.x != 0:
            self.state = 'right' if self.direction.x > 0 else 'left'
        if self.direction.y != 0:
            self.state = 'down' if self.direction.y > 0 else 'up'

        # animate
        self.frame_index = self.frame_index + 5 * dt if self.direction else 0
        self.image = self.frames[self.state][int(self.frame_index) % len(self.frames[self.state])]

    def update(self, dt):
        self.input()
        self.move(dt)

