import pytest
from cli_handler import CLIHandler

@pytest.fixture
def cli_handler():
    return CLIHandler()

def test_handle_input_create_user(cli_handler, capsys, monkeypatch):
    # Mock user input
    user_input = "4\n"  # Choose option 4 to exit the application

    # Monkeypatch input function to provide user input
    monkeypatch.setattr('builtins.input', lambda _: user_input)

    # Ensure that SystemExit is raised
    with pytest.raises(SystemExit):
        cli_handler.handle_input("4")  # Provide the choice argument

    # Capture stdout to verify output
    captured = capsys.readouterr()
    assert "Exiting HABITUAL. Goodbye!" in captured.out
