import streamlit as st

name = st.text_input("請輸入姓名")
if name:
    st.write(f"你好, {name}!")

option = st.selectbox("請選擇一個選項", ["國文", "英文", "數學"])
if option:
    st.write(f"你選擇的科目是: {option}")

mode = st.radio("分析模式", ["高於門檻", "低於門檻"])
if mode:
    st.write(f"你選擇的分析模式是: {mode}")

threshold = st.slider("請選擇門檻值", 0, 100, 60)
if threshold >= 60:
    st.balloons()
else:
    st.snow()
st.write(f"你設定的門檻值是: {threshold}")

show_only = st.checkbox("只顯示符合條件的學生", value=True)
if show_only:
    st.write("啟動及格篩選，僅顯示符合條件的學生")

bonus = st.number_input("請輸入加分值", min_value=0, max_value=10, value=0)
if bonus:
    st.write(f"你設定的加分值是: {bonus}")
