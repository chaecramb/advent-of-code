from enum import Enum
import csv


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, direction, distance):
        if direction == Direction.north:
            self.y += distance
        elif direction == Direction.south:
            self.y -= distance
        elif direction == Direction.east:
            self.x += distance
        elif direction == Direction.west:
            self.x -= distance

    def coordinates(self):
        return (self.x, self.y)


class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

    def turnLeft(self):
        if self == Direction.north:
             return Direction(3)
        return Direction(self.value-1)

    def turnRight(self):
        if self == Direction.west:
            return Direction(0)
        return Direction(self.value+1)


def change_direction(current_direction, direction_to_turn):
    if direction_to_turn == "L":
        return current_direction.turnLeft()
    else:
        return current_direction.turnRight()


def distance(path):
    current_position = Position(0, 0)
    direction = Direction.north
    pathway = path.split(", ")

    for step in pathway:
        direction_to_turn, distance = step[0], int(step[1:])

        # Change direction        
        direction = change_direction(direction, direction_to_turn)

        # Modify current_position x and y coords based on distance and direction
        current_position.move(direction, distance)

    # Final distance calculation
    x, y = current_position.coordinates()
    return abs(x) + abs(y)
