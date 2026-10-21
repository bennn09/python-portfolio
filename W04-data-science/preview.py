# 載入與檢視資料表內容
import pandas as pd
df = pd.read_csv('students.csv')

# 語法範例：
print(df["math"].mean())

