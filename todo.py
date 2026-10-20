tasks = []

# try to open "tasks.txt" for reading
#     for each line in the file
#         strip the newline off the line
#         add it to the tasks list
# if the file doesn't exist yet
#     do nothing (the list just starts empty)
try:
    with open("tasks.txt", "r") as f:
        for line in f:
            tasks.append(line.strip())
except FileNotFoundError:
    pass  # If the file doesn't exist, we just start with an empty list

def show_tasks(tasks):
    for i, task in enumerate(tasks, start=1):
        print(f" {i}) {task}")

def save_tasks(tasks):
    # open "tasks.txt" for writing
    #     for each task in the list
    #         write the task and a newline to the file
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")

while True:
    choice = input("(a)dd, (v)iew, (d)elete, or (q)uit? ")

    

    if choice == "a":
        task = input("What is the task? ")
        tasks.append(task)
        save_tasks(tasks)
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
                    save_tasks(tasks)
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Invalid task number.")

    elif choice == "q":
        print("Goodbye!")
        break

    else:
        print("Please type a, v, d, or q.")