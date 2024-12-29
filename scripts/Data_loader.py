import pandas as pd
import sqlite3

def load_data(file_path):
    return pd.read_csv(file_path)