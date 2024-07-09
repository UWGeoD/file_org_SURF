import sys
from pathlib import Path
from FileOrganizer import FileOrganizer

def run_organizer_for_all_folders(config_file, source_root, target_root):
    source_root = Path(source_root)
    target_root = Path(target_root)

    with open(config_file, 'r') as file:
        folders = [line.strip() for line in file]

    for folder in folders:
        source_directory = source_root / folder
        target_directory = target_root  # Use only the root target directory

        organizer = FileOrganizer(source_directory, target_directory)
        organizer.organize_files()
        print(f'Processed files from {source_directory} to {target_directory}')

def main():
    if len(sys.argv) != 4:
        print("Usage: python run_organizer_many.py [config_file] [source_root] [target_root]")
        sys.exit(1)
    
    config_file, source_root, target_root = sys.argv[1:4]
    run_organizer_for_all_folders(config_file, source_root, target_root)

if __name__ == "__main__":
    main()

