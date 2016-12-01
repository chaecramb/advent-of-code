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
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.path = [(x, y)]
        self.current_direction = Direction.north

    NEW_DIR = {
        'L': lambda x: (x + 1) % 4,
        'R' : lambda x: (x - 1) % 4
    }

    def move(self, distance):
        for _ in range(distance):
            self.x += MOVEMENTS[self.current_direction][0]
            self.y += MOVEMENTS[self.current_direction][1]
            self.path.append(self.coordinates())

    def coordinates(self):
        return (self.x, self.y)

    def turn(self, direction_to_turn):
        new_direction = self.NEW_DIR[direction_to_turn](self.current_direction.value)
        self.current_direction = Direction(new_direction)


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
