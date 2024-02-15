from datetime import datetime

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False
        self.completion_date = None

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True
        self.completion_date = datetime.now()

    def is_completed(self):
        """Check if the task is completed."""
        return self.completed

    def get_completion_date(self):
        """Get the completion date of the task."""
        return self.completion_date

# Testing the implementation
if __name__ == "__main__":
    # Test the Task class
    task = Task("Exercise for 30 minutes")
    print(task.is_completed())  # Output: False
    task.mark_completed()
    print(task.is_completed())  # Output: True
    print(task.get_completion_date())  # Output: Current date and time
