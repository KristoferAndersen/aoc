import main

def test_day1b():
    print("test 1b")
    input = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]
    assert 6 == main.solve_b(input)
