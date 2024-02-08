class ToDoList:
    def _init_(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f'Task "{task}" added.')

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f'Task "{task}" deleted.')
        else:
            print(f'Task "{task}" not found.')

    def mark_completed(self, task):
        if task in self.tasks:
            print(f'Task "{task}" marked as completed.')
        else:
            print(f'Task "{task}" not found.')

    def display_tasks(self):
        if not self.tasks:
            print('No tasks found.')
        else:
            print('Current tasks:')
            for idx, task in enumerate(self.tasks, start=1):
                print(f'{idx}. {task}')

def main():
    todo_list = ToDoList()

    while True:
        print('\n===== ToDo List Menu =====')
        print('1. Add Task')
        print('2. Delete Task')
        print('3. Mark as Completed')
        print('4. Display Tasks')
        print('5. Exit')

        choice = input('Enter your choice (1-5): ')

        if choice == '1':
            task = input('Enter the task: ')
            todo_list.add_task(task)
        elif choice == '2':
            task = input('Enter the task to delete: ')
            todo_list.delete_task(task)
        elif choice == '3':
            task = input('Enter the task to mark as completed: ')
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print('Exiting ToDo List. Goodbye!')
            break
        else:
            print('Invalid choice. Please enter a number between 1 and 5.')

if _name_ == "_main_":
    main()
