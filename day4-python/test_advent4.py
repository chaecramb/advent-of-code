import advent4 as a4

def test1():
    assert a4.real_room('aaaaa-bbb-z-y-x-123[abxyz]') == True

def test2():
    assert a4.real_room('a-b-c-d-e-f-g-h-987[abcde]') == True

def test3():
    assert a4.real_room('not-a-real-room-404[oarel]') == False

def test4():
    assert a4.real_room('totally-real-room-200[decoy]') == False
