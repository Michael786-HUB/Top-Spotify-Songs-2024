from dotenv import load_dotenv
import os
import kaggle
import kagglehub
import pandas as pd

load_dotenv()
kaggle_api = os.getenv('key')

import kagglehub
import pandas as pd
import os

def download_kaggle_to_df(dataset_path, filename=None):
    """
    Download a Kaggle dataset and return as pandas DataFrame.
    
    Args:
        dataset_path: Kaggle dataset path (e.g., "username/dataset-name")
        filename: Specific CSV file to load. If None, loads the first CSV found.
    
    Returns:
        pandas DataFrame
    """
    # Download the dataset
    download_path = kagglehub.dataset_download(dataset_path)
    
    files = [f for f in os.listdir(download_path) if f.endswith('.csv')]

    if not files:
        raise ValueError("No CSV files found in the dataset.")
    else:
        csv_file = os.path.join(download_path, filename if filename else files[0]) 
        df = pd.read_csv(csv_file, encoding='latin1')
    
    return df

# Usage:
df = download_kaggle_to_df("nelgiriyewithana/most-streamed-spotify-songs-2024")
print(df.head())







