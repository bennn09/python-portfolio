import streamlit as st

scores = [
    {"name": "小安", "subject": "數學", "score": 85},
    {"name": "小華", "subject": "數學", "score": 58},
    {"name": "小美", "subject": "英文", "score": 92},
    {"name": "小傑", "subject": "英文", "score": 65},
]

st.title("互動式成績查詢")
name = st.text_input("輸入姓名關鍵字")
subject = st.selectbox("選擇科目", ["全部", "數學", "英文"])
threshold = st.slider("最低分數", 0, 100, 60)

result = []  # 準備一個空籃子
for item in scores:
    if subject != "全部" and item["subject"] != subject:
        continue
    if name and name not in item["name"]:
        continue
    if item["score"] >= threshold:
        result.append(item)  # 放進籃子裡
st.write("符合條件的資料：")
if result:
    st.write(result)
else:
    st.warning("沒有符合條件的資料")
