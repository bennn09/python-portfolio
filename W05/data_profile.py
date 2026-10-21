import pandas as pd
 
df = pd.read_csv('messy_students.csv')

print(df.head(20)) #顯示所有資料

df=df.drop_duplicates() #刪除重複資料
df['name'] = df['name'].str.strip() #清除前空白
print(df.head(20)) #顯示清理後的資料

# 將乾淨的 DataFrame 匯出為新 CSV 檔
df.to_csv(
    "cleaned_students.csv",
    index=False
)
