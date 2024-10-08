import pygame
import math
from pygame.locals import*
import pymunk, pymunk.pygame_util
class basicfig(pygame.sprite.Sprite):
    def __init__(self, screen,space,pos=(100,100)):
        self.xpos =pos[0]
        self.ypos=pos[1]
        pygame.sprite.Sprite.__init__(self)
        self.screen=screen
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        self.image = pygame.image.load("assets/gamechar.png")
        self.rect = Rect(self.xpos, self.ypos, 80, 80)
        self.xchange=0
        self.ychange=0
        

        self.body = pymunk.Body(0, 0, pymunk.Body.STATIC)
        self.body.position = self.xpos,self.ypos
        #self.body.mass=10
        self.poly = pymunk.Poly.create_box(self.body,(80,80),0) # Create a box shape and attach to body
        self.poly.mass = 10              # Set the mass on the shape
        self.poly.elasticity=1
        self.poly.density=1
        space.add(self.body, self.poly)   
        self.poly.collision_type=2
        self.poly.body.position = self.xpos, self.ypos
        self.body.velocity = (self.xchange, self.ychange) 
    def update1(self,dt=.1,Normal=True):
        if math.sqrt(self.ychange**2+self.xchange**2)>15 and Normal==True:
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
        self.xpos=self.poly.body.position[0]
        self.ypos=self.poly.body.position[1]
        self.pos=pygame.Vector2(self.xpos, self.ypos)
        #self.poly.body.velocity=(self.xchange*18,self.ychange*18)
        self.rect = Rect(self.poly.body.position[0], self.poly.body.position[1], 80, 80)