tasks = []

while True:
    choice = input("(a)dd, (v)iew, or (q)uit? ")

    if choice == "a":
        task = input("What's the task? ")
        tasks.append(task)
        print("Added!")
    elif choice == "v":
        if not tasks:
            print("No tasks yet!")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f" {i}. {task}")
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Please type a, v, or q.")