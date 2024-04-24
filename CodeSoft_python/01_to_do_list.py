import json

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})

    def view_tasks(self):
        for index, task in enumerate(self.tasks, start=1):
            print(f"{index}. [{task['completed'] and 'X' or ' '}] {task['task']}")

    def mark_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
        else:
            print("Invalid task index!")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index!")

    def save_to_file(self, filename):
        with open(filename, "w") as f:
            json.dump(self.tasks, f)

    def load_from_file(self, filename):
        try:
            with open(filename, "r") as f:
                self.tasks = json.load(f)
        except FileNotFoundError:
            print("File not found!")

def main():
    todo_list = ToDoList()

    # Load tasks from file if exists
    todo_list.load_from_file("tasks.json")

    while True:
        print("\n=== To-Do List ===")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Save and Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to mark as complete: "))
            todo_list.mark_complete(task_index)
        elif choice == "4":
            task_index = int(input("Enter task index to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            todo_list.save_to_file("tasks.json")
            print("To-Do list saved. Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
