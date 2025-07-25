import pygame as pg
import random as rd

ct=0
pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Snake Game")
playing = True

clock = pg.time.Clock()
#test_surface = pg.Surface((50,50))

x_pos = 300
y_pos = 200

block_size = 50

snake_rect = pg.Rect(x_pos,y_pos,50,50);         #x_pos and y_pos are the coordinates and 50 - 50 are the size
food_color = (170,70,30)
snake_color = (70,120,210)
global food
food = None 

def random_x():
    x_cord = rd.randrange(0,751,5)
    return x_cord

def random_y():
    y_cord = rd.randrange(0,551,5)
    return y_cord

ini = 0
left=right=up=down = False
bg_color = (175,215,70)
snake = [snake_rect]
pg.draw.rect(screen,snake_color,snake[0])
growing = False

while playing:
    screen.fill(bg_color)
    if ini==0:
        pg.draw.rect(screen,snake_color,snake[0])

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_DOWN:
                down = True
                left = right = up = False
            elif event.key == pg.K_UP:
                up = True
                down = right = left = False
            elif event.key == pg.K_RIGHT:
                right = True
                left = up = down = False
            elif event.key == pg.K_LEFT:
                left = True
                right = up = down = False



    
    new_head = snake[0].copy()
    snake.insert(0,new_head)
    if up:
            
        if not growing:
           snake.pop()
           for i in snake:
               i.y-=block_size
               pg.draw.rect(screen,snake_color,i)
        else:
            for i in snake:
                i.y-=block_size
                pg.draw.rect(screen,snake_color,i)

    elif down:
        if not growing:
            snake.pop()
            for i in snake:
                i.y+=block_size
                pg.draw.rect(screen,snake_color,i)
        else:
            for i in snake:
                i.y+=block_size
                pg.draw.rect(screen,snake_color,i)


    
    pg.display.update()
    clock.tick(6)







