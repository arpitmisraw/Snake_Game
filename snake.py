import pygame
import random

pygame.init()

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
display_width = 800
display_height = 600

game_display = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Snake Game')
clock = pygame.time.Clock()
fps = 15

def game_quit():
    pygame.quit()
    quit()


def display_snake(snake,block_size):
    for i in range(len(snake)):
        if i==0:
            pygame.draw.rect(game_display,red,[snake[i][0],snake[i][1],block_size,block_size])
        else:
            snake[i]=snake[i-1]
            pygame.draw.rect(game_display,red,[snake[i][0],snake[i][1],block_size,block_size])

def display_apple(apple_x,apple_y,block_size):
    pygame.draw.rect(game_display,green,[apple_x,apple_y,block_size,block_size])

def display_message(text,size,color):
    font = pygame.font.Font('freesansbold.ttf',size)
    game_display.blit(font.render(text,True,color),((display_width/2)-150,(display_height/2)-50))
    

def game_loop():
    game_over = False
    game_choice = False 
    block_size = 10
    snake=list()
    x = display_width/2
    y = display_height/2
    snake.append([x,y])
    x_change = 0
    y_change = 0
    apple_x = round(random.randrange(display_width-block_size)/10)*10
    apple_y = round(random.randrange(display_height-block_size)/10)*10
    snake_speed = block_size
    while not game_over:
        while game_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        game_quit()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    y_change = 0
                    x_change = -1*snake_speed
                elif event.key == pygame.K_RIGHT:
                    y_change = 0
                    x_change = snake_speed
                elif event.key == pygame.K_UP:
                    x_change = 0
                    y_change = -1*snake_speed
                elif event.key == pygame.K_DOWN:
                    x_change = 0
                    y_change = snake_speed
        
        snake[0][0]+=x_change
        snake[0][1]+=y_change
        game_display.fill(white)
        display_snake(snake,block_size)
        display_apple(apple_x,apple_y,block_size)
        if apple_x == snake[0][0] and apple_y == snake[0][1]:
            apple_x = round(random.randrange(display_width-block_size)/10)*10
            apple_y = round(random.randrange(display_height-block_size)/10)*10
        if snake[0][0]>display_width:
            snake[0][0]=0
        if snake[0][0]+block_size<0:
            snake[0][0]=display_width
        if snake[0][1]>display_height:
            snake[0][1]=0
        if snake[0][1]+block_size<0:
            snake[0][1]=display_height
            
        clock.tick(fps)
        pygame.display.update()
game_loop()
    