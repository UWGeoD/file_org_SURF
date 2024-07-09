import os
from pathlib import Path
import shutil
from multiprocessing import Pool
import logging

class FileOrganizer:
    def __init__(self, source_directory, target_directory='Organized_data'):
        self.source_directory = Path(source_directory)
        self.target_directory = Path(target_directory)
        self.log_directory = self.target_directory / 'Log'
        self.ensure_directory(self.target_directory)
        self.ensure_directory(self.log_directory)
        self.setup_logging()

    @staticmethod
    def ensure_directory(path):
        """Ensure directory exists."""
        path.mkdir(parents=True, exist_ok=True)

    def setup_logging(self):
        """Setup logging for both success and error logs."""
        logging.basicConfig(level=logging.INFO)  # Set the logging level if needed
        self.success_logger = logging.getLogger('success')
        self.error_logger = logging.getLogger('error')
        

        # Set loggers to not propagate the messages to the root logger
        self.success_logger.propagate = False
        self.error_logger.propagate = True

        success_handler = logging.FileHandler(self.log_directory / 'success.log')
        error_handler = logging.FileHandler(self.log_directory / 'error.log')

        success_handler.setLevel(logging.INFO)
        error_handler.setLevel(logging.ERROR)

        formatter = logging.Formatter('%(asctime)s - %(message)s')
        success_handler.setFormatter(formatter)
        error_handler.setFormatter(formatter)

        self.success_logger.addHandler(success_handler)
        self.error_logger.addHandler(error_handler)

    def organize_files(self):
        """Organize files by date and hour using multiprocessing."""
        tasks = []
        for filename in os.listdir(self.source_directory):
            if self.is_valid_file(filename):
                date, hour = self.parse_filename(filename)
                folder_name = f'seis_sensor_processed_{date}_{hour}'
                folder_path = self.target_directory / folder_name
                self.ensure_directory(folder_path)
                tasks.append((self.source_directory / filename, folder_path))

        with Pool() as pool:
            pool.starmap(self.copy_file, tasks)

    @staticmethod
    def is_valid_file(filename):
        """Check if the file matches the expected pattern."""
        return filename.startswith('seis_sensor_processed_') and filename.endswith('.h5')

    @staticmethod
    def parse_filename(filename):
        """Extract date and hour from filename."""
        parts = filename.split('_')
        date = parts[3]  # '20220518'
        hour = parts[4][:2]  # '15'
        return date, hour

    def copy_file(self, source_file, folder_path):
        """Copy file to the specified folder and log the action."""
        target_file = folder_path / source_file.name
        try:
            shutil.copy(str(source_file), str(target_file))
            self.success_logger.info(f'Copied {source_file.name} to {folder_path}')
        except Exception as e:
            self.error_logger.error(f'Failed to copy {source_file.name} to {folder_path} - {e}')


