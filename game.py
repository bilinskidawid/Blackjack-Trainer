
import pygame
import sys

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
CARD_WIDTH, CARD_HEIGHT = 100, 150  # Adjust the card size
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

card_image = pygame.transform.scale(pygame.image.load('card.png'), (CARD_WIDTH, CARD_HEIGHT))  # Scale the card image

class Card(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = card_image
        self.rect = self.image.get_rect(center=pos)
        self.angle = 0
        self.flip_frames = 10
        self.flipping = False
        self.original_image = self.image  # Store the original image for flipping

    def flip(self):
        self.flipping = True

    def update(self):
        if self.flipping:
            self.angle += 180 / self.flip_frames
            if self.angle >= 90:  # Change angle condition to 90 for folding sideways
                self.flipping = False
                self.angle = 0
                self.image = pygame.transform.flip(self.original_image, True, False)  # Flip horizontally
        self.image = pygame.transform.rotate(self.original_image, self.angle)

all_sprites = pygame.sprite.Group()
card = Card((WINDOW_WIDTH//2, WINDOW_HEIGHT//2))
all_sprites.add(card)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                card.flip()

    all_sprites.update()

    screen.fill((255, 255, 255))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(30)

pygame.quit()
sys.exit()

