import pygame
import random
import sys
pygame.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Player and Enemy Collision Game")
WHITE = (255, 255, 255)
BLUE = (50, 50, 255)
RED = (255, 50, 50)
clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)
score = 0
font = pygame.font.SysFont(None, 36)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    player.update()
    hit_list = pygame.sprite.spritecollide(player, enemies, False)
    for enemy in hit_list:
        score += 1
        enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
        enemy.rect.y = random.randint(0, SCREEN_HEIGHT - enemy.rect.height)
    screen.fill(WHITE)
    all_sprites.draw(screen)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)