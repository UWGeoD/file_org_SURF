import os
import sys
from pathlib import Path
import re

def write_folder_names_to_config(source_directory, config_file='config.txt'):
    pattern = re.compile(r'^Well_-SURF\(\)__on_\d{8}_\d{6}_UTC\(\+0000\)$')
    source_path = Path(source_directory)
    folders = [folder for folder in os.listdir(source_path) if pattern.match(folder)]

    with open(config_file, 'w') as file:
        for folder in folders:
            file.write(f"{folder}\n")
    print(f"Config file created with {len(folders)} folders.")

def main():
    if len(sys.argv) != 2:
        print("Usage: python create_config.py [source_directory]")
        sys.exit(1)

    source_directory = sys.argv[1]
    write_folder_names_to_config(source_directory)

if __name__ == "__main__":
    main()

