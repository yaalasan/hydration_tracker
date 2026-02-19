import streamlit as st
from datetime import datetime, date, time
import pytz
import os
import json

st.set_page_config(page_title="Bossan’s Hydration 💖", page_icon="🌸")

# ---------------- SAVE DATA ----------------

DATA_FILE = "glasses.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"glasses": 0, "last_day": str(date.today())}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

data = load_data()

# ---------------- DAILY RESET ----------------

today = str(date.today())

if data["last_day"] != today:
    data["last_day"] = today
    data["glasses"] = 0
    save_data(data)

# ---------------- SESSION LOAD ----------------

if "glasses" not in st.session_state:
    st.session_state.glasses = data["glasses"]

# ---------------- THEME ----------------

st.markdown("""
<style>
.stApp {
    background-color: #ffd6e8;
    color: #4d004d;
    font-family: Arial;
}
h1 {
    text-align: center;
    color: #b30059;
}
h3 {
    text-align: center;
    color: #800040;
}
div.stButton > button {
    background-color: #ff99cc;
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------

st.title("Bossan’s Hydration 🌙💖")
st.markdown("<h3>Stay glowing & hydrated ✨</h3>", unsafe_allow_html=True)

# ---------------- NOTIFICATION SCRIPT ----------------

st.markdown("""
<script>
function remind(msg) {
    if (Notification.permission === "granted") {
        new Notification(msg);
    }
}
if (Notification.permission !== "granted") {
    Notification.requestPermission();
}
</script>
""", unsafe_allow_html=True)

# ---------------- RAMADAN REMINDERS ----------------

china = pytz.timezone("Asia/Shanghai")
now = datetime.now(china)

iftar_time = time(18, 30)
suhoor_time = time(4, 30)

if now.hour == iftar_time.hour:
    st.success("✨ Time to hydrate after Iftar 💧")
    st.markdown("<script>remind('Bossan 💖 Time to drink water after Iftar!');</script>", unsafe_allow_html=True)

elif now.hour == suhoor_time.hour:
    st.info("🌅 Drink water before Suhoor 💖")
    st.markdown("<script>remind('Bossan 💖 Drink water before Suhoor!');</script>", unsafe_allow_html=True)

# ---------------- PROGRESS ----------------

target = 8
progress = min(st.session_state.glasses / target, 1.0)

st.progress(progress)
st.markdown(f"<h3>{st.session_state.glasses} / {target} glasses 💧</h3>", unsafe_allow_html=True)

# ---------------- BUTTONS ----------------

col1, col2 = st.columns(2)

with col1:
    if st.button("I drank a glass 💧", use_container_width=True):
        st.session_state.glasses += 1
        data["glasses"] = st.session_state.glasses
        save_data(data)
        st.rerun()

with col2:
    if st.button("Remove one", use_container_width=True):
        if st.session_state.glasses > 0:
            st.session_state.glasses -= 1
            data["glasses"] = st.session_state.glasses
            save_data(data)
            st.rerun()

# ---------------- CUTE MESSAGES ----------------

if st.session_state.glasses == 0:
    st.info("Start your glow journey 🌸")

elif st.session_state.glasses < 4:
    st.warning("Good start! Keep sipping 💕")

elif st.session_state.glasses < 7:
    st.success("You're doing amazing ✨")

elif st.session_state.glasses >= target:
    st.balloons()
    st.success("Hydration queen 👑 Mission complete!")

st.markdown("<p style='text-align: center;'>Drink water and stay strong 🕷️</p>", unsafe_allow_html=True)
