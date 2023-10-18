import pygame
import math
from queue import PriorityQueue

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("A* Path Finding Algorithm")

# Colors
RED = (255, 0, 0)  # Closed
GREEN = (0, 255, 0)  # Open
BLUE = (0, 0, 255)  # Barrier
YELLOW = (255, 255, 0)  # Start
WHITE = (255, 255, 255)  # Empty
BLACK = (0, 0, 0)  # Path
PURPLE = (128, 0, 128)  # End
ORANGE = (255, 165, 0)  # Visited
GREY = (128, 128, 128)  # Grid Lines
TURQUOISE = (64, 224, 208)  # Visited


# Node class
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.width = width
        self.total_rows = total_rows

    def get_pos(self):
        return self.row, self.col

    def is_closed(self):
        return self.color == RED

    def is_open(self):
        return self.color == GREEN

    def is_barrier(self):
        return self.color == BLUE

    def is_start(self):
        return self.color == YELLOW

    def is_end(self):
        return self.color == TURQUOISE

    def reset(self):
        self.color = WHITE

    def make_closed(self):
        self.color = RED

    def make_open(self):
        self.color = GREEN

    def make_barrier(self):
        self.color = BLACK

    def make_end(self):
        self.color = TURQUOISE

    def make_path(self):
        self.color = PURPLE

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid):
        pass

    def __lt__(self, other):  # less than
        return False


def h(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return abs(x1 - x2) + abs(y1 - y2)  # Manhattan distance


def make_grid(rows, width):
    grid = []
    gap = width // rows
    for i in range(rows):
        grid.append([])
        for j in range(rows):
            spot = Node(i, j, gap, rows)
            grid[i].append(spot)

    return grid


def draw_grid(win, rows, width):
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, ORANGE, (0, i * gap), (width, i * gap))
        for j in range(rows):
            pygame.draw.line(win, ORANGE, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
    win.fill()
