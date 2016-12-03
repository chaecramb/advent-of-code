# Layout of keypad
KEYPAD = [
['', '', '1', '', ''],
['', '2','3','4', ''],
['5','6','7','8','9'],
['', 'A','B','C', ''],
['', '', 'D', '', '']
]

# Possible movements
MOVEMENT = {
    'U': (-1, 0),
    'R': (0, 1),
    'D': (1, 0),
    'L': (0, -1)
}

# Constraints of keypad
MIN = 0
MAX = 4


def keypad_digit(position):
    """ Return the digit of the keypad corresponding to a position """
    return KEYPAD[position[0]][position[1]]


def move(position, direction):
    """ Return a new position having moved in given direction """

    # Return position as a tuple contrained by bounds of keypad
    return (max(MIN, min(position[0]+MOVEMENT[direction][0], MAX)),
            max(MIN, min(position[1]+MOVEMENT[direction][1], MAX)))


def code(instructions):
    # Start at number 5 on the keypad
    position = (2,0)
    current_digit = keypad_digit(position)

    # Digits in the code
    digits = []

    # Split input by line
    # Each line corresponds the to instructions for an
    # individual digit
    digit_instructions = instructions.split('\n')

    # Follow sequence of instructions for each digit
    for sequence in digit_instructions:
        for direction in sequence:
            new_position = move(position, direction)

            # Change position if the new position 
            # is not blank
            if keypad_digit(new_position):
                position = new_position

        digits.append(keypad_digit(position))

    # Return the code sequence as a string
    return ''.join(digits)


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        print(code(f.read()))