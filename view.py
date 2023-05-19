import pygame


class View:
    def __init__(self, model, cell_size=10):
        self.model = model
        self.cell_size = cell_size
        self.width = self.model.width * self.cell_size
        self.height = self.model.height * self.cell_size

        pygame.init()
        self.screen = pygame.display.set_mode((self.width + 200, self.height))

        self.start_button = pygame.Rect(self.width + 20, 20, 160, 40)
        self.pause_button = pygame.Rect(self.width + 20, 80, 160, 40)

    def draw(self):
        self.screen.fill((0, 0, 0))  # Clear the screen
        font = pygame.font.Font(None, 24)
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
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button)  # Green for start
        pygame.draw.rect(self.screen, (255, 0, 0), self.pause_button)  # Red for pause
        self.screen.blit(font.render('Start', True, (0, 0, 0)), self.start_button.move(5, 5))
        self.screen.blit(font.render('Pause', True, (0, 0, 0)), self.pause_button.move(5, 5))

        for y in range(self.model.height):
            for x in range(self.model.width):
                cell = self.model.grid[x][y]
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size, self.cell_size, self.cell_size)
                if cell.is_alive:
                    if cell.is_ant:
                        color = (255, 0, 0)  # Drawing ants as red squares
                    elif cell.is_purple:
                        color = (128, 0, 128)  # Purple for square cells
                    else:
                        color = (255, 255, 255)  # White for alive cells
                else:
                    color = (0, 0, 0)
                pygame.draw.rect(self.screen, color, rect)

        pygame.display.flip()