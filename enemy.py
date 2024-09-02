from charactarlev import charactar
import pygame
import math
from pygame.locals import*
class enemy(charactar):
    def __init__(self,space,screen,handler,tuple,):
        charactar.__init__(self,screen,space,handler,tuple)
        print("b")
        self.xpos=tuple[0]
        self.ypos=tuple[1]
        self.poly.collision_type=2
        self.poly.body.velocity=(-30,0)
        self.xchange=-30
        self.ychange=0
        print(self.xpos)
    def update1(self,Normal=True):
        if math.sqrt(self.ychange**2+self.xchange**2)>15 and Normal==True:
            self.xchange= math.sqrt(2)*self.xchange/2
            self.ychange= math.sqrt(2)*self.ychange/2
        if self.xpos<0 and self.xchange<0:
             #self.xpos=45
             self.xchange=-self.xchange
        elif self.xpos>1200 and self.xchange>0:
             #self.xpos=1275
             self.xchange=-self.xchange
        if self.ypos<0 and self.ychange<0:
             #self.xpos=45
             self.ychange= -self.ychange
        elif self.ypos>640 and self.ychange>0:
             #self.xpos=45
             self.ychange= -self.ychange
      
        self.poly.body.velocity=(self.xchange*18,self.ychange*18)
        #self.xpos=self.poly.body.position[0]
        #self.ypos=self.poly.body.position[1]
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        #self.poly.body.velocity=(self.xchange*18,self.ychange*18)
        self.rect = Rect(2*(math.floor((self.poly.body.position[0])/2)), self.poly.body.position[1], 80, 80)
        self.xpos=self.poly.body.position[0]
        self.ypos=self.poly.body.position[1]
        #print((self.poly.body.position[0], self.poly.body.position[1]))
        #elf.update()
        #self.draw(self.screen)
        #pygame.draw.circle(self.screen, "red", pygame.Vector2(self.xpos,self.ypos), 40)

