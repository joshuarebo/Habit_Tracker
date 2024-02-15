import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from storage_manager import StorageManager


# Fixture to initialize StorageManager
@pytest.fixture
def storage_manager():
    return StorageManager()


# Test saving and loading data
def test_save_and_load_data(storage_manager, tmp_path):
    # Prepare sample data
    data_to_save = ["test_data"]

    # Save data
    storage_manager.filename = tmp_path / "test_data.pkl"
    storage_manager.save_data(data_to_save)

    # Load data
    loaded_data = storage_manager.load_data()

    # Verify data integrity
    assert loaded_data == data_to_save


# Run pytest
if __name__ == "__main__":
    pytest.main()
