# main.py
import pygame
from controller import Controller
from model import Model
from view.view import View
from config import WIDTH, HEIGHT, FILL_PROB, CELL_SIZE, FPS


def main():
    pygame.init()  # Initialize Pygame
    model = Model(WIDTH, HEIGHT, FILL_PROB)  # Create a model instance
    view = View(model, CELL_SIZE)  # Create a view instance
    controller = Controller(model, view)  # Create a controller instance
    view.set_controller(controller)  # Set the controller for the view
    controller.run()  # Run the controller
    pygame.quit()  # Quit Pygame


if __name__ == '__main__':
    main()