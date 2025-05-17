import runpy

def main():
    try:
        choice = int(input("Enter a challenge number: "))

        script_path = f"challenges/{choice}.py"
        print(f"Running {script_path}...\n")
        runpy.run_path(script_path, run_name="__main__")

    except FileNotFoundError:
        print(f"Script {script_path} not found.")
    except ValueError:
        print("Invalid input. Please enter a number.")
    except Exception as e:
        print(f"An error occurred while running the script: {e}")

if __name__ == "__main__":
    main()
