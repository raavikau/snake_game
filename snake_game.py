import pygame
pygame.init()
dis_width = 800
dis_height = 600

screen_dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake game')
game_over =False
while not game_over:
    for event in pygame.event.get():  # prints out all the actions that take place on the screen with event.get()
        print(event)
pygame.quit()
quit()
