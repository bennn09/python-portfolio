import pandas as pd
df = pd.read_csv('data.csv')
# 篩選數學大於 90 分的學生
high_math = df[df['math'] > 90]
print("數學優異名單：")
print(high_math[['name', 'math']])		#外層中括號表示選取欄位，裡面的串列列出要選的欄位名稱

# 篩選英文不及格的學生
low_eng = df[df['english'] < 60]
print("英文需輔導名單：")
print(low_eng[['name', 'english']])
