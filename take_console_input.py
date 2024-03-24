class TakeInput:
    def DecideInput(self, input_type):
        if input_type == "Text":
            return TakeConsoleInput()


class TakeConsoleInput(TakeInput):
    def run_add_task(self, todo_list):
        name = input("Enter task name: ").capitalize()
        description = input("Enter task description: ").capitalize()
        # Add the new task to the todo list
        todo_list.add_task(name, description)
        print(f"Task {name} has been added.")


    def take_user_choice(self):
        user_choice = input("""What would you like to do?
            a: Add Task
            b: Remove Task
            c: Edit Task
            d: List All Tasks
            > """).capitalize()
        
        return user_choice


    def run_remove_task(self, todo_list):
        while True:
            task_name = input("Enter task you would like to remove: ").capitalize()
            # Remove specified item from the todo list
            todo_list.remove_task(task_name)
            break


    def run_edit_task(self, todo_list):
        while True:
            
            user_choice = input("""What would you like to do: 
                a: Edit Task
                b: Mark As Completed
                > """).capitalize()
            
            if user_choice == 'A':           
                task_name = input("Enter task you would like to edit: ").capitalize() 
                # Check if the task already exists
                if task_name in todo_list.tasks:
                        # Run double confirmation method
                    if self.run_double_confirmation():
                        new_name = input("Enter new task name: ").capitalize()
                        new_description = input("Enter new task description: ")
                        # Edit the specified task
                        todo_list.edit_task(task_name, new_name, new_description)
                    break
                else: 
                    print("Task does not exist. Please select a task from the list.")
            elif user_choice == 'B':
                task_name = input("Enter the task you would like to mark as completed: ").capitalize()
                # Run double confirmation and update_status method
                if self.run_double_confirmation():
                    todo_list.update_status(task_name)
                break
            else:
                print("Invalid input. Please enter 'A' or 'B'.")


    def run_double_confirmation(self):
        while True:
            user_choice = input("Please confirm your action. Y to confirm, N to decline: ").capitalize()
            # Return True on confirmation, False on decline
            if user_choice == 'Y':
                return True
            elif user_choice == 'N':
                print("Confirmation Declined")
                return False
            else:
                print("Invalid input. Please enter 'y' to confirm or 'n' to decline.")


    def run_user_list(self, todo_list):
        # Display all items in the todo list
        todo_list.list_tasks()
        input("Press 'Enter' to return to the main menu. ")