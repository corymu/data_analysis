import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

file = 'data/telco_churn_clean.csv'

df = pd.read_csv(file)
print(df.shape)
print(df.columns)
print(df.describe())
print(df['Churn'].value_counts(normalize=True))
#churn is 73.5%/26.5%


#1
#Churn Distribution
def seaborntest(df):
    sns.countplot(x='Churn', data=df)
    plt.title('Churn Distribution')
    plt.show()
    return df

#2
## Numeric Feature Distro
def numericfeaturedistro(df):
    numeric_cols = ['tenure', 'MonthlyCharges', 'TotalCharges', 'AvgMonthlySpend']

    for col in numeric_cols:
        plt.figure(figsize=(6,4))
        sns.histplot(data=df,x=col,hue='Churn',kde=True, bins=30)
        plt.title(f'Distribution of {col} by Churn')
        plt.show()
    return df

#3
## Churn vs Categorical Features
def catchurn(df):
    cat_cols = ['Contract_Month-to-month', 'Contract_One year', 'Contract_Two year', 'PaperlessBilling', 'PaymentMethod_Bank transfer (automatic)', 'PaymentMethod_Credit card (automatic)', 'PaymentMethod_Electronic check', 'PaymentMethod_Mailed check']

    for col in cat_cols:
        churn_rate = df.groupby(col)['Churn'].mean().sort_values(ascending=False)
        churn_rate.plot(kind='bar')
        plt.title(f'Churn Rate by {col}')
        plt.ylabel('Churn Rate')
        plt.show()
    return df

#4
##Correlation Matrix
def CorrMatrix(df):
    churn_corr = df.corr(numeric_only=True)['Churn'].drop('Churn')
    
    top_corr = churn_corr[abs(churn_corr)> .2].sort_values(ascending=False)
    
    plt.figure(figsize=(12,8))
    sns.barplot(x=top_corr,y=top_corr.index,palette='coolwarm')
    
    plt.title('Correlation Matrix')
    plt.show()

#5
##Key Feature Interaction
def keyfeat(df):
    sns.scatterplot(x='MonthlyCharges',y='tenure',hue='Churn',data=df)
    plt.title('Monthly Charges vs Tenure by Churn')
    plt.show()
    return df


#seaborntest(df)
#numericfeaturedistro(df)
#catchurn(df)
#CorrMatrix(df)
#keyfeat(df)