from todo import parse_task_number

def test_valid_number():
    assert parse_task_number("1", 3) == 0
    assert parse_task_number("2", 3) == 1
    assert parse_task_number("3", 3) == 2

def test_out_of_range_number():
    assert parse_task_number("0", 3) is None
    assert parse_task_number("4", 3) is None
    
def test_non_numeric_input():
    assert parse_task_number("abc", 3) is None
    assert parse_task_number("", 3) is None

def test_whitespace_around_number():
    assert parse_task_number(" 2 ", 3) == 1