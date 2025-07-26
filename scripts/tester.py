import pandas as pd

df = pd.read_csv('data/telco_customer_churn.csv')

#print(df.shape) #show # rows and columns
#print(df.info()) #show column names and types
#print(df.head()) #print preview

#print(df.isnull().sum()) # shows null values for the df

#print(df['TotalCharges'].dtype) #show dtype for the column
print(df['TotalCharges'].head(10)) #preview totalcharges

#changes total charges to a numeric value
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

#prints total null values
print(df['TotalCharges'].isnull().sum())

#drops na
df = df.dropna(subset=['TotalCharges'])

#prints null total charges which should now be 0
print(df['TotalCharges'].isnull().sum())
