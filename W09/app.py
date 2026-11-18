import streamlit as st
import streamlit as st

st.title("我的學習名片( ᵔ ᗢ ᵔ )y")
st.subheader("歡迎來到我的個人學習空間！")
st.subheader("About Me")
st.write("大家好，我叫Bianca，目前就讀於國立馬公高中，今年17歲")
st.write("對於跑車、JDM很感興趣")

st.write("我的目標: 成為一名優秀的設計師，不斷學習新技術。")


name = st.text_input("請輸入你的姓名")
topic = st.text_input("請輸入你感興趣的資訊主題")

if st.button("建立我的學習名片"):
    if name.strip() != "":
        st.success("資料已送出，學習名片建立成功！")
        st.write(f"姓名: {name}")
        st.write(f"感興趣的資訊主題: {topic}")
        st.write("現在正在學習中Python")
    else:
        st.error("請輸入你的姓名:red[*]")
