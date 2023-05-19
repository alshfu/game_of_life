# input_box.py
import pygame


class InputBox:
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)  # Create a rectangle for the input box
        self.color = pygame.Color('dodgerblue2')  # Color of the input box
        self.text = text  # Initial text of the input box
        self.font = pygame.font.Font(None, 32)  # Font for rendering text
        self.txt_surface = self.font.render(text, True, self.color)  # Surface for rendering text

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                print(self.text)  # Print the text when Enter is pressed
                self.text = ''  # Clear the text
            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]  # Remove the last character
            else:
                self.text += event.unicode  # Add the pressed character to the text
            self.txt_surface = self.font.render(self.text, True, self.color)  # Update the surface with the new text

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))  # Render the text on the screen
        pygame.draw.rect(screen, self.color, self.rect, 2)  # Draw the input box rectangle
