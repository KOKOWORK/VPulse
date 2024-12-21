import pygame
from pygame.locals import *
from . import *
import time

pygame.init()
ostream=pygame.font.Font(GAME_FONT,FONT_SIZE)

class font:
    def __init__(self,text,color,pos):
        self.text=text
        self.color=color
        self.pos=pos

    def draw(self,screen):
        cout_surface=ostream.render(self.text,True,self.color)
        cout_rect=self.pos
        screen.blit(cout_surface,self.pos)

    def update(self,color,movex,movey):
        if color!=0:
            self.color=color
        self.pos=(self.pos[0]+movex,self.pos[1]+movey)

class doublefont:
    def __init__(self,text,fcolor,bcolor,pos):
        self.word1=font(text,fcolor,(pos[0]+2,pos[1]+2))
        self.word2=font(text,bcolor,pos)

    def draw(self,screen):
        self.word1.draw(screen)
        self.word2.draw(screen)

    def update(self,fcolor,bcolor,movex,movey):
        self.word1.update(fcolor,movex,movey)
        self.word2.update(bcolor,movex,movey)