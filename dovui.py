import streamlit as st
import pandas as pd
import random
import time

st.set_page_config(page_title="🎯 Đố Vui Quay Số", layout="centered")

# ======================== CSS GIAO DIỆN ========================
st.markdown("""
<style>
body { background-color: #f5f9ff; font-family: 'Inter', sans-serif; }
h1, h2, h3 { text-align: center; color: #0072f5; font-weight: 800; }
.card {
    background: white;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    padding: 25px;
    margin: 20px auto;
    text-align: center;
    width: 90%;
}
.spin-btn {
    background: #28a745;
    color: white;
    font-weight: bold;
    border: none;
    border-radius: 12px;
    padding: 12px 30px;
    cursor: pointer;
    font-size: 18px;
}
.spin-btn:hover { background: #1e7e34; }
.option-btn {
    display: block;
    width: 100%;
    background-color: #fff;
    border: 2px solid #0072f5;
    color: #0072f5;
    font-weight: 600;
    border-radius: 10px;
    padding: 8px;
    margin: 5px 0;
    cursor: pointer;
}
.option-btn:hover {
    background-color: #0072f5;
    color: white;
}
.correct { background: #c8f7c5; padding: 5px; border-radius: 8px; font-weight: bold; }
.wrong { background: #ffbaba; padding: 5px; border-radius: 8px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ======================== DỮ LIỆU CÂU HỎI ========================
df = pd.DataFrame([
    {"Số": 1, "Câu hỏi": "Hồ Gươm nằm ở đâu?", 
     "Đáp án đúng": "Hà Nội", "Đáp án sai 1": "Đà Nẵng", "Đáp án sai 2": "Huế", "Đáp án sai 3": "Hồ Chí Minh"},
    {"Số": 2, "Câu hỏi": "Thủ đô của Nhật Bản là gì?", 
     "Đáp án đúng": "Tokyo", "Đáp án sai 1": "Kyoto", "Đáp án sai 2": "Osaka", "Đáp án sai 3": "Nagoya"},
    {"Số": 3, "Câu hỏi": "Ngân hàng Eximbank thành lập năm nào?", 
     "Đáp án đúng": "1989", "Đáp án sai 1": "1990", "Đáp án sai 2": "1985", "Đáp án sai 3": "1995"},
    {"Số": 4, "Câu hỏi": "1 năm có bao nhiêu tháng có 31 ngày?",
     "Đáp án đúng": "7", "Đáp án sai 1": "6", "Đáp án sai 2": "5", "Đáp án sai 3": "8"},
])

# ======================== SESSION STATE ========================
if "turn" not in st.session_state:
    st.session_state.turn = 1
if "score" not in st.session_state:
    st.session_state.score = {1: 0, 2: 0}
if "used_numbers" not in st.session_state:
    st.session_state.used_numbers = []
if "current_question" not in st.session_state:
    st.session_state.current_question = None
if "spin_done" not in st.session_state:
    st.session_state.spin_done = False

# ======================== GIAO DIỆN ========================
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.markdown(f"<h2>Lượt Quay Của <span style='color:#0052cc;'>Người Chơi {st.session_state.turn}</span></h2>", unsafe_allow_html=True)

if not st.session_state.spin_done:
    st.markdown("<div style='font-size:80px;color:#0072f5;'>❓</div>", unsafe_allow_html=True)
    st.write("Bấm nút để quay số, câu hỏi tương ứng sẽ xuất hiện.")
    if st.button("🎡 QUAY NGAY", use_container_width=True):
        with st.spinner("Đang quay..."):
            for _ in range(15):
                st.write(f"⏳ Số {random.randint(1, len(df))}")
                time.sleep(0.05)
            number = random.randint(1, len(df))
        if number in st.session_state.used_numbers:
            st.warning("⚠️ Câu hỏi này đã được trả lời, hãy quay lại!")
        else:
            st.session_state.spin_done = True
            st.session_state.current_question = number
            st.session_state.used_numbers.append(number)
    st.markdown("</div>", unsafe_allow_html=True)

# ======================== HIỂN THỊ CÂU HỎI ========================
if st.session_state.spin_done and st.session_state.current_question:
    q = df[df["Số"] == st.session_state.current_question].iloc[0]
    st.markdown(f"<div class='card'><h3>❓ Câu {q['Số']} (Người Chơi {st.session_state.turn}): {q['Câu hỏi']}</h3></div>", unsafe_allow_html=True)
    
    options = [q["Đáp án đúng"], q["Đáp án sai 1"], q["Đáp án sai 2"], q["Đáp án sai 3"]]
    random.shuffle(options)
    choice = st.radio("Chọn đáp án:", options)
    
    if st.button("✅ Trả Lời"):
        if choice == q["Đáp án đúng"]:
            st.success("🎉 Chúc mừng! Bạn đã trả lời chính xác.")
            st.session_state.score[st.session_state.turn] += 1
            st.balloons()
        else:
            st.error(f"❌ Sai rồi! Đáp án đúng là: {q['Đáp án đúng']}")
        
        st.session_state.spin_done = False
        st.session_state.turn = 2 if st.session_state.turn == 1 else 1
        remaining = len(df) - len(st.session_state.used_numbers)
        st.info(f"🔄 Quay tiếp! Lượt Người Chơi {st.session_state.turn} – Còn {remaining} câu hỏi.")

# ======================== ĐIỂM ========================
st.markdown("</div>", unsafe_allow_html=True)
st.markdown(f"<h4>🏆 Điểm số: Người Chơi 1 = {st.session_state.score[1]} | Người Chơi 2 = {st.session_state.score[2]}</h4>", unsafe_allow_html=True)
