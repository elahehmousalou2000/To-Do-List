tasks = []

while True:
    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        tasks.append(input("Task: "))
    elif choice == "2":
        if not tasks:
            print("No tasks.")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif choice == "3":
        if tasks:
            number = int(input("Task number: "))
            if 1 <= number <= len(tasks):
                tasks.pop(number - 1)
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
