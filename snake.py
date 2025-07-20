import pygame as pg
import random as rd


pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Snake Game")
playing = True

clock = pg.time.Clock()
#test_surface = pg.Surface((50,50))

x_pos = 300
y_pos = 200

snake = pg.Rect(x_pos,y_pos,50,50);

snake_color = (70,120,210)



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
        snake.y-= 5
        if snake.y >= 600 or snake.y <=0:
            snake.y = 200
            snake.x = 300
            up = False        
    elif down:
        snake.y += 5

        if snake.y >= 550 or snake.y <=0:
            snake.y = 200
            snake.x = 300
            down = False
    elif right:
        snake.x += 5

        if snake.x >= 750 or snake.x <= 0:
            snake.y = 200
            snake.x = 300
            right = False
    elif left:
        snake.x -= 5

        if snake.x >= 800 or snake.x <= 0:
            snake.y = 200
            snake.x = 300
            left = False


    
    
    pg.draw.rect(screen,snake_color,snake)



    pg.display.update()

   # test_surface.fill((70,120,210))
    clock.tick(60) # loop runs max 60 times in a sec 

