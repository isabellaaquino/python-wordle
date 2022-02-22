import os
import pygame
import grid

# Set - ups

SRC_PATH = 'C:/Users/Isabe/Desktop/ead/wordle/src/'

ICON = pygame.image.load(os.path.join(SRC_PATH + 'yellow', 'YELLOW_W.png'))

DEFAULT = pygame.image.load(os.path.join(SRC_PATH + 'grey', 'GREY_0.png'))

pygame.display.set_caption("WORDLE")
pygame.display.set_icon(ICON)

# Variables 

WIDTH, HEIGHT = 1280, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
WIN_FILL = (45, 48, 71)

FPS = 60

def draw_window():
    WIN.fill(WIN_FILL)
    grid.draw_firstGrid(WIN, DEFAULT)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window()
    pygame.quit()

if __name__ == "__main__":
    main()