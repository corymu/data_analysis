# Correlection to Chrun Analysis Document
    File = eda_churn.py

### This is a desciption file to understand the File Stated above


## Churn Distribution
This is the first test that seaborn and matplotlib are working properly
a general display of the overall churn rate of the overall dataset

## Numeric Feature Distro
*/images/Distribution of Monthly Charges by Churn.png*
*/images/Distribution of Tenure by Churn.png*
*/images/Distribution of Total Charges by Churn.png*

Filter for strong correlation
    */images/Distribution of Monthly Charges by Churn.png* show that the longer that the user stay with the service the less churn there tends to be

## Churn vs Categorical Features
*images/Churn Rate by Contract One Year.png*
*images/Churn Rate by Contract Two Year.png*
*images/Churn Rate by Contract_Month-to-Month.png*
*images/Churn Rate by Paperless Billing.png*
*images/Churn Rate by Payment Method Credit Card (auto).png*
*images/Churn Rate by Payment Method Electronic Check.png*
*images/Churn Rate by Payment Method Mailed Check.png*
*images/Churn Rate by Payment Method_Bank Transfer(Auto).png*

Creates churn rate based on category
    displays each category by churn rate
    a great visual for each of the differnt categories

## Correlation Matrix
*/images/Churn Correlation Matrix.png*
Breaks down the highest correlated categories 

## Key Feature Interaction
*/images/Monthly Charges vs Tenure.png*
Scatter plot display that show the distrbution of monthly charges with a heatmap of color to show churn
