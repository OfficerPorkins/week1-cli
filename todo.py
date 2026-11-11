import json
import os
from datetime import datetime


def save_tasks(tasks, path="tasks.json"):
    with open(path, "w") as f:
        json.dump(tasks, f)


def load_tasks(path="tasks.json"):
    try:
        with open(path) as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        bak = path + ".bak"
        if os.path.exists(bak):
            stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
            os.replace(bak, f"{bak}.{stamp}")
        os.replace(path, bak)
        print(f"{path} was corrupted; old data saved to {bak}")
        return []

def parse_task_number(text, count):
    """Turn user input like '2' into a 0-based index, or None if invalid."""
    try:
        number = int(text)
    except ValueError:
        return None
    if number < 1 or number > count:
        return None
    return number - 1


def show_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f"{i}. [{mark}] {task['title']}")


def get_task_index(tasks):
    text = input("Task number: ")
    index = parse_task_number(text, len(tasks))
    if index is None:
        print("Invalid task number.")
        return None
    return index


def main():
    tasks = load_tasks()
    while True:
        choice = input("(a)dd, (v)iew, (c)omplete, (d)elete, (e)dit, (q)uit: ").lower()
        if choice == "a":
            tasks.append({"title": input("Task: "), "done": False})
        elif choice == "v":
            show_tasks(tasks)
        elif choice in ("c", "d", "e"):
            index = get_task_index(tasks)
            if index is None:
                continue
            if choice == "c":
                tasks[index]["done"] = True
            elif choice == "d":
                tasks.pop(index)
            elif choice == "e":
                tasks[index]["title"] = input("New title: ")
        elif choice == "q":
            save_tasks(tasks)
            break
        save_tasks(tasks)


if __name__ == "__main__":
    main()