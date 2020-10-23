import sys
import pygame
from setting import Setting

bg_color = (230, 230, 230)
def run_game():
#   pygame.init()
    ai_setting = Setting()

    screen = pygame.display.set_mode((ai_setting.screen_width , 800))
    pygame.display.set_caption("Alien Invision")

    # start main procedure
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill(bg_color)
        pygame.display.flip()
run_game()