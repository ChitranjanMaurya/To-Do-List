
file_name = "tasks.txt"


# Load tasks from file
def load_tasks():
    try:
        file = open(file_name, "r")
        tasks = file.read().splitlines()
        file.close()
        return tasks
    except:
        return []


# Save tasks to file
def save_tasks(tasks):
    file = open(file_name, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()


tasks = load_tasks()

while True:
    print("\n===== TO-DO LIST =====")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    elif choice == "2":
        task = input("Enter a task: ")
        tasks.append(task)
        save_tasks(tasks)
        print("Task added.")

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))
            if num >= 1 and num <= len(tasks):
                tasks.pop(num - 1)
                save_tasks(tasks)
                print("Task removed.")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")