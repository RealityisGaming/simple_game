import pygame
from sys import exit


def display_score():
  current_score = int(pygame.time.get_ticks() / 1000) - start_time
  score_surf = text_font.render(F'Score: {current_score}', False, (60,60,60))
  score_rect = score_surf.get_rect(center = (400,50))
  screen.blit(score_surf, score_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Fantasy Survival')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
game_active = True
start_time = 0

sky_surface = pygame.image.load('graphics\Sky.png').convert()
ground_surface = pygame.image.load('graphics\ground.png').convert()

# score_surf = text_font.render('0', False, 'Red')
# score_rect = score_surf.get_rect(topleft = (0, 0))

# Snail
# snail_surface = pygame.image.load('graphics\snail\snail1.png').convert_alpha()
# snail_rect = snail_surface.get_rect(midbottom = (600, 300))

# Player
player_surf = pygame.image.load('graphics\Player\player_walk_1.png').convert_alpha()
player_rect= player_surf.get_rect(bottomleft = (80,300))
player_gravity = 0
player_stand = pygame.image.load('graphics\Player\player_stand.png').convert_alpha()
player_stand_rect = player_stand.get_rect(bottomleft = (80,300))


while True:

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      exit()
  # Motion
    if game_active:

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
          player_gravity = -20

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT and player_rect.bottom >= 300:
          player_rect.bottom.x += 20
    else:
      if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
        game_active = True
        snail_rect.left = 800
        start_time = int(pygame.time.get_ticks() / 1000)

  # Elements
  if game_active:
    screen.blit(sky_surface,(0,0))
    screen.blit(ground_surface,(0,300))
    # pygame.draw.rect(screen, 'Pink', score_rect)
    # screen.blit(score_surf,score_rect)
    display_score()

  # Snail
    # snail_rect.right -= 4
    # if snail_rect.right <=0: snail_rect.left = 800
    # screen.blit(snail_surface, snail_rect)

  # Player
    player_gravity += 1
    player_rect.y += player_gravity
    if player_rect.bottom >= 300:
      player_rect.bottom = 300
    
    screen.blit(player_surf, player_rect)

    # # Collsion
    # if snail_rect.colliderect(player_rect):
    #   game_active = False
  else:
    screen.fill((94,129,162))
    screen.blit(player_stand, player_stand_rect)


  # update everything
  pygame.display.update()
  clock.tick(60)