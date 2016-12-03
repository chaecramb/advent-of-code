import advent2 as a2

def test1():
    instructions = "ULL\nRRDDD\nLURDL\nUUUUD"
    assert a2.code(instructions) == 1985