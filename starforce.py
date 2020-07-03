import pygame
import math
import random

pygame.init()
screen = pygame.display.set_mode((800,600))
background = pygame.image.load('bg.png')

pygame.display.set_caption("Star Force")
icon1 = pygame.image.load('rocket.png')
pygame.display.set_icon(icon1)

#Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX=10
textY=10

def show_score(x,y):
    score = font.render("Score: " + str(score_value),True,(255,255,255))
    screen.blit(score,(x,y))
# Player
player_image = pygame.image.load('space-invaders.png')
playerX=370
playerY=480
playerX_change = 0

# Enemy[
enemy_image = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6
for i in range(num_of_enemies):
    enemy_image.append(pygame.image.load('alien.png')) 
    enemyX .append (random.randint(0,735))
    enemyY .append (random.randint(50,150))
    enemyX_change .append (5)
    enemyY_change .append (40)

# Bullet
bullet_image = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player(x,y):
    screen.blit(player_image,(x,y))

def enemy(x,y,i):
    screen.blit(enemy_image[i],(x,y))

def bullet_fire(x,y):
    global bullet_state 
    bullet_state = "fire"
    screen.blit(bullet_image,(x+16,y+10))
    
def isCollusion(enemyX,enemyY,bulletX,bulletY) :
    distance = math.sqrt(math.pow(enemyX-bulletX,2)+math.pow(enemyY-bulletY,2))
    if distance < 27:
        return True
    else:
        return False

running = True
while running:
    screen.fill((0, 0, 0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                 playerX_change = -5
            if event.key == pygame.K_RIGHT:
                 playerX_change = 5
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                 bulletX = playerX
                 bullet_fire(bulletX,bulletY)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                 playerX_change = 0
           
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736 
    
    for i in range(num_of_enemies):
         enemyX[i] += enemyX_change[i]
         if enemyX[i] <= 0:
             enemyX_change[i] = 5
             enemyY[i] += enemyY_change[i]
         if enemyX[i] >= 736:
            enemyX_change[i] = -5
            enemyY[i] += enemyY_change[i]
         collision = isCollusion(enemyX[i],enemyY[i],bulletX,bulletY)
         if collision:
             bulletY = 480
             bullet_state = "ready"
             score_value += 10
             enemyX[i] = random.randint(0,735)
             enemyY[i] = random.randint(50,150)
         enemy(enemyX[i],enemyY[i],i)

    if bulletY <= 0 :
        bulletY = 480
        bullet_state = "ready"

    if bullet_state is "fire":
        bullet_fire(bulletX,bulletY)
        bulletY -=bulletY_change

    

    player(playerX,playerY)
    
    show_score(textX,textY)
    pygame.display.update()
    