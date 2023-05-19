# view.py
import pygame
from config import CELL_SIZE


class View:
    def __init__(self, model, cell_size=CELL_SIZE):
        self.model = model  # Reference to the model
        self.controller = None  # Reference to the controller
        self.cell_size = cell_size  # Size of each cell
        self.width = self.model.width * self.cell_size  # Width of the view
        self.height = self.model.height * self.cell_size  # Height of the view

        pygame.init()  # Initialize Pygame
        self.screen = pygame.display.set_mode((self.width + 200, self.height))  # Create the screen

        self.start_button = pygame.Rect(self.width + 20, 20, 160, 40)  # Start button rectangle
        self.pause_button = pygame.Rect(self.width + 20, 80, 160, 40)  # Pause button rectangle

    def set_controller(self, controller):
        self.controller = controller  # Set the controller for the view

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        font = pygame.font.Font(None, 24)  # Create a font object

        # Render and display information texts
        texts = [
            f'Alive cells: {self.model.alive_cells}',
            f'Dead cells: {self.model.dead_cells}',
            f'Ants: {self.model.ants}',
            f'Steps: {self.model.steps}',
        ]
        for i, text in enumerate(texts):
            text_img = font.render(text, True, (255, 255, 255))
            self.screen.blit(text_img, (self.width + 30, i * 30 + 120))

        # Draw the buttons
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)  # Green for start button
        pygame.draw.rect(self.screen, (255, 0, 0), self.pause_button)  # Red for pause button
        self.screen.blit(font.render('Start', True, (0, 0, 0)), self.start_button.move(5, 5))
        self.screen.blit(font.render('Pause', True, (0, 0, 0)), self.pause_button.move(5, 5))

        for y in range(self.model.height):
            for x in range(self.model.width):
                cell = self.model.grid[x][y]  # Get the cell at the current position
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)  # Create a rectangle for the cell

                if cell.is_alive:
                    color = (255, 255, 255)  # White for alive cells
                else:
                    color = (0, 0, 0)  # Black for dead cells

                pygame.draw.rect(self.screen, color, rect)  # Draw the cell

        pygame.display.flip()  # Update the display