tasks = []

# Loading disabled for now (JSON is next)
# try:
#     with open("tasks.txt", "r") as f:
#         for line in f:
#             tasks.append(line.strip())
# except FileNotFoundError:
#     pass

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        mark = "x" if task["done"] else " "
        print(f" {i}) [{mark}] {task['title']}")

def save_tasks(tasks):
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

while True:
    choice = input("(a)dd, (v)iew, (c)omplete, (d)elete, or (q)uit? ")

    if choice == "a":
        task = input("What is the task? ")
        tasks.append({"title": task, "done": False})
        # save_tasks(tasks)   # disabled for now
        print(f"Added! You now have {len(tasks)} task(s).")

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
                    # save_tasks(tasks)   # disabled for now
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid task number.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please type a, v, c, d, or q.")