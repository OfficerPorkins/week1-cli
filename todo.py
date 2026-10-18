tasks = []

while True:
    choice = input("(a)dd, (v)iew, or (q)uit? ")

    if choice == "a":
        task = input("What's the task? ")
        tasks.append(task)
        print("Added!")
    elif choice == "v":
        for task in tasks:
            enumerate(tasks)
            print("-", task)
    elif choice == "q":
        print("Goodbye!")
        break
    else:
        print("Please type a, v, or q.")