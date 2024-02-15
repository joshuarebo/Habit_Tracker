import pytest
from datetime import datetime
from task import Task  # Import the Task class from task.py


# Test task creation
def test_task_creation():
    task = Task("Exercise for 30 minutes")
    assert task.description == "Exercise for 30 minutes"
    assert not task.is_completed()  # Ensure task is initially not completed


# Test marking tasks as completed
def test_task_completion():
    task = Task("Exercise for 30 minutes")
    assert not task.is_completed()  # Ensure task is initially not completed
    task.mark_completed()
    assert task.is_completed()  # Ensure task is completed after calling mark_completed()
    assert task.get_completion_date() is not None  # Ensure completion date is set



# Run pytest
if __name__ == "__main__":
    pytest.main()
