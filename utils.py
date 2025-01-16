import pandas as pd

df = pd.read_csv('house-data.csv')
address_columns = df.columns[df.columns.get_loc('Abazar'):]
address_list = list(address_columns)