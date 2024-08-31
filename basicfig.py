import pygame
import math
from pygame.locals import*
import pymunk, pymunk.pygame_util
class basicfig(pygame.sprite.Sprite):
    def __init__(self, screen,space,l,w,orgposition=True,img=True):
        self.xpos =200
        self.ypos=200
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        self.image = pygame.image.load("assets/gamechar.png")
        self.rect = Rect(self.xpos, self.ypos, l,w)
        self.xchange=0
        self.ychange=0
    def update1(self,dt=.1,Normal=True):
        self.xpos+= self.xchange
        self.ypos+=self.ychange
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        self.rect = Rect(self.xpos, self.ypos, 80, 80)
        #elf.update()
        #self.draw(self.screen)
        #pygame.draw.circle(self.screen, "red", pygame.Vector2(self.xpos,self.ypos), 40)
