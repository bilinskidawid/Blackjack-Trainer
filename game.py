
import pygame
import sys
import os
import time
from pygame_gui import UIManager
from pygame_gui.elements import UIButton

from shoe import *
from hand import Hand

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)


def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            img = pygame.image.load(img_path).convert_alpha()  # Load image with alpha channel
            img.set_colorkey(None)  # remove borders around transparent pngs
            images.append(img)
    return images

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1800, 1100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load('./src/other/table.png').convert()

# Scale the background image to fit the window size
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#seat default card placement
firstSeat = [int(SCREEN_WIDTH / 1.35), int(SCREEN_HEIGHT * 0.65), 45]
secondSeat = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 0.8), 0]
thirdSeat = [int(SCREEN_WIDTH / 3.7), int(SCREEN_HEIGHT * 0.65), -45]
dealerSeat = [int(SCREEN_WIDTH / 2.25), int(SCREEN_HEIGHT * 0.275), 0]





# Load card image
cards = load_images_from_folder('./src/cards')


def append_card(seat, image: pygame.Surface, width: int):
    # Calculate scaling factor to maintain aspect ratio
    original_width, original_height = image.get_size()
    aspect_ratio = original_width / original_height
    new_height = int(width / aspect_ratio)
    # Resize the image
    image = pygame.transform.smoothscale(image, (width, new_height))
    # Rotate the image
    rotated_image = pygame.transform.rotate(image, seat[2]) 
    image_rect = rotated_image.get_rect()
    image_rect.centerx = seat[0]
    image_rect.bottom = seat[1]
    screen.blit(rotated_image, image_rect)


# Main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    screen.blit(background_image, (0, 0))
    
    # Add card to the specific coordinate with custom width (e.g., 175 pixels)
    append_card(firstSeat,cards[0], 125)
    append_card(secondSeat,cards[1], 125)
    append_card(thirdSeat, cards[2], 125)
    append_card(dealerSeat, cards[3], 125) 
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

