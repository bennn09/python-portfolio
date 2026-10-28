# 適合回答：兩個數值之間是否呈現關係？
import matplotlib.pyplot as plt

study_hours = [1.0, 2.5, 0.5, 3.0, 1.5]
scores = [65, 91, 58, 94, 73]

# 繪製散佈圖基本程式
plt.scatter(study_hours, scores)
plt.show()

# 儲存圖表並輸出結果
output_file = "subject_average.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
plt.show()