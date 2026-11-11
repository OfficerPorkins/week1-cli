import os
from todo import parse_task_number, save_tasks, load_tasks

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

def test_save_then_load_round_trip(tmp_path):
    path = str(tmp_path / "tasks.json")
    tasks = [
        {"title": "write tests", "done": False},
        {"title": "push to github", "done": True},
    ]

    save_tasks(tasks, path)

    assert load_tasks(path) == tasks
    

def test_load_missing_file_returns_empty_list(tmp_path):
    path = str(tmp_path / "nope.json")
    result = load_tasks(path)
    assert result == []

def test_load_corrupted_file_backs_up_and_returns_empty_list(tmp_path):
    path = str(tmp_path / "corrupted.json")
    bak = str(tmp_path / "corrupted.json.bak")
    with open(path, "w") as f:
        f.write("not valid json")

    result = load_tasks(path)
    assert result == []
    assert os.path.exists(bak)

    with open(bak) as f:
        assert f.read() == "not valid json"