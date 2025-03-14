import pandas as pd

def load_data(path: str):
    return pd.read_parquet(path)
