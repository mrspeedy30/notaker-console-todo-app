import time
tasks = []


def add_task():
    print("Add task")
    new_task = input("Enter the text of the task: ")
    new_task = new_task.strip()
            
    if len(new_task) == 0:
        print("Cannot add an empty line")
        return
    
    if len(new_task) > 100:
        print("You cannot add a string that is too long")
        return 

    is_present = False
    for task in tasks:
        if task["text"].lower() == new_task.lower():
            is_present = True
            break
            
    if is_present:
        print("This task is already in the list")
        return

    tasks.append({"text": new_task, "is_done": False})
    print(f"Task '{new_task}' successfully added.")
    time.sleep(1)

def list_tasks():
    print("All tasks:")
    if len(tasks) == 0:
        print("The task list is empty.")
        time.sleep(2)
        return

    for index, task in enumerate(tasks, start=1):
        if task["is_done"]:
            print(f'✓ {index}. {task["text"]}')
        else:
            print(f'𐄂 {index}. {task["text"]}')
    time.sleep(2)
def mark_task():
    print("Time to complpiting the tasks")

    if len(tasks) == 0:
        print("The task list is empty.")
        return
    
    list_tasks()
    
    user_input = input("Enter the number of the task to mark: ").strip()
    if not user_input.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(user_input) - 1
    if not (0 <= task_index < len(tasks)):
        print("Invalid task number.")
        return

    tasks[task_index]["is_done"] = True
    print(f"Task '{tasks[task_index]['text']}' marked as completed.")
    time.sleep(1)

def delete_task():
    print("Delete task")

    if len(tasks) == 0:
        print("The task list is empty.")
        return

    list_tasks()

    user_input = input("Enter the number of the task to delete: ").strip()

    if not user_input.isdigit():
        print("Please enter a valid number.")
        return

    task_index = int(user_input) - 1
    
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['text']}' successfully deleted.")
    else:
        print("Invalid task number.")
    time.sleep(1)

def show_help():
    print("-" * 15 + " Help " + 15 * "-")
    print("The program allows you keep a to-do list")
    print("You can add, delete, and mark a task")
    print("-" * 15 + "-------" + 15 * "-")
    time.sleep(2)

while True:
    print("=" * 15 + " To-Do " + 15 * "=")
    print("1. Add task")
    print("2. Show all tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Help")
    print("0. Exit")
    print("=" * 15 + "========" + 15 * "=")

    choice = input("Select an action: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        list_tasks()

    elif choice == "3":
        mark_task()

    elif choice == "4":
        delete_task()

    elif choice == "5":
        show_help()

    elif choice == "0":
        print("Exit")
        break
    else:
        print("Invalid command.")
