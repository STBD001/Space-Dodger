import pygame
import random

pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Space Dodger")

white = (255, 255, 255)
black = (0, 0, 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("p1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width // 2, screen_height - 50)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= 5
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += 5

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("p2.jfif").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = -self.rect.height

    def update(self):
        self.rect.y += 5
        if self.rect.top > screen_height:
            self.kill()

player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
obstacles = pygame.sprite.Group()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if random.randint(1, 30) == 1:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    all_sprites.update()

    if pygame.sprite.spritecollideany(player, obstacles):
        running = False

    screen.fill(black)
    all_sprites.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)

pygame.quit()
