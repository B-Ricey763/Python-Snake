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
        self.width = width
        self.height = height
        self.arr = [[FieldState.EMPTY for y in range(width)] for x in range(height)]

    def clear(self) -> None:
        """Iterates through each cell in the field and sets to empty"""
        for y in range(self.width):
            for x in range(self.height):
                self.set_value(Point(y, x), FieldState.EMPTY)

    def render(self, screen) -> None:
        """Draws each cell in the field based on their state"""
        for y in range(self.width):
            for x in range(self.height):
                if self.get_value(Point(x, y)) == FieldState.SNAKE:
                    draw.rect(screen, WHITE, (x*SIZE, y*SIZE, SIZE, SIZE))

    def get_value(self, point: Point) -> FieldState:
        """Get a field state value from a certain position"""
        return self.arr[point.y][point.x]
    
    def set_value(self, point: Point, value: FieldState) -> bool:
        """Set a field state value. Returns: whether or not it could be done"""
        if self.within_bounds(point):
            self.arr[point.y][point.x] = value
            return True
        return False

    def within_bounds(self, point: Point):
        """Returns: wether or not the point exists on the field"""
        return 0 <= point.x < self.width and 0 <= point.y < self.height

