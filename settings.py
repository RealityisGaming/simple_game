import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Fantasy Survival')
clock = pygame.time.Clock()

test_surface = pygame.image.load('NinjaAdventure')

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  # draw elements
  screen.blit(test_surface,(200,100))
  # update everything
  pygame.display.update()
  clock.tick(60)