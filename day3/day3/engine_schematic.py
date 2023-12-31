
import string
from dataclasses import dataclass
from collections import namedtuple

@dataclass
class Point:
    x: int
    y: int

    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y

HorizontalLine = namedtuple('HorizontalLine', ['x_start', 'x_end', 'y'])

def is_symbol(character: str):
    if (len(character) != 1):
        return False
    if character in string.punctuation and character != '.':
        return True
    else:
        return False


class EngineSchematic:
    lines: list[str]

    def __init__(self, lines: list[str]) -> None:
        self.lines = lines 

    def get_whole_number(self, point: Point):
        left = point.x
        right = point.x
        while(self.lines[point.y][left - 1] in string.digits and left >= 0):
            left -= 1
        while(self.lines[point.y][right + 1] in string.digits and right < len(self.lines[point.y])):
            right += 1
        return HorizontalLine(left, right, point.y)

    def find_adjacent_part_numbers(self, point: Point):
        min_x = max(0, point.x - 1)
        max_x = min(len(self.lines[point.y]), point.x + 1)
        min_y = max(0, point.y -1)
        max_y = min(len(self.lines), point.y + 1)
        adjacent_numbers : set[HorizontalLine]= set()
        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                if(y == point.y and x == point.x):
                    continue
                if(self.lines[y][x] in string.digits):
                    adjacent_numbers.add(self.get_whole_number(Point(x, y))) 
        return adjacent_numbers
    
    def line_to_number(self, line: HorizontalLine):
        return int(self.lines[line.y][line.x_start:line.x_end + 1]) 

    def find_all_part_numbers(self):
        part_numbers: set[HorizontalLine] = set()
        for y, line in enumerate(self.lines):
            for x, character in enumerate(line):
                if(is_symbol(character)):
                    part_numbers.update(self.find_adjacent_part_numbers(Point(x, y)))
        return list(map(self.line_to_number, part_numbers))

    def get_gear_ratio(self, point: Point):
        character = self.lines[point.y][point.x]
        if(len(character) != 1): return 0
        if(character != '*'): return 0
        adjacent_numbers = list(map(self.line_to_number, self.find_adjacent_part_numbers(point)))
        if(len(adjacent_numbers) == 2):
            return adjacent_numbers[0] * adjacent_numbers[1]
        return 0
    
    def find_sum_of_all_gear_ratios(self):
        sum = 0
        for y, line in enumerate(self.lines):
            for x, character in enumerate(self.lines[y]):
                sum += self.get_gear_ratio(Point(x, y))
        return sum
