from colors import Colors
import pygame
from position import Position

# parent class for all block types
class Block():
    # initialize block objects
    def __init__(self, id):
        self.id = id
        self.cells = {}
        self.cell_size = 30
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        self.colors = Colors.get_cell_colors()

    # move the block through rows and columns
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # calculates block's current position
    def get_cell_positions(self):
        # get block and list of rotation states
        tiles = self.cells[self.rotation_state]
        # store blocks cell position
        moved_tiles = []
        for position in tiles:
            # calculate cell position
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # changes current rotation state
    def rotate(self):
        self.rotation_state += 1
        if self.rotation_state == len(self.cells):
           self.rotation_state = 0

    # if block is rotated outside the game screen, undo the rotation
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    # draws block on screen
    def draw(self, screen, offset_x, offset_y):
        # list of possible block positions
        tiles = self.get_cell_positions()
        for tile in tiles:
            # create the block with calculated measurements
            tile_rect = pygame.Rect(offset_x + tile.column*self.cell_size, offset_y + tile.row*self.cell_size, self.cell_size-1, self.cell_size-1)
            # put created block with a color on screen
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)