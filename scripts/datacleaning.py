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


##  Change data types to Binary
binary_columns = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']

for col in binary_columns:
    df[col] = df[col].map({'Yes': 1, 'No': 0})


## Drop and encode irrelevant col
df = df.drop('customerID', axis=1)

df = pd.get_dummies(df, columns=[
    'gender', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport',
    'StreamingTV', 'StreamingMovies', 'Contract', 'PaymentMethod'
])

##  Feature Engineering 
def tenure_group(tenure):
    if tenure <= 12:
        return '0-1 year'
    elif tenure <= 24:
        return '1-2 years'
    elif tenure <= 48:
        return '2-4 years'
    else:
        return '4+ years'

df['TenureGroup'] = df['tenure'].apply(tenure_group)
df = pd.get_dummies(df, columns=['TenureGroup'])


#df.to_csv('data/telco_churn_clean.csv', index=False)
