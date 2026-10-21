import pandas as pd
 
df = pd.read_csv('messy_students.csv')
 
df.info()

print(df.isna().sum())
print(df.duplicated().sum())
