from controller import Controller
from model import Model
from view import View


def main():
    game_model = Model(50, 50)
    view = View(game_model)
    controller = Controller(game_model, view)
    controller.run()

if __name__ == '__main__':
    main()