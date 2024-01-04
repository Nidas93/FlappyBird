import pygame
import os

# pygame setup
pygame.init()
screen = pygame.display.set_mode((288, 512))
clock = pygame.time.Clock()
running = True

bg = pygame.image.load(os.path.join("assets/sprites", "background.png"))
# start_message = pygame.image.load(os.path.join("assets/sprites", "message.png"))

while running:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg, (0, 0))

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(120)  # set the FPS limit

pygame.quit()
