from task import Task

class Todo:
    # Initialize instances TakeInput
    def __init__(self, user_input):
        # Initialize empty dictionary to store tasks
        self.tasks = {}
        self.completed_tasks = {}
        self.user_input = user_input


    def add_task(self, task_name, description, status=False):
        # Add a new task to the tasks dictionary
        # Tasks are stored as a Task object with name, description & status
        self.tasks[task_name] = Task(task_name, description, status)


    def remove_task(self, task_name):
        # Remove a task from the dictionary after user confirmation
        if task_name in self.tasks:
            if self.user_input.run_double_confirmation():
                del self.tasks[task_name]
                print(f"Task {task_name} has been removed.")
        else:
            print(f"Task {task_name} does not exist.") 


    def update_task(self, tasks, task_name, new_name, new_description):
        # Check if the new task name is different from the current task name
        if new_name != task_name:
            # If the task exists keep its completion status. If not, ddefault to False
            status = tasks[task_name].status if task_name in tasks else False
            # Delete the old task
            del tasks[task_name]
        else:
            # If the task hasnt changed, keep the status
            status = tasks[task_name].status
        
        # Update or create new task object
        tasks[new_name] = Task(new_name, new_description, status)
        print(f"Task {task_name} has been updated.")

    
    def update_status(self, task_name):
        # Update the status of task
        if task_name in self.tasks:
            self.tasks[task_name].status = True
            # Move completed task to completed_tasks dictionary and delete from tasks dictionary
            self.completed_tasks[task_name] = self.tasks[task_name]
            del self.tasks[task_name]
            print(f"Task {task_name} status has been updated to Completed")
        else:
            print(f"Task {task_name} not found.")


    def edit_task(self, task_name, new_name, new_description):
        # Edit an existing task using the Edit class's update_task method
        self.update_task(self.tasks, task_name, new_name, new_description)


    def list_tasks(self):
        # List all the tasks stored in the tasks dictionary
        if self.tasks:
            for index, (task_name, task) in enumerate(self.tasks.items(), start=1):
                task.print(index)
        else:
            print("No tasks.")