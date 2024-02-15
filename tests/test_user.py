import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from datetime import datetime, timedelta
from user import User


# Fixture to generate sample data for four weeks
@pytest.fixture
def sample_data():
    sample_data = {
        "habit_1": [datetime(2024, 1, 1), datetime(2024, 1, 3), datetime(2024, 1, 5)],
        "habit_2": [datetime(2024, 1, 2), datetime(2024, 1, 4), datetime(2024, 1, 6)],
        # Add more habits and completion dates as needed
    }
    return sample_data


# Test user creation
def test_user_creation():
    user = User("Alice")
    assert user.username == "Alice"


# Test habit creation
def test_habit_creation():
    user = User("Alice")
    user.create_habit("Exercise", "daily", 30)
    assert len(user.habits) == 1
    assert user.habits[0].name == "Exercise"


# Test marking habits as complete
def test_marking_habits_complete(sample_data):
    user = User("Alice")
    for habit_name, completion_dates in sample_data.items():
        user.create_habit(habit_name, "daily", 30)
        for completion_date in completion_dates:
            user.mark_habit_complete(habit_name, completion_date)

    for habit in user.habits:
        assert len(habit.completions) == len(sample_data.get(habit.name, []))
        for completion_date in habit.completions:
            assert completion_date in sample_data.get(habit.name, [])


