# Layout of keypad
KEYPAD = [
[1,2,3],
[4,5,6],
[7,8,9]
]


def keypad_digit(position):
    """ Return the digit of the keypad corresponding to a position """
    return KEYPAD[position[0]][position[1]]


def move(position, direction):
    """ Return a new position having moved in given direction """

    # Possible movements
    MOVEMENT = {
        'U': (-1, 0),
        'R': (0, 1),
        'D': (1, 0),
        'L': (0, -1)
    }

    # Constraints of keypad
    MIN = 0
    MAX = 2

    # Constrain return tuple by 0 and 2 to stay within bounds
    # of the keypad
    return (max(MIN, min(position[0]+MOVEMENT[direction][0], MAX)),
            max(MIN, min(position[1]+MOVEMENT[direction][1], MAX)))


def code(instructions):
    # Start at number 5 on the keypad
    position = (1,1)

    # Digits in the code
    digits = []

    # Split input but line
    # Each line corresponds the to instructions for an
    # individual digit
    digit_instructions = instructions.split('\n')

    # For each sequence of instructions calculate the
    # end position on the keypad and append the corresponding
    # digit to the code sequence
    for sequence in digit_instructions:
        for direction in sequence:
            position = move(position, direction) 
        digits.append(keypad_digit(position))
    
    # Join digits in the the code sequence as a string then 
    # return as an int
    return int(''.join([str(d) for d in digits]))


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        print(code(f.read()))