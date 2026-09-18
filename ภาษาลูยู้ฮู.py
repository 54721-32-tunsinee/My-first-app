import streamlit as st

st.title("เกมทายภาษาลูหมวดคำพูดในชีวิตประจำวัน")

# ----------------------------------------------------
# กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

if "is_ended" not in st.session_state:
    st.session_state.is_ended = False


# ----------------------------------------------------
# ฟังก์ชันเคลียร์ค่าเมื่อกดปุ่มเริ่มใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.is_ended = False


# ----------------------------------------------------
# ฟังก์ชันแสดงผลลัพธ์
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):

    st.balloons()

    score = 0

    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    # ข้อ 1
    if u_ans1 == "หิวข้าว":
        st.success("✅ ข้อ 1: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 1: ยังไม่ถูกต้อง (คุณตอบ '{u_ans1}')")

    # ข้อ 2
    if u_ans2 == "วันนี้งานเยอะมาก":
        st.success("✅ ข้อ 2: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 2: ยังไม่ถูกต้อง (คุณตอบ '{u_ans2}')")

    # ข้อ 3
    if u_ans3 == "ปวดหัวเพราะเจองาน":
        st.success("✅ ข้อ 3: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 3: ยังไม่ถูกต้อง (คุณตอบ '{u_ans3}')")

    # ข้อ 4
    if u_ans4 == "หิวข้าวแต่ไม่มีเงิน":
        st.success("✅ ข้อ 4: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 4: ยังไม่ถูกต้อง (คุณตอบ '{u_ans4}')")

    # ข้อ 5
    if u_ans5 == "หวัดดี":
        st.success("✅ ข้อ 5: ถูกต้อง")
        score += 1
    else:
        st.error(f"❌ ข้อ 5: ยังไม่ถูกต้อง (คุณตอบ '{u_ans5}')")

    # สรุปคะแนน
    st.info(f"🏆 ได้คะแนนรวม: {score} คะแนน")

    if score == 5:
        st.success("🎉 You win!")
    else:
        st.error("💀 You lose!")


# ----------------------------------------------------
# ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)


# ----------------------------------------------------
# ช่องรับคำตอบ
# ----------------------------------------------------
ans1 = st.text_input(
    "ข้อ 1: “หลิวหู ล้าวขู้” แปลว่าอะไร",
    value=st.session_state.ans1_val,
)

ans2 = st.text_input(
    "ข้อ 2: “ลันวูน ลี้นู้ ลานงูน เลอะยู้ ลากมูก” แปลงเป็นภาษาไทยว่าอะไร?",
    value=st.session_state.ans2_val,
)

ans3 = st.text_input(
    "ข้อ 3: “หลวดปูด หลัวหู เลาะพรุ เลอจู ลานงูน” แปลว่าอะไร?",
    value=st.session_state.ans3_val,
)

ans4 = st.text_input(
    "ข้อ 4: “หิวข้าว แต่‘ไล่มู ลีมู’เงิน” ประโยคนี้หมายถึงอะไร?",
    value=st.session_state.ans4_val,
)

ans5 = st.text_input(
    "ข้อ 5: “หลัดหวุด ลีดู” หมายถึง ",
    value=st.session_state.ans5_val,
)


# ----------------------------------------------------
# บันทึกคำตอบล่าสุด
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# ----------------------------------------------------
# ปุ่มส่งคำตอบ
# ----------------------------------------------------
if not st.session_state.get("is_ended", False):

    if st.button("📥 ส่งคำตอบ"):
        st.session_state.is_ended = True
        st.rerun()


# ----------------------------------------------------
# แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):

    show_result_dialog(
        st.session_state.ans1_val,
        st.session_state.ans2_val,
        st.session_state.ans3_val,
        st.session_state.ans4_val,
        st.session_state.ans5_val
    )
