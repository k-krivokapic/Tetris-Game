import pygame
from colors import Colors


class Grid:
    # initialize objects to create the grid
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30
        # creates the tetris grid
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        # gets colors
        self.colors = Colors.get_cell_colors()

    # print the grid
    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                print(self.grid[row][column], end = " ")
            print()

    # checks if the current row/column position is valid
    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # checks if cell(s) are empty
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # checks if cell(s) are occupied
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # set values to 0 to clear a row
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] = 0

    # when a user clears a row, the row above it needs to become the new bottom row
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            # copies what the 2nd to last row is and makes it the new bottom row
            self.grid[row+num_rows][column] = self.grid[row][column]
            # clears the original bottom row
            self.grid[row][column] = 0

    # clears full rows and keeps track of the number of rows cleared
    def clear_full_rows(self):
        completed = 0
        # iterates through rows backwards
        for row in range(self.num_rows-1, 0, -1):
            # if the row is full, clear it
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    # clear the entire grid
    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # draws the grid on the screen
    def draw(self, screen):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # x = column, y = row, w,h = self.cell_size
                cell_rect = pygame.Rect(column*self.cell_size+11, row*self.cell_size+11, self.cell_size-1, self.cell_size-1)
                # surface, color, rect
                pygame.draw.rect(screen, self.colors[cell_value], cell_rect)