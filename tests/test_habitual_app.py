import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from habitual_app import HabitualApp
from user import User
from storage_manager import StorageManager
from analytics_module import AnalyticsModule
from io import StringIO


@pytest.fixture
def app():
    return HabitualApp()


def test_create_user(app):
    username = "Alice"
    app.create_user(username)
    assert app.find_user(username) is not None


def test_delete_user(app):
    username = "Bob"
    app.create_user(username)
    app.delete_user(username)
    assert app.find_user(username) is None


def test_analyze_habits(app):
    username = "Alice"
    user = User(username)
    user.create_habit("Exercise", "daily", 30)
    app.users.append(user)
    analysis_result = app.analyze_habits(username)
    assert isinstance(analysis_result, dict)


def test_handle_input(app, monkeypatch):
    # Mock user input
    user_input = ["1", "Alice", "4"]
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(user_input)))

    # Ensure that the user is created successfully
    app.handle_input("1")

    # Retrieve the created user
    user = app.find_user("Alice")

    # Check if the user object is not None and has the correct username
    assert user is not None
    assert user.username == "Alice"


def test_run(app, monkeypatch):
    # Mock user input for app.run()
    user_input = ["1", "Alice", "4"]
    monkeypatch.setattr('sys.stdin', StringIO('\n'.join(user_input)))

    # Ensure that the app runs without errors
    try:
        app.run()
    except SystemExit as e:
        assert e.code == None


def test_save_and_load_data(app):
    # Create and save some data
    user1 = User("Alice")
    user2 = User("Bob")
    app.users.append(user1)
    app.users.append(user2)
    app.save_data()

    # Clear current data
    app.users = []

    # Load the saved data
    app.load_data()

    # Check if data is loaded correctly
    assert len(app.users) == 2
    assert app.find_user("Alice") is not None
    assert app.find_user("Bob") is not None


def test_display_menu(capsys):
    app = HabitualApp()
    app.display_menu()
    captured = capsys.readouterr()
    assert "1. Create User" in captured.out
    assert "2. Delete User" in captured.out
    assert "3. Analyze Habits" in captured.out
    assert "4. Exit" in captured.out


# Run pytest
if __name__ == "__main__":
    pytest.main()
