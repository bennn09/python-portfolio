# 適合回答：不同類別之間，誰比較高？
import matplotlib.pyplot as plt #plt為別稱

subjects = ["國文", "英文", "數學"]
scores = [81.2, 78.5, 78.0]

# 設定中文字型，避免中文亂碼
plt.rcParams["font.sans-serif"] = ["Microsoft JhengHei"] 
plt.rcParams["axes.unicode_minus"] = False

# 繪製長條圖基本程式
plt.bar(subjects, scores)
plt.show()

# 儲存圖表並輸出結果
output_file = "subject_average.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
plt.show()

