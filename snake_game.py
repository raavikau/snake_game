import pygame
import random
pygame.init()
white = (255, 255, 255)
blue = (50, 153, 213)
black = (0, 0, 0)
red = (255, 0, 0)
dis_width = 800
dis_height = 600

screen_dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10
font_style = pygame.font.SysFont(None, 30)

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen_dis.blit(mesg, [dis_width/4, dis_height/3])  # blit it to a specific position on the display surface

def our_score(score):
    val = font_style.render("Your Score: " + str(score), True, red)
    screen_dis.blit(val, [10, 10])

def our_snake(snake_blocks, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen_dis, white, [x[0], x[1], snake_blocks, snake_blocks])

def game_loop():
    game_over = False
    game_close = False
    x1 = dis_width / 2  # starting position of snake
    y1 = dis_height / 2
    length_snake = 1
    snake_list = []
    x1_change = y1_change = 0  # after change snake position variables
    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0  # generate initial food position
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0  # rounding to ensure the food appears on a grid aligned to 10px
    while not game_over:
        while game_close:
            screen_dis.fill(blue)
            message("You lost! press Q-quit or C-play again", red)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_close = False
                        game_over = True
                    if event.key == pygame.K_c:
                        game_loop()
        for event in pygame.event.get():  # prints out all the actions that take place on the screen with event.get()
            if event.type == pygame.QUIT:  # if click on the close button
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    x1_change = 0
                    y1_change = -snake_block
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    x1_change = 0
                    y1_change = snake_block
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:  # if snake hit the boundaries
            game_close = True
        x1 += x1_change
        y1 += y1_change
        screen_dis.fill(blue)
        pygame.draw.rect(screen_dis, red, [food_x, food_y, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > length_snake:  # if snake_list exceed length of snake then tail is removed
            del snake_list[0]
        for x in snake_list[:-1]:  # check the collision with itself
            if x == snake_head:
                game_close = True
        our_snake(snake_block, snake_list)  # draw snake on screen
        our_score(length_snake - 1)
        pygame.display.update()
        if x1== food_x and y1 == food_y:
            food_x = round(random.randrange(dis_width-snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(dis_height-snake_block) / 10.0) * 10.0
            length_snake += 1
        clock.tick(snake_speed)
    pygame.quit()
    quit()
game_loop()
