import sys
from io import StringIO
import pytest
from cli_handler import CLIHandler
from habitual_app import HabitualApp
from unittest.mock import patch


@pytest.fixture
def cli_handler():
    return CLIHandler()


def test_cli_creation(cli_handler):
    assert isinstance(cli_handler, CLIHandler)


@patch('sys.stdin', StringIO("1\nAlice\n4\n"))
def test_handle_input_create_user(cli_handler):
    app = HabitualApp()
    cli_handler.app = app
    cli_handler.handle_input("1")
    assert app.find_user("Alice") is not None


@patch('sys.stdin', StringIO("2\nAlice\n4\n"))
def test_handle_input_delete_user(cli_handler):
    app = HabitualApp()
    cli_handler.app = app
    cli_handler.handle_input("2")
    assert app.find_user("Alice") is None


@patch('sys.stdin', StringIO("3\nAlice\n4\n"))
def test_handle_input_analyze_habits(cli_handler):
    app = HabitualApp()
    cli_handler.app = app
    analysis_result = cli_handler.handle_input("3")
    assert analysis_result.strip() == "User not found."


@patch('sys.stdin', StringIO("4\n"))
def test_handle_input_exit(cli_handler):
    app = HabitualApp()
    cli_handler.app = app
    with pytest.raises(SystemExit):
        cli_handler.handle_input("4")


@patch('sys.stdin', StringIO("4\n"))
def test_run(cli_handler):
    app = HabitualApp()
    cli_handler.app = app
    with pytest.raises(SystemExit):
        cli_handler.run()
