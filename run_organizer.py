import sys
from pathlib import Path
from FileOrganizer import FileOrganizer

def main():
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python run_organizer.py [source_directory] [target_directory]")
        sys.exit(1)

    # Extract source and target directories from command-line arguments
    source_dir = Path(sys.argv[1])
    target_dir = Path(sys.argv[2])

    # Create an instance of FileOrganizer with the provided paths
    organizer = FileOrganizer(source_directory=source_dir, target_directory=target_dir)

    # Organize files
    organizer.organize_files()

if __name__ == '__main__':
    main()

