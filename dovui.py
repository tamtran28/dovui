import streamlit as st
import pandas as pd
import random
import time

# ---------------- CẤU HÌNH GIAO DIỆN ----------------
st.set_page_config(page_title="🎯 Đố Vui Quay Số", layout="centered")

# CSS cho giao diện đẹp
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #c3ecb2 0%, #7de2fc 100%);
    color: #333333;
    font-family: 'Inter', sans-serif;
}
h1, h2, h3 {
    text-align: center;
    font-weight: 800;
    color: #1c3f60;
}
.stButton>button {
    background-color: #0072f5;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #0059b2;
    color: #f2f2f2;
}
.question-box {
    background-color: #ffffffdd;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TIÊU ĐỀ ----------------
st.title("🎡 MINIGAME ĐỐ VUI QUAY SỐ 🎯")
st.caption("Quay vòng – Trả lời – Tung bông chúc mừng 🎉")

# ---------------- DANH SÁCH CÂU HỎI ----------------
df = pd.DataFrame([
    {"Số": 1, "Câu hỏi": "Thủ đô của Việt Nam là gì?",
     "Đáp án đúng": "Hà Nội", "Đáp án sai 1": "TP.HCM", "Đáp án sai 2": "Huế", "Đáp án sai 3": "Đà Nẵng"},
    {"Số": 2, "Câu hỏi": "5 + 3 bằng bao nhiêu?",
     "Đáp án đúng": "8", "Đáp án sai 1": "6", "Đáp án sai 2": "9", "Đáp án sai 3": "7"},
    {"Số": 3, "Câu hỏi": "Biển lớn nhất thế giới là gì?",
     "Đáp án đúng": "Thái Bình Dương", "Đáp án sai 1": "Đại Tây Dương", "Đáp án sai 2": "Ấn Độ Dương", "Đáp án sai 3": "Bắc Băng Dương"},
    {"Số": 4, "Câu hỏi": "Ai là tác giả 'Truyện Kiều'?",
     "Đáp án đúng": "Nguyễn Du", "Đáp án sai 1": "Nguyễn Trãi", "Đáp án sai 2": "Hồ Xuân Hương", "Đáp án sai 3": "Lý Thường Kiệt"},
    {"Số": 5, "Câu hỏi": "Ngân hàng Eximbank được thành lập năm nào?",
     "Đáp án đúng": "1989", "Đáp án sai 1": "1990", "Đáp án sai 2": "1985", "Đáp án sai 3": "1995"},
])

# ---------------- VÒNG QUAY ----------------
st.markdown("## 🎲 Bấm nút để quay số may mắn")

if st.button("🎡 QUAY SỐ NGAY!"):
    with st.spinner("🎯 Đang quay vòng..."):
        spin_placeholder = st.empty()
        for _ in range(25):
            spin_placeholder.markdown(f"<h2 style='text-align:center;'>🎯 {random.randint(1,10)}</h2>", unsafe_allow_html=True)
            time.sleep(0.08)
        number = random.randint(1, 10)
        spin_placeholder.markdown(f"<h2 style='text-align:center; color:#d63384;'>✨ SỐ CỦA BẠN: {number} ✨</h2>", unsafe_allow_html=True)

    q = df[df["Số"] == number]
    if not q.empty:
        st.markdown(f"<div class='question-box'><h3>❓ {q.iloc[0]['Câu hỏi']}</h3></div>", unsafe_allow_html=True)
        correct = q.iloc[0]["Đáp án đúng"]
        options = [
            correct,
            q.iloc[0]["Đáp án sai 1"],
            q.iloc[0]["Đáp án sai 2"],
            q.iloc[0]["Đáp án sai 3"],
        ]
        random.shuffle(options)

        answer = st.radio("👉 Chọn đáp án của bạn:", options)

        if st.button("✅ Trả lời"):
            if answer == correct:
                st.success("🎉 Chính xác! Bạn giỏi quá 👏👏👏")
                st.balloons()
            else:
                st.error("❌ Sai mất rồi! Hãy thử lại ở lượt sau nhé.")
    else:
        st.warning("Không có câu hỏi cho số này.")
