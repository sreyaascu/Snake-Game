import pygame as pg
import random as rd


pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Snake Game")
playing = True

clock = pg.time.Clock()
test_surface = pg.Surface((50,50))
x_pos = 300
y_pos = 200




left=right=up=down = False


while playing:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_UP:
                up = True
                down=right=left = False
            elif event.key == pg.K_DOWN:
                down = True
                up=left=right = False
            elif event.key == pg.K_LEFT:
                left = True
                down=up=right = False
            elif event.key == pg.K_RIGHT:
                right = True
                left=down=up = False

#Screen dimensions : (800,600)
            
    screen.fill((175,215,70))
        
    if up:
        y_pos -= 5
        if y_pos >= 600 or y_pos <=0:
            y_pos = 200
            x_pos = 300
            up = False        
    elif down:
        y_pos += 5

        if y_pos >= 550 or y_pos <=0:
            y_pos = 200
            x_pos = 300
            down = False
    elif right:
        x_pos += 5

        if x_pos >= 750 or x_pos<=0:
            y_pos = 200
            x_pos = 300
            right = False
    elif left:
        x_pos -= 5

        if x_pos >= 800 or x_pos<=0:
            y_pos = 200
            x_pos = 300
            left = False



    screen.blit(test_surface,(x_pos,y_pos))
    




    pg.display.update()

    test_surface.fill((70,120,210))
    clock.tick(60) # loop runs max 60 times in a sec 

