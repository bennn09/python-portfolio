from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt


# 讀取資料並計算各科平均
df = pd.read_csv('cleaned_students2.csv')
subjects = ["國文", "英文", "數學"]
columns = ["chinese", "english", "math"]
average_scores = [df[column].mean() for column in columns]

# 設定中文字型，避免中文亂碼
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"] 
plt.rcParams["axes.unicode_minus"] = False

#製作長條圖並設定標題、座標軸與格線
plt.figure(figsize=(8, 5))
plt.bar(subjects, average_scores)
plt.title("各科平均成績")
plt.xlabel("科目")
plt.ylabel("平均分數")
plt.grid(axis="y", alpha=0.3)
plt.tight_layout()

# 儲存圖表並輸出結果
output_file = "subject_average.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
plt.show()

print("各科平均成績：")
for subject, score in zip(subjects, average_scores):
    print(f"{subject}：{score:.1f}")
print(f"圖表已儲存至：{output_file}")
