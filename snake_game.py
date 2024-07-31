import pygame

pygame.init()
blue = (50, 153, 213)
black = (0, 0, 0)
dis_width = 800
dis_height = 600

screen_dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 10

x1 = dis_width/2
y1 = dis_height/2
x1_change = y1_change = 0  # after change snake position variables
game_over = False
while not game_over:
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
    x1 += x1_change
    y1 += y1_change
    screen_dis.fill(blue)
    pygame.draw.rect(screen_dis, black, [x1, y1, snake_block, snake_block])
    pygame.display.update()
    clock.tick(snake_speed)
pygame.quit()
quit()
