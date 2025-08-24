import pygame as pg
import random as rd

pg.init()
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Snake Game")
playing = True

clock = pg.time.Clock()
#test_surface = pg.Surface((50,50))
ct = 0
x_pos = 300
y_pos = 200
f_x = 500
f_y = 100
bs = 50
grad = 40

food = pg.Rect(f_x,f_y,bs,bs)
snake_rect = pg.Rect(x_pos,y_pos,50,50);         #x_pos and y_pos are the coordinates and 50 - 50 are the size
food_color = (170,70,30)
snake_color = (30,grad,255)

food_ini = True

def random_x():
    x_cord = rd.randrange(0,751,50)
    return x_cord

def random_y():
    y_cord = rd.randrange(0,551,50)
    return y_cord


left=right=up=down = False
bg_color = (175,215,70)
snake = [snake_rect]
growing = False
moving = False
while playing:
    screen.fill(bg_color)
    grad = 40
    if food_ini:
        pg.draw.rect(screen,food_color,food)
        ct=1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            playing = False
        elif event.type == pg.KEYDOWN:

            if event.key == pg.K_DOWN:
                if up==True:
                    continue
                elif up==False:
                    down = True
                    left=up=right = False
                    moving = True 
            elif event.key == pg.K_UP:
                if down==False:
                    up = True
                    moving = True
                    down = right = left = False
                elif down==True:
                    continue
            elif event.key == pg.K_RIGHT:
                if left==True:
                    continue
                elif left==False:
                    right = True
                    up=down=left = False
                    moving = True
            elif event.key == pg.K_LEFT:
                if right == False:
                    left = True
                    moving = True
                    right = up = down = False
                elif right == True:
                    continue


    if moving:
        if up:
            new_head = snake[0].copy()
            new_head.y -= bs
            snake.insert(0,new_head)

            if not snake[0].colliderect(food):
                snake.pop()
            else:
                food_ini = False
                food = pg.Rect(random_x(),random_y(),50,50)
                food_ini = True
            for i in snake:
                snake_color = (30,grad,255) 
                pg.draw.rect(screen,snake_color,i)
                grad += 5 



        elif down:
            new_head = snake[0].copy()
            new_head.y += bs
            snake.insert(0,new_head)
            if not snake[0].colliderect(food):

                snake.pop()
                
            else:
                food_ini = False
                food = pg.Rect(random_x(),random_y(),50,50)
                food_ini = True
            for i in snake:
                snake_color = (30,grad,255) 
                pg.draw.rect(screen,snake_color,i)
                grad += 5
        
        elif right:
            
            new_head = snake[0].copy()
            new_head.x += bs
            snake.insert(0,new_head)
            
            if not snake[0].colliderect(food):

                snake.pop()

            else:
                food_ini = False
                food = pg.Rect(random_x(),random_y(),50,50)
                food_ini = True

            for i in snake:
                snake_color = (30,grad,255) 
                pg.draw.rect(screen,snake_color,i)
                grad += 5
        
        elif left:

            new_head = snake[0].copy()
            new_head.x -= bs
            snake.insert(0,new_head)
            
            if not snake[0].colliderect(food):
                snake.pop()

            else:
                food_ini = False

                food = pg.Rect(random_x(),random_y(),50,50)
                food_ini = True
            for i in snake:
                snake_color = (30,grad,255) 
                pg.draw.rect(screen,snake_color,i)
                grad += 5 



    else:
        grad = 40
        snake_color = (30,40,255)
        pg.draw.rect(screen,snake_color,snake[0])
    
    if ((snake[0].x > 750) or (snake[0].x < 0)) or ((snake[0].y ) > 550 or (snake[0].y < 0)):

        while (len(snake)==1):
            snake.pop()
        snake_rect = pg.Rect(x_pos,y_pos,50,50)
        snake = [snake_rect]
        up=right=down=left = False
        moving = False

    pg.display.update()

    clock.tick(7)






