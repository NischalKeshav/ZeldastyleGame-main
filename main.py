import pygame
import math


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=.1
from charactarlev import charactar
from basicfig import basicfig
player=charactar(screen)
bush=basicfig(screen,80,80)
entities = pygame.sprite.Group()
entities.add(player)
entities.add(bush)

while running:
    screen.fill("green")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player.xchange<0:
                  player.xchange=0
            if event.key == pygame.K_d and player.xchange>0:
                  player.xchange=0
            if event.key == pygame.K_w and player.ychange<0:
                  player.ychange=0
            if event.key == pygame.K_s and player.ychange>0:
                  player.ychange=0




    #pygame.draw.circle(screen, "red", pygame.Vector2(player.xpos,player.ypos), 40)
    player.update1(dt)

    entities.update()#update sprite
    entities.draw(screen)#update sprite
    pygame.display.flip()#update sprite

    keys =pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player.ychange = -400 * dt
    if keys[pygame.K_s]:
        player.ychange= 400 * dt
    if keys[pygame.K_a]:
        player.xchange= -400 * dt
    if keys[pygame.K_d]:
        player.xchange= 400 * dt
    dt= clock.tick(60)/1000  # limits FPS to 60




pygame.quit()



