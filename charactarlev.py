import pygame
import math
from pygame.locals import*
class charactar(pygame.sprite.Sprite):
    def __init__(self, screen):
        self.xpos =640
        self.ypos=360
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        self.image = pygame.image.load("assets/gamechar.png")
        self.rect = Rect(self.xpos, self.ypos, 80, 80)
        self.xchange=0
        self.ychange=0
    def update1(self,dt=.1,Normal=True):
        if math.sqrt(self.ychange**2+self.xchange**2)>(7) and Normal==True:
            self.xchange= math.sqrt(2)*self.xchange/2
            self.ychange= math.sqrt(2)*self.ychange/2
        if self.xpos<0 and self.xchange<0:
             #self.xpos=45
             self.xchange=0
        elif self.xpos>1200 and self.xchange>0:
             #self.xpos=1275
             self.xchange=0
        if self.ypos<0 and self.ychange<0:
             #self.xpos=45
             self.ychange=0
        elif self.ypos>640 and self.ychange>0:
             #self.xpos=45
             self.ychange=0
        self.xpos+= self.xchange
        self.ypos+=self.ychange
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        self.rect = Rect(self.xpos, self.ypos, 80, 80)
        #elf.update()
        #self.draw(self.screen)
        #pygame.draw.circle(self.screen, "red", pygame.Vector2(self.xpos,self.ypos), 40)
