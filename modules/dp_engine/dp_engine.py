from snsql import from_df, Privacy, from_connection
from modules.database.database import create_connection
import pandas as pd

# csv_path = 'PUMS.csv'
# meta_path = 'PUMS.yaml'
# pums = pd.read_csv(csv_path)
# reader = from_df(pums, privacy=privacy, metadata=meta_path)

meta_path = 'users.yaml'
conn = create_connection()
privacy = Privacy(epsilon=1.0, delta=1.0)
reader = from_connection(conn, privacy=privacy, metadata=meta_path, engine='sqlserver')

def get_noisy_output(query):
    lst = reader.execute(query)
    result = {}
    for i in range(len(lst[0])):
        result[lst[0][i]] = lst[1][i]
    return result