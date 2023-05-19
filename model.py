# model.py
import random
from config import BIRTH_NEIGHBOURS, SURVIVE_NEIGHBOURS, ANT_NEIGHBOURS


class Cell:
    def __init__(self):
        self.is_alive = False  # Flag indicating whether the cell is alive or not
        self.is_ant = False  # Flag indicating whether the cell contains an ant or not
        self.ant_direction = None  # Direction of the ant


class Model:
    def __init__(self, width, height, fill_prob=0.1):
        self.width = width  # Width of the grid
        self.height = height  # Height of the grid
        self.grid = [[Cell() for _ in range(height)] for _ in range(width)]  # Create a grid of cells
        self.alive_cells = 0  # Number of alive cells
        self.dead_cells = 0  # Number of dead cells
        self.ants = 0  # Number of ants
        self.steps = 0  # Number of steps taken in the simulation

        # Initialize cells based on the fill probability
        for row in self.grid:
            for cell in row:
                if random.random() < fill_prob:
                    cell.is_alive = True

    def step(self):
        new_grid = [[Cell() for _ in range(self.height)] for _ in range(self.width)]  # Create a new grid
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[x][y]  # Get the current cell
                alive_neighbours = self.count_alive_neighbours(x, y)  # Count the number of alive neighbors

                if not cell.is_alive and alive_neighbours == BIRTH_NEIGHBOURS:
                    new_grid[x][y].is_alive = True  # Birth rule
                elif cell.is_alive and alive_neighbours in SURVIVE_NEIGHBOURS:
                    new_grid[x][y].is_alive = True  # Survival rule
                elif not cell.is_alive and alive_neighbours == ANT_NEIGHBOURS:
                    new_grid[x][y].is_ant = True  # Ant rule
                    new_grid[x][y].ant_direction = random.choice(['N', 'E', 'S', 'W'])  # Set a random direction for the ant

                if cell.is_ant:
                    self.move_ant(cell, new_grid, x, y)  # Move the ant

        self.alive_cells = sum(cell.is_alive for row in self.grid for cell in row)  # Update the count of alive cells
        self.dead_cells = self.width * self.height - self.alive_cells  # Update the count of dead cells
        self.ants = sum(cell.is_ant for row in self.grid for cell in row)  # Update the count of ants
        self.steps += 1  # Increment the step count
        self.grid = new_grid  # Update the grid

    def count_alive_neighbours(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.grid[nx][ny].is_alive:
                    count += 1
        return count

    def move_ant(self, cell, new_grid, x, y):
        dx, dy = 0, 0
        if cell.ant_direction == 'N':
            dy = -1
        elif cell.ant_direction == 'E':
            dx = 1
        elif cell.ant_direction == 'S':
            dy = 1
        elif cell.ant_direction == 'W':
            dx = -1

        nx, ny = x + dx, y + dy
        if 0 <= nx < self.width and 0 <= ny < self.height and not self.grid[nx][ny].is_alive:
            new_grid[nx][ny].is_ant = True
            new_grid[nx][ny].ant_direction = self.turn(cell)
            new_grid[nx][ny].is_alive = True

    def turn(self, cell):
        directions = ['N', 'E', 'S', 'W']
        index = directions.index(cell.ant_direction)
        return directions[(index + 1) % len(directions)]