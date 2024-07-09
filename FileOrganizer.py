import os
from pathlib import Path
import shutil

class FileOrganizer:
    def __init__(self, source_directory, target_directory='Organized_data'):
        self.source_directory = Path(source_directory)
        self.target_directory = Path(target_directory)
        self.ensure_directory(self.target_directory)

    @staticmethod
    def ensure_directory(path):
        """Ensure directory exists."""
        path.mkdir(exist_ok=True)

    def organize_files(self):
        """Organize files by date and hour."""
        for filename in os.listdir(self.source_directory):
            if self.is_valid_file(filename):
                date, hour = self.parse_filename(filename)
                folder_name = f'seis_sensor_processed_{date}_{hour}'
                folder_path = self.target_directory / folder_name
                self.ensure_directory(folder_path)
                self.move_file(filename, folder_path)

    @staticmethod
    def is_valid_file(filename):
        """Check if the file matches the expected pattern."""
        return filename.startswith('seis_sensor_processed_') and filename.endswith('.h5')

    @staticmethod
    def parse_filename(filename):
        """Extract date and hour from filename."""
        parts = filename.split('_')
        date = parts[3]  # '20220518'
        hour = parts[4][:2]  # '151012.832+0000' -> '15'
        return date, hour

    def move_file(self, filename, folder_path):
        """Copy file to the specified folder."""
        shutil.copy(str(self.source_directory / filename), str(folder_path / filename))
        print(f'Copied {filename} to {folder_path}')

