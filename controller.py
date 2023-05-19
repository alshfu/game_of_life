import pygame


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.running = True

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.view.start_button.collidepoint(event.pos):
                self.running = True
            elif self.view.pause_button.collidepoint(event.pos):
                self.running = False

    def run(self):
        clock = pygame.time.Clock()
        while True:
            for event in pygame.event.get():
                self.handle_event(event)
            if self.running:
                self.model.step()
            self.view.draw()
            clock.tick(10)  # Limit the frame rate to 10 FPS