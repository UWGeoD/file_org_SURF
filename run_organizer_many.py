import subprocess
import sys

def run_organizer_for_all_folders(config_file):
    try:
        with open(config_file, 'r') as file:
            folders = file.readlines()
    except FileNotFoundError:
        print(f"Error: The configuration file '{config_file}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

    for folder in folders:
        folder = folder.strip()  # Remove any trailing newline characters
        # Correct the path in the command if necessary
        command = f"python file_org_SURF/run_organizer.py 'May_2022/{folder}' 'Organized_SURF/{folder}'"
        subprocess.run(command, shell=True)

def main():
    if len(sys.argv) != 2:
        print("Usage: python run_organizer_many.py [config_file]")
        sys.exit(1)
    
    config_file = sys.argv[1]
    run_organizer_for_all_folders(config_file)

if __name__ == "__main__":
    main()


