import pandas as pd

file = 'data_analysis/data/telco_customer_churn.csv'

df = pd.read_csv(file)

print(df.columns)