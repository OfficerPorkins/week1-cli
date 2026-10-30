import json
import os
from datetime import datetime

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f" {i}) [{mark}] {task['title']}")

def save_tasks(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=2)

def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        if os.path.exists("tasks.json.bak"):
            os.replace("tasks.json.bak", f"tasks.json.bak.{datetime.now().strftime('%Y%m%d%H%M%S')}")
        os.replace("tasks.json", "tasks.json.bak")
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        return []

def get_task_index(tasks):
    if not tasks:
        print("No tasks to modify!")
        return None

    show_tasks(tasks)
    number_text = input("Which task number? ")

    task_index = parse_task_number(number_text, len(tasks))

    if task_index is None:
        print("Invalid task number.")
        return None
    
    return task_index

def parse_task_number(text, count):
    try:
        task_number = int(text)
    except ValueError:
        return None

    if not (1 <= task_number <= count):
        return None

    return task_number - 1

tasks = load_tasks()

while True:
    choice = input("(a)dd, (e)dit, (v)iew, (c)omplete, (d)elete, or (q)uit? ")

    if choice == "a":
        task = input("What is the task? ")
        tasks.append({"title": task, "done": False})
        print(f"Added! You now have {len(tasks)} task(s).")
        save_tasks(tasks)

    elif choice == "v":
        if not tasks:
            print("No tasks yet!")
        else:
            show_tasks(tasks)

    elif choice in ["c", "d", "e"]:
        task_index = get_task_index(tasks)
        if task_index is None:
            continue

        if choice == "c":
            tasks[task_index]["done"] = True
            print("Marked as done!")
        elif choice == "d":
            deleted_task = tasks.pop(task_index)
            print(f"Deleted task: {deleted_task['title']}")
        elif choice == "e":
            new_title = input("What is the new title? ")
            tasks[task_index]["title"] = new_title
            print("Task updated!")

        save_tasks(tasks)

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please type a, e, v, c, d, or q.")