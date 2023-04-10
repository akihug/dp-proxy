import snsql
from snsql import Privacy
import pandas as pd


def get_noisy_output(query):
    csv_path = 'PUMS.csv'
    meta_path = 'PUMS.yaml'
    pums = pd.read_csv(csv_path)
    privacy = Privacy(epsilon=1.0, delta=1.0)
    reader = snsql.from_df(pums, privacy=privacy, metadata=meta_path)
    result = reader.execute(query)
    return result