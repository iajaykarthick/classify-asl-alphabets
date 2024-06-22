from utils.kaggle_utils import download_and_setup_dataset
from utils.config import load_config

def fetch_data():
    config = load_config()
    dataset_name = config['kaggle_dataset']
    raw_data_path = config['data_paths']['raw']
    download_and_setup_dataset(dataset_name, raw_data_path)
    
def main():
    fetch_data()
    
if __name__ == '__main__':
    main()