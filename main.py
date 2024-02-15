from cli_handler import CLIHandler

def main():
    cli_handler = CLIHandler()
    try:
        cli_handler.run()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
