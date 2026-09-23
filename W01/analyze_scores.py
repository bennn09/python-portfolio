scores=[78,92,59,88,73,95,81,69,84,90]

hightest=max(scores)
lowest=min(scores)
average=sum(scores)/len(scores)
top3=sorted(scores,reverse=True)[:3]

print("=== 成績分析 ===")
print("資料筆數:",len(scores))
print("最高分:",hightest)
print("最低分:",lowest)
print("平均:",average)
print("前三名:",top3)

passed=[
score for score in scores
if score>=60
]
print("及格人數:",len(passed)) #輸出:9

ranking=sorted(scores,reverse=True)
print("高到低成績排序:",ranking)