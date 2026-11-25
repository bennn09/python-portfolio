import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Student Score Explorer", page_icon="📊", layout="centered"
)
st.title("Student Score Explorer")
st.write("互動式學習成績分析 App")
st.caption("以下資料為教學用模擬資料，並非真實學生資料。")
data = {
    "name": [
        "小安",
        "小華",
        "小美",
        "小傑",
        "小琳",
        "小宇",
        "小晴",
        "小豪",
        "小君",
        "小恩",
        "小哲",
        "小涵",
    ],
    "class_name": [
        "101",
        "101",
        "101",
        "101",
        "102",
        "102",
        "102",
        "102",
        "101",
        "102",
        "101",
        "102",
    ],
    "Chinese": [85, 72, 91, 58, 77, 88, 69, 95, 62, 81, 74, 90],
    "English": [78, 55, 93, 66, 82, 71, 59, 88, 73, 96, 64, 84],
    "Math": [92, 48, 76, 65, 83, 57, 94, 72, 61, 89, 54, 80],
}
df = pd.DataFrame(data)

st.subheader("一、設定分析條件")
keyword = st.text_input("姓名關鍵字", placeholder="例如：小安")
class_choice = st.selectbox("選擇班級", ["全部", "101", "102"])
subject_choice = st.selectbox("選擇分析科目", ["國文", "英文", "數學"])
subject_columns = {"國文": "Chinese", "英文": "English", "數學": "Math"}
score_column = subject_columns[subject_choice]
mode = st.radio("選擇分析方式", ["高於或等於門檻", "低於門檻"])
threshold = st.slider("設定分數門檻", min_value=0, max_value=100, value=60)
show_only = st.checkbox("只顯示符合條件的學生", value=True)

st.subheader("二、分析結果")

result_df = df.copy()

if keyword:
    result_df = result_df[result_df["name"].str.contains(keyword, na=False)]

if class_choice != "全部":
    result_df = result_df[result_df["class_name"] == class_choice]

if mode == "高於或等於門檻":
    result_df = result_df[result_df[score_column] >= threshold]
else:
    result_df = result_df[result_df[score_column] < threshold]

total_count = len(result_df)
st.write("分析科目：", subject_choice, "｜分析方式：", mode, "｜分數門檻：", threshold)
st.write("符合條件人數：", total_count)

if total_count > 0:
    average_score = result_df[score_column].mean()
    st.write("符合條件資料的平均分數：", round(average_score, 2))
else:
    st.warning("沒有符合條件的資料，無法計算平均分數。")

if show_only:
    st.write("符合條件的學生資料：")
    st.dataframe(
        result_df[["name", "class_name", score_column]], use_container_width=True
    )
else:
    st.write("目前篩選後的資料：")
    st.dataframe(result_df, use_container_width=True)

with st.expander("查看資料欄位說明"):
    st.write(
        "name：學生姓名｜class_name：班級｜Chinese：國文｜English：英文｜Math：數學"
    )
    st.write("目前共有", len(df), "筆模擬資料。")
