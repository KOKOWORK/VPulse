import pygame
import sys
from pygame.locals import *
from src import *
from src.img import *
from src.obj import *
from src.font import *
from random import *

screen=pygame.display.set_mode(GAME_SIZE)
indexbg=Image(MAIN_BG,0,(0,0),GAME_SIZE,0)
testobject=objectbase(TEST_OBJECT,0,(1400,410),(200,80),0)
testgif=objectbase(TEST_GIF,0,(650,300),(300,300),12)
welcome=doublefont("Hello World!",COLOR_TIANYI,COLOR_ALING,(0,0))
keycout=font(test_text,COLOR_TIANYI,(0,100))
nowbg=indexbg
fps_text=font(test_text,COLOR_ALING,(1300,0))
clock=pygame.time.Clock()

pygame.display.set_caption("Hello Wolrd!")

while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(COLOR_TIANYI)
    nowbg.draw(screen)
    testobject.update(-1,1)
    testobject.draw(screen)
    testgif.draw(screen)
    testgif.update(0,0)
    #welcome.update(0,0,randint(-1,1),randint(-1,1))
    welcome.draw(screen)

    keys=pygame.key.get_pressed()
    pressed_keys=[]  
    for key in range(len(pygame.key.get_pressed())):  
        if keys[key]:
            pressed_keys.append(pygame.key.name(key))
  
    if pressed_keys:
        keycout.text="You are pressing: "+' '.join(pressed_keys)
        keycout.pos=(0,100)
        keycout.draw(screen)

    if keys[pygame.K_UP]:
        keycout.text="UP"
        keycout.pos=(0,140)
        keycout.draw(screen)

    if keys[pygame.K_DOWN]:
        keycout.text="DOWN"
        keycout.pos=(0,180)
        keycout.draw(screen)

    if keys[pygame.K_LEFT]:
        keycout.text="LEFT"
        keycout.pos=(0,220)
        keycout.draw(screen)

    if keys[pygame.K_RIGHT]:
        keycout.text="RIGHT"
        keycout.pos=(0,260)
        keycout.draw(screen)

    if keys[pygame.K_KP_ENTER]:
        pygame.quit()
        sys.exit()
    
    fps=clock.get_fps()
    fps_text.text=f"FPS: {fps:.2f}"
    fps_text.draw(screen)

    pygame.display.flip()
    clock.tick(MAX_FPS)