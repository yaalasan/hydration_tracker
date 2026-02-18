import streamlit as st
from datetime import datetime, date, time
import pytz

st.markdown("""
<link rel="manifest" href="manifest.json">
<meta name="theme-color" content="#ff4da6">
""", unsafe_allow_html=True)


st.set_page_config(page_title="Bossan’s Hydration 💖", page_icon="🌸")

# --- Cute but readable theme ---
st.markdown("""
<style>
.stApp {
    background-color: #ffd6e8;
    color: #4d004d;
    font-family: 'Arial';
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

st.title("Bossan’s Hydration 🌙💖")
st.markdown("<h3>Gentle Reminder ✨</h3>", unsafe_allow_html=True)

# --- China Time ---
china = pytz.timezone("Asia/Shanghai")
now = datetime.now(china)

# --- Reminder Times ---
iftar_time = time(18, 30)
suhoor_time = time(4, 30)

st.markdown(" Stay glowing & hydrated 🌙")

if now.hour == iftar_time.hour:
    st.success("✨ Time to hydrate after Iftar 💧")

elif now.hour == suhoor_time.hour:
    st.info("🌅 Drink water before Suhoor 💖")

# --- Daily Tracking ---
today = str(date.today())

if "day" not in st.session_state:
    st.session_state.day = today
    st.session_state.glasses = 0

if st.session_state.day != today:
    st.session_state.day = today
    st.session_state.glasses = 0

target = 8

# --- FIXED progress ---
progress = min(st.session_state.glasses / target, 1.0)
st.progress(progress)

st.markdown(f"<h3>{st.session_state.glasses} / {target} glasses 💧</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    if st.button("I drank a glass 💧"):
        st.session_state.glasses += 1

with col2:
    if st.button(" Remove one "):
        if st.session_state.glasses > 0:
            st.session_state.glasses -= 1

# --- Cute Messages ---
if st.session_state.glasses == 0:
    st.info("Start your glow journey 🌸")

elif st.session_state.glasses < 4:
    st.warning("Good start! Keep sipping 💕")

elif st.session_state.glasses < 7:
    st.success("You're doing amazing ✨")

elif st.session_state.glasses >= target:
    st.balloons()
    st.success("Hydration queen 👑 Mission complete!")

st.markdown("<p style='text-align: center;'>Drink water and stay strong!🕷️ </p>", unsafe_allow_html=True)

