import sys
import re
from pathlib import Path
from FileOrganizer import FileOrganizer  # Ensure FileOrganizer.py is accessible

def run_organizer_for_all_folders(config_file, source_root, target_root):
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
        # Extract date and time to construct the target folder name correctly
        match = re.search(r'\d{8}_\d{6}', folder)
        if match:
            date_time = match.group()
            date = date_time[:8]  # '20220519'
            hour = date_time[9:11]  # '15'
            target_folder_name = f'seis_sensor_processed_{date}_{hour}'
            source_directory = Path(source_root) / folder
            target_directory = Path(target_root) / target_folder_name
            organizer = FileOrganizer(source_directory, target_directory)
            organizer.organize_files()
        else:
            print(f"Skipping folder with unexpected format: {folder}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python run_organizer_many.py [config_file] [source_root] [target_root]")
        sys.exit(1)
    
    config_file = sys.argv[1]
    source_root = sys.argv[2]
    target_root = sys.argv[3]
    run_organizer_for_all_folders(config_file, source_root, target_root)

if __name__ == "__main__":
    main()

