from enum import Enum
from collections import Counter


class Direction(Enum):   
    north = 0
    east = 1
    south = 2
    west = 3


MOVEMENTS = {
    Direction.north: [0,  1],
    Direction.east: [1, 0],
    Direction.south: [0, -1],
    Direction.west: [-1, 0]
}


class Position:
    """ 
    Position class holds details of current position on grid, orientation 
    and the path taken to reach the current position.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [(x, y)]
        self.orientation = Direction.north

    # adjusts orientation approriately 
    NEW_DIR = {
        'L': lambda x: (x - 1) % 4,
        'R' : lambda x: (x + 1) % 4
    }

    def move(self, distance):
        # adjust x and y coords appropriately and track movements in self.path
        for _ in range(distance):
            self.x += MOVEMENTS[self.orientation][0]
            self.y += MOVEMENTS[self.orientation][1]
            self.path.append(self.coordinates())

    def coordinates(self):
        # the current position of the instance
        return (self.x, self.y)

    def turn(self, direction_to_turn):
        # change orientation of the instance
        new_direction = self.NEW_DIR[direction_to_turn](self.orientation.value)
        self.orientation = Direction(new_direction)


def distance(path):
    current_position = Position(0, 0)
    pathway = path.split(", ")

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
