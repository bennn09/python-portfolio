import pandas as pd
# 1. 讀取資料
df = pd.read_csv('students.csv')
# 2. 基本統計
math_avg = df['math'].mean()
eng_max = df['english'].max()
# 3. 輸出結果
print(f"班級數學平均：{math_avg:.1f} 分")
print(f"英文最高分：{eng_max} 分")
