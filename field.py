from pygame import display, draw
from enum import Enum
from collections import namedtuple

WHITE = 255, 255, 255
SIZE = 16

class FieldState(Enum):
    EMPTY = 0
    SNAKE = 1
    APPLE = 2

Point = namedtuple("Point", ("x", "y"))

class Field:
    def __init__(self, width: int, height: int):
        self.arr = [[FieldState.EMPTY for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height
    
    def render(self, screen):
        for y in range(self.width):
            for x in range(self.height):
                if self.get_value(Point(x, y)) == FieldState.SNAKE:
                    draw.rect(screen, WHITE, (x*SIZE, y*SIZE, SIZE, SIZE))

    def get_value(self, point: Point) -> FieldState:
        return self.arr[point.y][point.x]
    
    def set_value(self, point: Point, value: FieldState) -> bool:
        if self.within_bounds(point):
            self.arr[point.y][point.x] = value
            return True
        return False

    def within_bounds(self, point: Point):
        return 0 <= point.x < self.width and 0 <= point.y < self.height

