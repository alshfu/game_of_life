import random
import pygame


class Cell:
    def __init__(self):
        self.is_alive = False
        self.is_ant = False
        self.ant_direction = None
        self.is_purple = False
        self.purple_count = 0


class Model:
    def __init__(self, width, height, fill_prob=0.1):
        self.width = width
        self.height = height
        self.grid = [[Cell() for _ in range(height)] for _ in range(width)]
        self.alive_cells = 0
        self.dead_cells = 0
        self.ants = 0
        self.steps = 0

        for row in self.grid:
            for cell in row:
                if random.random() < fill_prob:
                    cell.is_alive = True

    def step(self):
        new_grid = [[Cell() for _ in range(self.height)] for _ in range(self.width)]
        for y in range(self.height):
            for x in range(self.width):
                cell = self.grid[x][y]
                alive_neighbours = self.count_alive_neighbours(x, y)

                if self.form_square(x, y):
                    new_grid[x][y].is_purple = True
                    new_grid[x][y].purple_count = 2
                    new_grid[x + 1][y].is_purple = True
                    new_grid[x + 1][y].purple_count = 2
                    new_grid[x][y + 1].is_purple = True
                    new_grid[x][y + 1].purple_count = 2
                    new_grid[x + 1][y + 1].is_purple = True
                    new_grid[x + 1][y + 1].purple_count = 2
                elif not cell.is_alive and alive_neighbours == 4 and not cell.is_purple:
                    new_grid[x][y].is_alive = True
                elif cell.is_purple:
                    cell.purple_count -= 1
                    if cell.purple_count == 0:
                        cell.is_purple = False
                        cell.is_alive = True
                elif cell.is_alive and alive_neighbours in [2, 3]:
                    new_grid[x][y].is_alive = True
                elif not cell.is_alive and alive_neighbours == 3:
                    new_grid[x][y].is_alive = True
                if not cell.is_alive and alive_neighbours == 3:  # Ant appears if there are 8 neighbours
                    new_grid[x][y].is_ant = True
                    new_grid[x][y].ant_direction = random.choice(['N', 'E', 'S', 'W'])
                if cell.is_ant:
                    self.move_ant(cell, new_grid, x, y)

        self.alive_cells = sum(cell.is_alive for row in self.grid for cell in row)
        self.dead_cells = self.width * self.height - self.alive_cells
        self.ants = sum(cell.is_ant for row in self.grid for cell in row)
        self.steps += 1
        self.grid = new_grid

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

    def form_square(self, x, y):
        if x + 1 >= self.width or y + 1 >= self.height:
            return False
        return all(
            self.grid[nx][ny].is_alive
            for nx in range(x, x + 2)
            for ny in range(y, y + 2)
            if 0 <= nx < self.width and 0 <= ny < self.height
        )

