import pandas as pd
df = pd.read_excel('Laptop_Logistic_Regression_Dataset.xlsx')
print("Columns:")
for col in df.columns:
    print(f"- {col}")
print("\nFirst row:")
print(df.iloc[0].to_dict())
