import advent4 as a4

def test_encrypted_data_parser1():
    assert a4.parse('aaaaa-bbb-z-y-x-123[abxyz]') == ('aaaaa-bbb-z-y-x', 123, 'abxyz')

def test_encrypted_data_parser2():
    assert a4.parse('nzydfxpc-rclop-qwzhpc-qtylyntyr-769[oshgk]') == ('nzydfxpc-rclop-qwzhpc-qtylyntyr', 769, 'oshgk')

def test_valid_room1():
    assert a4.real_room('aaaaa-bbb-z-y-x', 'abxyz') == True

def test_valid_room2():
    assert a4.real_room('a-b-c-d-e-f-g-h', 'abcde') == True

def test_valid_room3():
    assert a4.real_room('not-a-real-room', 'oarel') == True

def test_fake_room2():
    assert a4.real_room('totally-real-room', 'decoy') == False

def test_advent4():
    assert a4.main('test_input.txt') == 1514
