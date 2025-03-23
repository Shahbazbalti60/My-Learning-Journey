# Simple To-Do List Application

tasks = []  # List to store tasks

def add_task(task):
    tasks.append(task)
    print(f'Added: {task}')

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Removed: {task}')
    else:
        print(f'Task not found: {task}')

def show_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task}")
    else:
        print("\nYour To-Do List is empty.")

while True:
    print("\nOptions: 1. Add Task | 2. Remove Task | 3. Show Tasks | 4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter a task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter the task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Exiting To-Do List App. Goodbye!")
        break
    else:
        print("Invalid choice, try again!")
