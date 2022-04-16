from src.utils.all_utils import read_yaml
import argparse
import pandas as pd
import os


def get_data(config_path):
    config = read_yaml(config_path)
    remote_data_path = config["data_source"]

    df = pd.read_csv(remote_data_path,encoding="ISO-8859-1",sep=';')

    artifacts_dir = config['artifacts']['artifacts_dir']
    raw_local_dir = config['artifacts']['raw_local_dir']
    raw_local_file = config['artifacts']['raw_local_file']

    raw_local_dir_path = os.path.join(artifacts_dir,raw_local_dir)
    raw_local_file_path = os.path.join(raw_local_dir_path,raw_local_file)
    print(raw_local_file_path)


    return df
df = get_data('config/config.yaml')

print(df.head())




