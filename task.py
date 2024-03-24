class Task:
    # Initialize class attributes
    name = ""
    description = ""
    status = False

    def __init__(self, name, description, status):
        self.name = name
        self.description = description
        self.status = status

    def get_status(self):
        # Get the completion status of the task
        if self.status == False:
            return "Not Completed"
        else:
            return "Completed"

    def print(self, index=0):
        # Print formatted task details
        print(f"""{index}. {self.name}
    * {self.description} - [{self.get_status()}]\n""")