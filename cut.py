
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
    images_dict = {}
    for filename in os.listdir(folder):
        img_path = os.path.join(folder, filename)
        if os.path.isfile(img_path):
            img = pygame.image.load(img_path).convert_alpha()  # Load image with alpha channel
            img.set_colorkey(None)  # remove borders around transparent pngs
            key = os.path.splitext(filename)[0]  # Remove file extension
            images_dict[key] = img
    return images_dict

# Initialize Pygame
pygame.init()

# Set up the screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1800, 1100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
background_image = pygame.image.load('./src/other/table.png').convert()

# Scale the background image to fit the window size
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

# seat default card placement
firstSeat = [int(SCREEN_WIDTH / 1.35), int(SCREEN_HEIGHT * 0.65), 45]
secondSeat = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 0.8), 0]
thirdSeat = [int(SCREEN_WIDTH / 3.7), int(SCREEN_HEIGHT * 0.65), -45]
dealerSeat = [int(SCREEN_WIDTH / 2.25), int(SCREEN_HEIGHT * 0.275), 0]

# Load card image
cards = load_images_from_folder('./src/cards')

def append_card(seat, image: pygame.Surface, width: int, number: int):
    # Calculate scaling factor to maintain aspect ratio
    original_width, original_height = image.get_size()
    aspect_ratio = original_width / original_height
    new_height = int(width / aspect_ratio)
    # Resize the image
    image = pygame.transform.smoothscale(image, (width, new_height))
    # Rotate the image
    rotated_image = pygame.transform.rotate(image, seat[2]) 
    image_rect = rotated_image.get_rect()
    image_rect.centerx = seat[0] + int(0.3*width*number)
    image_rect.bottom = seat[1] - int(0.3*new_height*number)
    return rotated_image, image_rect

# Main loop
running = True
first = True
shoe = Shoe()
card = shoe.draw_card()['image']
dealer = shoe.draw_card()['image']

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button click
            if second_seat_image_rect.collidepoint(event.pos):  # Check if the click is within the second seat image rect
                screen.blit(background_image, (0, 0))
                card = shoe.draw_card()['image']
                new_card_image, new_card_rect = append_card(secondSeat, cards[card], 125, 0)
                screen.blit(new_card_image, new_card_rect)
                append_card(dealerSeat, cards['2oS'], 125, 0)
                pygame.display.flip()

    screen.blit(background_image, (0, 0))
    
    # Add card to the specific coordinate with custom width (e.g., 175 pixels)
    second_seat_image, second_seat_image_rect = append_card(secondSeat, cards[card], 125, 0)
    screen.blit(second_seat_image, second_seat_image_rect) 
    append_card(dealerSeat, cards['2oS'], 125, 0)

    
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

