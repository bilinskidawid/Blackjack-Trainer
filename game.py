
import pygame
import sys


#import pygame

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1800,1100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load('./images/table.png').convert()

# Scale the background image to fit the window size
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))
# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_image, (0, 0))
    
    # Draw all cards
    card = pygame.image.load('./images/AoD.png')
    screen.blit(card, (100, 20)) 
    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()

