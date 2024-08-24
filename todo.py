TODO_FILE = 'todo.txt'


def save_tasks(tasks):
    """ Save the list of tasks to the TODO_FILE.

    Args: 
      tasks(list of dict): 
        A list of tasks,where each task is a dictionary with 'id', 'task', and 'done' status.
    """    
    with open(TODO_FILE, 'w') as file:
        for task in tasks:
            status = 'done' if task["done"] else 'not done'
            file.write(f"{task['id']} - {task['task']} - {status}\n")



def load_tasks():
    """
    Load tasks from the TODO_FILE.

    Returns:
        list of dict: A list of tasks,where each task is represented by a dictionary with 'id', 'task', and 'done' status.

    """
    tasks = []
    try:
        with open(TODO_FILE, 'r') as file:
            for line in file:
                id, task, status = line.rsplit(' - ', 2)
                id = int(id.strip())
                task = task.strip()
                status = status.strip()
                tasks.append({"id": id, "task": task, "done": (status == 'done')})
    except FileNotFoundError:
        pass
    return tasks



def get_next_id(tasks):
    """
    Get the next available ID for a new task.

    Args:
        tasks(list of dict): List of current tasks.

    Returns:
        int: The next available task ID.
    """
    if not tasks:
        return 1
    else:
        return max(task['id'] for task in tasks) + 1
    


def add_task(task_description):
    """
    Add a new task to the list.

    Args:
        task_description(str): The description of the new task.
    """
    tasks = load_tasks()
    new_id = get_next_id(tasks)
    tasks.append({"id": new_id, "task": task_description, "done": False})
    save_tasks(tasks)
    print(f"Task added with ID {new_id}!")



def list_tasks(filter_by=None):
    """
    List all tasks or filter tasks by their completion status.

    Args:
        filter_by(str, optional): Filter tasks by 'done' or 'not done'. If None, list all tasks.
    """
    tasks = load_tasks()

    if filter_by == 'done':
        tasks = [task for task in tasks if task["done"]]
        if not tasks:
            print("No tasks are marked as done.")
            return
    elif filter_by == 'not done':
        tasks = [task for task in tasks if not task["done"]]
        if not tasks:
            print("No tasks are pending.")
            return

    if not tasks:
        print("No tasks available.")
    else:
        for task in tasks:
            status = "Done" if task["done"] else "Not Done"
            print(f"{task['id']}. {task['task']} - {status}")




def mark_task_done(task_id):
    """
    Mark a specific task as completed.

    Args:
        task_id(int): The ID of the task to mark as done.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print("Task marked as done!")
            return
    print("Invalid task ID.")



def delete_task(task_id):
    """
    Delete a specific task from the list.

    Args:
        task_id(int): The ID of the task to delete.
    """
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task['id'] == task_id:
            removed_task = tasks.pop(i)
            save_tasks(tasks)
            print(f"Task '{removed_task['task']}' deleted successfully!")
            return
    print("Invalid task ID.")



def edit_task(task_id):
    """
    Edit the description of a specific task.

    Args:
        task_id(int): The ID of the task to edit.
    """
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            new_description = input("Enter the new description: ")
            task["task"] = new_description
            save_tasks(tasks)
            print("Task updated successfully!")
            return
    print("Invalid task ID.")



def show_help():
    """
    Print a help message describing available commands.
    """
    print("""
    To-Do List Manager Commands:
    1. Add Task: Adds a new task to the list.
    2. Show Tasks: Lists all tasks with their status.
    3. Mark Task as Done: Marks a task as completed.
    4. Delete Task: Removes a task from the list.
    5. Edit Task: Edit an existing task's description.
    6. Exit: Exits the program.
    """)




if __name__ == "__main__":
    while True:
        print("\n===== To-Do List =====")
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Help")
        print("6. Edit Task")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task)

        elif choice == '2':
            filter_by = input("Filter by (done/not done)? Press Enter to skip: ")
            list_tasks(filter_by)

        elif choice == '3':
            task_id = int(input("Enter the task ID to mark as done: "))
            mark_task_done(task_id)

        elif choice == '4':
            task_id = int(input("Enter the task ID to delete: "))
            delete_task(task_id)

        elif choice == '5':
            show_help()

        elif choice == '6':
            task_id = int(input("Enter the task ID to edit: "))
            edit_task(task_id)

        elif choice == '7':
            print("Exiting the To-Do List.")
            break

        else:
            print("Invalid choice. Please try again.")
