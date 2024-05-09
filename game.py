import pygame
import sys
import os
import time
from pygame_gui import UIManager
from pygame_gui.elements import UIButton
from typing import List
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
hit_image = pygame.image.load('./src/other/hit.png').convert_alpha()
stand_image = pygame.image.load('./src/other/stand.png').convert_alpha()
double_image = pygame.image.load('./src/other/double.png').convert_alpha()

hit_image.set_colorkey(None)



# Scale the background image to fit the window size
background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

#seat default card placement
firstSeat = [int(SCREEN_WIDTH / 1.35), int(SCREEN_HEIGHT * 0.65), 45]
secondSeat = [int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT * 0.8), 0]
thirdSeat = [int(SCREEN_WIDTH / 3.7), int(SCREEN_HEIGHT * 0.65), -45]
dealerSeat = [int(SCREEN_WIDTH / 2.25), int(SCREEN_HEIGHT * 0.275), 0]

button_positions = [int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT / 2.5)]





# Load card image
cards = load_images_from_folder('./src/cards')

others = load_images_from_folder('./src/other/')


def append_card(seat, image: pygame.Surface, number: int):
    # Calculate scaling factor to maintain aspect ratio
    width = SCREEN_HEIGHT // 8
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
    screen.blit(rotated_image, image_rect)


#puts the buttons in the correct positions, adjusts depending on how many buttons are added
def show_buttons(buttons: List[pygame.Surface]):
    desired_height = SCREEN_HEIGHT // 7
    count = 0
    # Iterate over each button
    for button in buttons:
        original_width, original_height = button.get_size()
        new_width = int(original_width * (desired_height / original_height))
        scaled_button = pygame.transform.smoothscale(button, (new_width, desired_height))
        screen.blit(scaled_button, [button_positions[0] - (87*len(buttons)) + (count*200), button_positions[1]])
        count += 1


def show_background():
    screen.blit(pygame.transform.scale(others['table'], (SCREEN_WIDTH, SCREEN_HEIGHT)), (0, 0))


# Main loop
running = True
shoe = Shoe()
card = shoe.draw_card()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
     
    show_background()
    show_buttons([others['hit'], others['stand'], others['double']])
    append_card(secondSeat,cards[card['image']], 0)
    append_card(dealerSeat, cards['2oS'], 0) 
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()

