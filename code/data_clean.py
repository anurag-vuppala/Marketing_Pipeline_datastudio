import string
import pandas as pd


class Read_dataset:
    def __init__(self, path) -> string:
        self.path = path
    
    def read_csv(self):
        return pd.read_csv(f'data/{self.path}')

data = Read_dataset.read_csv('google_age.csv')

print(data)
    
    