import json
import os

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
        os.replace("tasks.json", "tasks.json.bak")
        print("Error: tasks.json is corrupted. Starting with an empty task list.")
        return []

tasks = load_tasks()

while True:
    choice = input("(a)dd, (v)iew, (c)omplete, (d)elete, or (q)uit? ")

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

    elif choice == "c":
        if not tasks:
            print("No tasks to complete!")
        else:
            show_tasks(tasks)
            number_text = input("Which task number is done? ")
            try:
                task_index = int(number_text) - 1
                if 0 <= task_index < len(tasks):
                    tasks[task_index]["done"] = True
                    print("Marked as done!")
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")                   
            except ValueError:
                print("Invalid task number.")

    elif choice == "d":
        if not tasks:
            print("No tasks to delete!")
        else:
            show_tasks(tasks)
            number_text = input("Which task number would you like to delete? ")
            try:
                task_index = int(number_text) - 1
                if 0 <= task_index < len(tasks):
                    deleted_task = tasks.pop(task_index)
                    print(f"Deleted task: {deleted_task['title']}")
                    save_tasks(tasks)   
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid task number.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please type a, v, c, d, or q.")