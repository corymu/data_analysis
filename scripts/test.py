import pandas as pd

file = 'data/telco_churn_clean.csv'

df = pd.read_csv(file)

print(df.columns)