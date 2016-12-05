from collections import Counter

def parse(encrypted_data):
    name = encrypted_data[:-11]
    room_id = int(encrypted_data[-10:-7])
    checksum = encrypted_data[-6:-1]
    return (name, room_id, checksum)


def count_letters(name):
    return Counter([c for c in name if c.isalpha()])


def most_common(letter_counter, num_letters):
    """ 
    Returns a list of the the most common num_letters letter,
    alphabetised where there are ties
    """
    return sorted(letter_counter.items(), key=lambda x: (-x[1], x[0]))[:5]


def verify_checksum(letters, checksum):
    return ''.join(letters) == checksum


def real_room(name, checksum):
    letter_counter = count_letters(name)
    letters = [l[0] for l in most_common(letter_counter, 5)]
    checksum_valid = verify_checksum(letters, checksum)
    return checksum_valid


def main(file):
    sum_of_sectors = 0

    with open(file, 'r') as f:
        for encrypted_line in f.readlines():
            name, room_id, checksum = parse(encrypted_line.strip())
            if real_room(name, checksum):
                sum_of_sectors += room_id

    return sum_of_sectors
    print("The sum of the sector IDs of the valid rooms is: " + str(sum_of_sectors))


if __name__ == '__main__':
    sum_of_sectors = main('input.txt')
    print("The sum of the sector IDs of the valid rooms is: " + str(sum_of_sectors))


