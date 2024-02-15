import sys
import os

# Add the path to the parent directory of the tests directory
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from cli_handler import CLIHandler
