import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from analytics_module import AnalyticsModule
from user import User  # Adjust import as needed


# Fixture to create a user object
@pytest.fixture
def user():
    return User("TestUser")


# Fixture to initialize AnalyticsModule
@pytest.fixture
def analytics_module():
    return AnalyticsModule()


# Test analyzing habits for a user
def test_analyze_habits(analytics_module, user):
    # Add sample habits and completion data to the user
    user.create_habit("Exercise", "daily", 30)
    user.create_habit("Read", "weekly", 4)
    user.create_habit("Meditate", "daily", 30)
    user.mark_habit_complete("Exercise", "2024-01-01")
    user.mark_habit_complete("Read", "2024-01-05")
    user.mark_habit_complete("Meditate", "2024-01-01")
    user.mark_habit_complete("Meditate", "2024-01-02")
    user.mark_habit_complete("Meditate", "2024-01-03")

    # Analyze habits
    analysis_result = analytics_module.analyze_habits(user)

    # Verify the analysis result
    assert "all_habits" in analysis_result
    assert "habits_by_periodicity" in analysis_result
    assert "longest_streak" in analysis_result





# Run pytest
if __name__ == "__main__":
    pytest.main()
