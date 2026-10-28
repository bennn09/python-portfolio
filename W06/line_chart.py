# 適合回答：數值如何隨時間或順序變化？
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temperatures = [22, 24, 21, 26, 28]

# 繪製折線圖基本程式
plt.plot(days, temperatures)
plt.show()

# 儲存圖表並輸出結果
output_file = "subject_average.png"
plt.savefig(output_file, dpi=150, bbox_inches="tight")
plt.show()