import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game display
width = 800
height = 600
game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Text Adventure Game")

# Load images
bedroom_image = pygame.image.load("bedroom.png")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define game variables
current_room = "start"  # Initial room

# Define the game loop
def game_loop():
    while True:
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the display
        game_display.fill(WHITE)

        # Draw text and other game elements
        if current_room == "start":
            # Draw the bedroom image
            # game_display.blit(bedroom_image, (0, 0))

            # Draw the text on the display
            font = pygame.font.Font(None, 30)
            text = font.render("You are in the bedroom.", True, BLACK)
            game_display.blit(text, (300, 400))

            # Add a caption for the start room
            caption = font.render("Welcome to the adventure!", True, BLACK)
            game_display.blit(caption, (20, 50))
        elif current_room == "door1":
            text = "You opened door 1. You entered a small library."
            # Draw the text on the display

        elif current_room == "door2":
            text = "You opened door 2. You found a treasure chest."
            # Draw the text on the display

        # Update the game display
        pygame.display.update()

# Start the game loop
game_loop()
