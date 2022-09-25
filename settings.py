import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Fantasy Survival')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

score_surf = test_font.render('0', False, 'Red')
score_rect = score_surf.get_rect(topleft = (0, 0))


snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom = (600, 300))

player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect= player_surf.get_rect(bottomleft = (80,300))


while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
    # if event.type == pygame.MOUSEMOTION:
    #   if player_rect.collidepoint(event.pos): print('collision')
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_SPACE:
        print('jump')
    if event.type == pygame.KEYUP:
      print('unpressed')

  # draw elements
  screen.blit(sky_surface,(0,0))
  screen.blit(ground_surface,(0,300))


  pygame.draw.rect(screen, 'Pink', score_rect)
  screen.blit(score_surf,score_rect)


  snail_rect.right -= 4
  if snail_rect.right <=0: snail_rect.left = 800
  screen.blit(snail_surface, snail_rect)

  # player_rect.left += 1
  screen.blit(player_surf, player_rect)

  # keys = pygame.key.get_pressed()
  # if keys[pygame.K_SPACE]:
  #   print('jump')


  # # Collsion
  # if player_rect.colliderect(snail_rect):
  #   print('collision')
  # mouse_pos = pygame.mouse.get_pos()
  # if player_rect.collidepoint((mouse_pos)):
  #   print(pygame.mouse.get_pressed())
  


  # update everything
  pygame.display.update()
  clock.tick(60)