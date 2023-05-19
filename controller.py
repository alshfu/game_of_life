# controller.py
import pygame
from view.input_box import InputBox


class Controller:
    def __init__(self, model, view):
        self.model = model  # Reference to the model
        self.view = view  # Reference to the view
        self.running = True  # Flag indicating whether the simulation is running or paused
        self.input_boxes = [
            InputBox(self.view.width + 30, 350, 100, 32),  # Input box for BIRTH_NEIGHBOURS
            InputBox(self.view.width + 30, 400, 100, 32),  # Input box for SURVIVE_NEIGHBOURS
            InputBox(self.view.width + 30, 550, 100, 32),  # Input box for ANT_NEIGHBOURS
            InputBox(self.view.width + 30, 600, 100, 32),  # Input box for PURPLE_STEPS
        ]

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False  # Quit the simulation if the window is closed
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.view.start_button.collidepoint(event.pos):
                self.running = True  # Start the simulation if the start button is clicked
            elif self.view.pause_button.collidepoint(event.pos):
                self.running = False  # Pause the simulation if the pause button is clicked
        for box in self.input_boxes:
            box.handle_event(event)  # Handle events for input boxes

    def run(self):
        clock = pygame.time.Clock()  # Create a clock object for limiting the frame rate
        while True:
            for event in pygame.event.get():
                self.handle_event(event)  # Handle events
            if self.running:
                self.model.step()  # Advance the simulation if it is running
            self.view.draw()  # Draw the view
            clock.tick(10)  # Limit the frame rate to 10 FPS