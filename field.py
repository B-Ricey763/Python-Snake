from enum import Enum

class FieldState(Enum):
    EMPTY = 0
    SNAKE = 1
    APPLE = 2

class Field:
    def __init__(self, width: int, height: int):
        self.arr = [[0 for y in range(width)] for x in range(height)]
        self.width = width
        self.height = height
    
    def get_value(self, coords) -> FieldState:
        return self.arr[row][col]
    
    def set_value(self, row, col, value)