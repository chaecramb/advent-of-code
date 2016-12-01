from enum import Enum
import csv
from collections import Counter
from itertools import cycle


class Direction(Enum):   
    north = 0
    east = 1
    south = 2
    west = 3


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [(x, y)]
        self.current_direction = Direction.north

    def move(self, distance):
        for i in range(0, distance):
            self.__adjust_coords()
            self.path.append(self.coordinates())

    def coordinates(self):
        return (self.x, self.y)

    def turn(self, direction_to_turn):
        if direction_to_turn == "L":
            self.__turn_left()
        else:
            self.__turn_right()

    def __turn_left(self):
        if self.current_direction == Direction.north:
             self.current_direction = Direction(3)
        else:
            self.current_direction = Direction(self.current_direction.value-1)

    def __turn_right(self):
        if self.current_direction == Direction.west:
            self.current_direction = Direction(0)
        else:
            self.current_direction = Direction(self.current_direction.value+1)

    def __adjust_coords(self):
        if self.current_direction == Direction.north:
                self.y += 1
        elif self.current_direction == Direction.south:
                self.y -= 1
        elif self.current_direction == Direction.east:
                self.x += 1
        elif self.current_direction == Direction.west:
                self.x -= 1


def distance(path):
    current_position = Position(0, 0)
    pathway = path.replace(" ", "").split(",")

    for step in pathway:
        direction_to_turn, distance = step[0], int(step[1:])

        # Change direction        
        current_position.turn(direction_to_turn)

        # Modify current_position x and y coords based on distance and direction
        current_position.move(distance)

        # Return early if we've visited a location twice
        for coord, count in Counter(current_position.path).items():
            if count > 1:
                return abs(coord[0]) + abs(coord[1])

    # Final distance calculation    
    x, y = current_position.coordinates()
    return abs(x) + abs(y)
