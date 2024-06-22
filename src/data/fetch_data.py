import os
import shutil

from utils.kaggle_utils import download_and_setup_dataset
from utils.config import load_config


def move_nested_contents(base_path):
    # Iterate through the specified paths
    for path in base_path:
        # Check if the path exists
        if os.path.exists(path):
            # List all items in the directory
            for item in os.listdir(path):
                nested_path = os.path.join(path, item)
                # Check if the item is a directory and matches the base name
                if os.path.isdir(nested_path) and os.path.basename(path) in item:
                    # Move contents of the nested directory to the parent directory
                    for nested_item in os.listdir(nested_path):
                        shutil.move(os.path.join(nested_path, nested_item), path)
                    # Remove the now-empty nested directory
                    os.rmdir(nested_path)
        else:
            print(f"Path {path} does not exist.")

def fetch_data():
    config = load_config()
    dataset_name = config['kaggle_dataset']
    raw_data_path = config['data_paths']['raw']
    file_paths = download_and_setup_dataset(dataset_name, raw_data_path)
    move_nested_contents(file_paths)
    
    
def main():
    fetch_data()
    
if __name__ == '__main__':
    main()