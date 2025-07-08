tasks = []  # sahi variable name

while True:
    print("\n📋 Menu")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. Show Tasks")
    print("4. Exit")

    choice = int(input("Enter your choice (1-4): "))

    if choice == 1:
        task = input("Enter your task: ")
        tasks.append(task)
        print(" Your task added.")

    elif choice == 2:
        task = input("Enter the task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print(" Your task removed.")
        else:
            print(" Task not found!")

    elif choice == 3:
        if not tasks:
            print("No tasks in the list.")
        else:
            print(" Your To-Do List:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == 4:
        print("Exiting the To-Do List! Goodbye.")
        break

    else:
        print(" Invalid choice. Please enter a number from 1 to 4.")


    

