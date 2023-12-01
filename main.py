class Task:
    def __init__(self, description, completed=False):
        self.description = description
        self.completed = completed


class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        new_task = Task(description)
        self.tasks.append(new_task)
        print(f"Task '{description}' added successfully.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            print("Tasks:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✔" if task.completed else "❌"
                print(f"{i}. [{status}] {task.description}")

    def mark_task_as_complete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1].completed = True
            print(f"Task {task_index} marked as complete.")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print(f"Task {task_index} deleted.")
        else:
            print("Invalid task index.")


def main():
    scheduler = TaskScheduler()

    while True:
        print("\nTask Scheduler Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            description = input("Enter task description: ")
            scheduler.add_task(description)
        elif choice == '2':
            scheduler.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter task index to mark as complete: "))
            scheduler.mark_task_as_complete(task_index)
        elif choice == '4':
            task_index = int(input("Enter task index to delete: "))
            scheduler.delete_task(task_index)
        elif choice == '5':
            print("Exiting Task Scheduler.")
            break
        else:
            print("Invalid choice. Please choose from 1 to 5.")


if __name__ == "__main__":
    main()
