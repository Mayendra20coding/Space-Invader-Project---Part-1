import math
import random
import pygame
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 500
PLAYER_START_X = 370
PLAYER_START_Y = 380
ENMEY_START_Y_,MIN = 50
ENMEY_START_Y_,MAX = 150
ENMEY_SPEED_X = 4
ENMEY_SPEED_Y = 40
BULLET_SPEED_Y = 10
COLLISION_DISTANCE = 27
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('download.jpg')
pygame.display.set_icon(icon)
playerimg = pygame.image.load('download (1).jpg')
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change = 0
enmeyimg = []
enmeyx = []
enmeyy = []
enmeyx_change = []
enmeyy_change = []
num_of_enmey = 100
for i in range(num_of_enmey):
    enmeyimg.append(pygame.image.load('download.png'))
    enmeyx.append(random.randint(0, SCREEN_WIDTH - 64))
    enmeyy.append(random.randint(ENMEY_START_Y_,MIN, ENMEY_START_Y_,MAX))
    enmeyx_change.append(ENMEY_SPEED_X)
    enmeyy_change.append(ENMEY_SPEED_Y)
bulletimg = pygame.image.load('download (1).png')
bulletx = 0
bullety = PLAYER_START_Y
bulletx_change = 0
bullety_change = BULLET_SPEED_Y
bullet_state = "ready"
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textx = 10
texty = 10
over_font = pygame.font.Font('freesansbold.ttf', 64)
def show_score(x, y):
    score = font.render("Score : " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (200, 250))
def player(x, y):
    screen.blit(playerimg, (x, y))
def enmey(x, y, i):
    screen.blit(enmeyimg[i], (x, y))
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletimg, (x + 16, y + 10))
def is_collision(enmeyx, enmeyy, bulletx, bullety):
    distance = math.sqrt((enmeyx - bulletx)**2 +(enmeyy - bullety)**2)
    return distance < COLLISION_DISTANCE