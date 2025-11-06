import pygame
import random
import sys
pygame.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Player and Enemy Collision Game")
background = pygame.image.load("background.jpg")
background = pygame.transform.scale(background, (screen_width, screen_height))
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
WHITE = (255, 255, 255)
player_image = pygame.Surface((50, 50))
player_image.fill((0, 255, 0)) 
player_rect = player_image.get_rect(center=(screen_width // 2, screen_height // 2))
enemies = []
for i in range(7):
    enemy = pygame.Surface((40, 40))
    enemy.fill((255, 0, 0))
    rect = enemy.get_rect(center=(random.randint(0, screen_width), random.randint(0, screen_height)))
    enemies.append(rect)
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player_rect.x += 5
    if keys[pygame.K_UP]:
        player_rect.y -= 5
    if keys[pygame.K_DOWN]:
        player_rect.y += 5
    for enemy in enemies:
        if player_rect.colliderect(enemy):
            score += 1
            enemy.x = random.randint(0, screen_width - 40)
            enemy.y = random.randint(0, screen_height - 40)
    screen.blit(background, (0, 0))
    screen.blit(player_image, player_rect)
    for enemy in enemies:
        pygame.draw.rect(screen, (255, 0, 0), enemy)
    score_text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
sys.exit()