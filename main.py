import pygame
import math
import pymunk, pymunk.pygame_util

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt=.1

space = pymunk.Space()
space.gravity = (0,900)

from charactarlev import charactar
from basicfig import basicfig
player=charactar(screen,space)
bush=basicfig(screen,space)
bush2=basicfig(screen,space,(100,500))
entities = pygame.sprite.Group()
entities.add(player)
entities.add(bush)
entities.add(bush2)

handler=space.add_collision_handler(1,2)
print(bush.poly.body.position)
def collide(arbiter,space,data):
    #print("hello")
    player.xchange=-player.xchange*2
    player.ychange= -player.ychange*2
    return(False)
def Resetpostcollision(arbiter,space,data):
    player.xchange= 0
    player.ychange= 0
    print(arbiter)
    #print("true")
    return True
def presolve(arbiter,space,data):
    #print("yo")
    #print(handler._get_post_solve)
    player.xchange=-player.xchange*3
    player.ychange= -player.ychange*3
    return True
handler.begin=collide
handler.separate=Resetpostcollision
#handler.pre_solve=presolve
x=1
print(-x)
while running:
    screen.fill("green")
    space.step(0.02)
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
    bush.update1(dt)
    bush2.update1(dt)
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
    dt= clock.tick(60)/500  # limits FPS to 60
    #if math.sqrt(player.ychange**2+player.xchange**2)>0a:
        #print(math.sqrt(player.ychange**2+player.xchange**2))




pygame.quit()



