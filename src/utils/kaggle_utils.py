import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

def download_and_setup_dataset(dataset_name, directory_path):
    directory = os.path.abspath(directory_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

    api = KaggleApi()
    api.authenticate()

    api.dataset_download_files(dataset_name, path=directory, unzip=True)
    
    file_paths = []

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        file_paths.append(os.path.abspath(file_path))
        
    return file_paths