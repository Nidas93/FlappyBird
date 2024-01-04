import pygame
import os, sys

# pygame setup
pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
pygame.display.set_caption("Flappy Bird")

bg = pygame.image.load(os.path.join("assets/sprites", "background.png")).convert()
start_message = pygame.image.load(os.path.join("assets/sprites", "message.png"))
floor_surface = pygame.image.load(os.path.join("assets/sprites", "floor.png"))

pip_pos_x = 288
botten_pipe_surface = pygame.image.load(
    os.path.join("assets/sprites", "pipe-green.png")
)
botten_pipe_surface_rect = botten_pipe_surface.get_rect(topleft=(pip_pos_x, 350))

top_pipe_surface = pygame.transform.rotate(botten_pipe_surface, 180)
top_pipe_surface_rect = top_pipe_surface.get_rect(topleft=(pip_pos_x, -100))

player_surf = pygame.image.load(
    os.path.join("assets/sprites", "redbird-downflap.png")
).convert_alpha()
player_rect = player_surf.get_rect(topleft=(125, 270))

start_game = False
end_game = False

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # if start_game == False and event.type == pygame.

    # blit = block image transfer
    screen.blit(bg, (0, 0))
    screen.blit(floor_surface, (0, 400))
    screen.blit(start_message, (50, 100))

    screen.blit(player_surf, player_rect)

    top_pipe_surface_rect.x -= 1
    botten_pipe_surface_rect.x -= 1
    screen.blit(botten_pipe_surface, botten_pipe_surface_rect)
    screen.blit(top_pipe_surface, top_pipe_surface_rect)

    if player_rect.colliderect(botten_pipe_surface_rect) or player_rect.colliderect(
        top_pipe_surface_rect
    ):
        end_game = True
        # print game over

    if pip_pos_x < -50:
        # Also randomize a new y pos value
        botten_pipe_surface_rect.x = pip_pos_x
        top_pipe_surface_rect.x = pip_pos_x

    pygame.display.update()

    clock.tick(60)  # set the FPS limit
