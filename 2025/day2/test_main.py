import main
import pytest

@pytest.mark.parametrize(
    "input,expected",
    [
        ('11', True),
        ('12', False),
        ('121', False),
        ('111', True),
        ('1212', True),
        ('123123', True),
        ('123321', False),
        ('1231234', False),
        ('111112111112', True),
        ('1111111', True),
        ('123123123', True),
        ('12341234', True),
        ('12312', False),
        ('1231234', False),
        ('12312312', False),
        ('123133123', False),
        ('12312123', False),
        ('111111111111111111111111111111', True),
        ('11111111111111111111111111111', True),
        ('1231', False),
        ('1', False),
        ('', False),
        ('12312312', False),
        ('101101', True),
        ('898898', True),
    ],
)
def test_isRepeatN(input, expected):
    assert main.isRepeatN(input) == expected

def test_solveB():
    input = [
        "11-22","95-115","998-1012","1188511880-1188511890","222220-222224",
        "1698522-1698528","446443-446449","38593856-38593862","565653-565659",
        "824824821-824824827","2121212118-2121212124",
    ]

    assert main.solveB(input) == 4174379265

