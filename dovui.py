import streamlit as st
import pandas as pd
import random
import time

# ---------------- CẤU HÌNH GIAO DIỆN ----------------
st.set_page_config(page_title="🎯 Minigame Đố Vui Quay Số", layout="centered")
st.title("🎡 MINIGAME ĐỐ VUI QUAY SỐ 🎯")
st.caption("Người chơi quay số để chọn câu hỏi. Trả lời đúng sẽ được tung bông chúc mừng 🎉")

# ---------------- DANH SÁCH CÂU HỎI ----------------
df = pd.DataFrame([
    {"Số": 1, "Câu hỏi": "Thủ đô của Việt Nam là gì?",
     "Đáp án đúng": "Hà Nội", "Đáp án sai 1": "TP.HCM", "Đáp án sai 2": "Huế", "Đáp án sai 3": "Đà Nẵng"},
    {"Số": 2, "Câu hỏi": "5 + 3 bằng bao nhiêu?",
     "Đáp án đúng": "8", "Đáp án sai 1": "6", "Đáp án sai 2": "9", "Đáp án sai 3": "7"},
    {"Số": 3, "Câu hỏi": "Biển lớn nhất thế giới là gì?",
     "Đáp án đúng": "Thái Bình Dương", "Đáp án sai 1": "Đại Tây Dương", "Đáp án sai 2": "Ấn Độ Dương", "Đáp án sai 3": "Bắc Băng Dương"},
    {"Số": 4, "Câu hỏi": "Sông dài nhất Việt Nam là?",
     "Đáp án đúng": "Sông Mekong", "Đáp án sai 1": "Sông Hồng", "Đáp án sai 2": "Sông Đồng Nai", "Đáp án sai 3": "Sông Đà"},
    {"Số": 5, "Câu hỏi": "Ai là tác giả 'Truyện Kiều'?",
     "Đáp án đúng": "Nguyễn Du", "Đáp án sai 1": "Nguyễn Trãi", "Đáp án sai 2": "Hồ Xuân Hương", "Đáp án sai 3": "Lý Thường Kiệt"},
    {"Số": 6, "Câu hỏi": "1 năm có bao nhiêu tháng có 31 ngày?",
     "Đáp án đúng": "7", "Đáp án sai 1": "6", "Đáp án sai 2": "8", "Đáp án sai 3": "5"},
    {"Số": 7, "Câu hỏi": "Ngân hàng Eximbank được thành lập năm nào?",
     "Đáp án đúng": "1989", "Đáp án sai 1": "1990", "Đáp án sai 2": "1985", "Đáp án sai 3": "1995"},
    {"Số": 8, "Câu hỏi": "Chất khí chúng ta hít thở để sống là?",
     "Đáp án đúng": "Oxy", "Đáp án sai 1": "Nitơ", "Đáp án sai 2": "CO2", "Đáp án sai 3": "Hydro"},
    {"Số": 9, "Câu hỏi": "Trái Đất quay quanh gì?",
     "Đáp án đúng": "Mặt Trời", "Đáp án sai 1": "Mặt Trăng", "Đáp án sai 2": "Sao Hỏa", "Đáp án sai 3": "Sao Kim"},
    {"Số": 10, "Câu hỏi": "Ai là người phát minh ra bóng đèn?",
     "Đáp án đúng": "Thomas Edison", "Đáp án sai 1": "Albert Einstein", "Đáp án sai 2": "Newton", "Đáp án sai 3": "Tesla"},
])

# ---------------- VÒNG QUAY ----------------
if st.button("🎲 Quay số (1–10)"):
    with st.spinner("Đang quay... 🎡"):
        for i in range(20):
            st.write(f"⏳ Đang quay... số {random.randint(1, 10)}")
            time.sleep(0.1)
        number = random.randint(1, 10)
    st.subheader(f"👉 Số được quay: {number}")

    # ---------------- CÂU HỎI ----------------
    q = df[df["Số"] == number]
    if not q.empty:
        question = q.iloc[0]["Câu hỏi"]
        correct = q.iloc[0]["Đáp án đúng"]
        options = [
            correct,
            q.iloc[0]["Đáp án sai 1"],
            q.iloc[0]["Đáp án sai 2"],
            q.iloc[0]["Đáp án sai 3"],
        ]
        random.shuffle(options)

        st.markdown(f"### ❓ {question}")
        answer = st.radio("Chọn câu trả lời:", options)

        if st.button("✅ Trả lời"):
            if answer == correct:
                st.success("🎉 Chính xác! Chúc mừng bạn!")
                st.balloons()
            else:
                st.error("❌ Sai rồi! Hãy thử lại ở lượt sau.")
    else:
        st.warning("Không tìm thấy câu hỏi tương ứng với số này.")
