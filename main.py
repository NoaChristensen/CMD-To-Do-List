from todo import Todo
from take_console_input import TakeInput

def run(todo_list, user_input):
        # Main loop for to-do list UI & interaction
        while True:
            user_choice = user_input.take_user_choice()
        
            # Direct the user's input to the corresponding method
            if user_choice == 'A':
                user_input.run_add_task(todo_list)
            elif user_choice == 'B':
                user_input.run_remove_task(todo_list)
            elif user_choice == 'C':
                user_input.run_edit_task(todo_list)
            elif user_choice == 'D':
                user_input.run_user_list(todo_list)
            else:
                print("Invalid Input. Please enter 'A', 'B', 'C' or 'D'")


user_input = TakeInput().DecideInput("Text")
todo_list = Todo(user_input)

run(todo_list, user_input)