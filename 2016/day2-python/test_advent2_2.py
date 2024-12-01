import advent2_2 as a2_2

def test1():
    instructions = """ULL\nRRDDD\nLURDL\nUUUUD"""
    assert a2_2.code(instructions) == '5DB3'