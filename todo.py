tasks = []

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f" {i}) {task}")

while True:
    choice = input("(a)dd, (v)iew, (d)elete, or (q)uit? ")

    if choice == "a":
        task = input("What is the task? ")
        tasks.append(task)
        print(f"Added! You now have {len(tasks)} task(s).")

    elif choice == "v":
        if not tasks:
            print("No tasks yet!")
        else:
            show_tasks(tasks)

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
                    print(f"Deleted task: {deleted_task}")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid task number.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please type a, v, d, or q.")