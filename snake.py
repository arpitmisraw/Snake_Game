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
    for snake_block in snake:
        pygame.draw.rect(game_display,red,[snake_block[0],snake_block[1],block_size,block_size])

def display_apple(apple_x,apple_y,block_size):
    pygame.draw.rect(game_display,green,[apple_x,apple_y,block_size,block_size])

def display_message(text,size,color):
    font = pygame.font.Font('freesansbold.ttf',size)
    game_display.blit(font.render(text,True,color),((display_width/2)-150,(display_height/2)-50))
    

def game_loop():

    #Initial declarations
    game_over = False
    game_choice = False 
    block_size = 20
    snake=list()
    x = display_width/2
    y = display_height/2
    snake.append([x,y])
    x_change = 0
    y_change = 0
    apple_x = round(random.randrange(block_size,display_width-2*block_size)/20)*20
    apple_y = round(random.randrange(block_size,display_height-2*block_size)/20)*20
    snake_speed = block_size
    count = 0

    #Till the game is not over 
    while not game_over:

        tail = len(snake)   

        #choice to continue
        while game_choice:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_ESCAPE:
                        game_quit()

        #To get the event.type
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
        
        
        game_display.fill(white)        #Fill the gameboard white

        #Change the position of apple and increase the length if the snake
        if apple_x == snake[0][0] and apple_y == snake[0][1]:
            apple_x = round(random.randrange(block_size,display_width-block_size)/20)*20
            apple_y = round(random.randrange(block_size,display_height-block_size)/20)*20
            temp=[[snake[tail-1][0],snake[tail-1][1]]]
            snake+=temp
        
        tail = len(snake)       #Update length of the tail

        #Update the position of all blocks of the snake
        for i in range(tail-1,0,-1):
            snake[i][0]=snake[i-1][0]
            snake[i][1]=snake[i-1][1]
        

        #Update the position of the head of the snake
        snake[0][0]+=x_change
        snake[0][1]+=y_change


        #Display the snake and the apple
        display_snake(snake,block_size)
        display_apple(apple_x,apple_y,block_size)
        
        
        #Boundary Conditions
        if snake[0][0] == display_width:
            snake[0][0]=0
        if snake[0][0]<0:
            snake[0][0]=display_width
        if snake[0][1] == display_height:
            snake[0][1]=0
        if snake[0][1]<0:
            snake[0][1]=display_height
            
        clock.tick(fps)     #FPS
        pygame.display.update()     #Updates the complete display
game_loop()
    