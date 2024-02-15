import pickle

class StorageManager:
    def __init__(self, filename="habitual_data.pkl"):
        self.filename = filename

    def save_data(self, data):
        """Save data to storage."""
        try:
            with open(self.filename, "wb") as file:
                pickle.dump(data, file)
            print("Data saved successfully.")
        except IOError as e:
            print(f"Error saving data: {e}")

    def load_data(self):
        """Load data from storage."""
        try:
            with open(self.filename, "rb") as file:
                data = pickle.load(file)
            print("Data loaded successfully.")
            return data
        except (IOError, EOFError) as e:
            print(f"Error loading data: {e}")
            return []

# Testing the implementation
if __name__ == "__main__":
    try:
        # Test the StorageManager class
        storage_manager = StorageManager()
        data_to_save = ["test_data"]
        storage_manager.save_data(data_to_save)
        loaded_data = storage_manager.load_data()
        print(loaded_data)  # Output: ["test_data"]
    except Exception as e:
        print(f"An error occurred: {e}")
