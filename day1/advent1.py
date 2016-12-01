from enum import Enum
import csv

class Direction(Enum):
    north = 0
    east = 1
    south = 2
    west = 3

def turnLeft(direction):
    if direction == Direction.north:
         return Direction(3)
    return Direction(direction.value-1)

def turnRight(direction):
    if direction == Direction.west:
        return Direction(0)
    return Direction(direction.value+1)

def distance(path):
    x = 0
    y = 0
    visited = []
    direction = Direction.north
    pathway = path.replace(" ", "").split(",")

    for step in pathway:
        # Change direction
        directionToTurn = step[0]
        if directionToTurn == "L":
            direction = turnLeft(direction)
        else:
            direction = turnRight(direction)

        # Modify x and y based on distance
        distance = int(str(step[1:]))
        if direction == Direction.north:
            y += distance
        elif direction == Direction.south:
            y -= distance
        elif direction == Direction.east:
            x += distance
        elif direction == Direction.west:
            x -= distance

        visited.append([x,y])

    # Final distance calculation
    return abs(x) + abs(y)

