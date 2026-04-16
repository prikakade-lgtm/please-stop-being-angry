import streamlit as st
import random
import time

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- SOFT AESTHETIC CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

html, body, .stApp {
    background: #fff7f9;
    font-family: 'Quicksand', sans-serif;
    color: #4a4a4a;
}

.block-container {
    max-width: 420px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

h1 { color: #e75480; }
h2 { color: #ff7aa2; }

.stButton>button {
    background-color: #ffe3ec;
    color: #4a4a4a;
    border-radius: 20px;
    padding: 12px;
    width: 100%;
    border: none;
    margin-top: 10px;
}

.stButton>button:hover {
    background-color: #ffd1e0;
}
</style>
""", unsafe_allow_html=True)

# ---- STATE ----
if "page" not in st.session_state:
    st.session_state.page = "home"

if "submitted" not in st.session_state:
    st.session_state.submitted = False

if "game_step" not in st.session_state:
    st.session_state.game_step = 1

# ---- HOME ----
if st.session_state.page == "home":
    st.markdown("<h1>hey you 😤</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", width=180)

    st.write("okay listen… just click this.")

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done"):
        st.session_state.page = "step2"

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>one question 🧠</h2>", unsafe_allow_html=True)

    st.write("do you miss me?")

    choice = st.radio("", [
        "no 😤",
        "maybe 😶",
        "okay fine 😒"
    ])

    if st.button("submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        if choice.startswith("no"):
            st.write("be serious 😭")
        elif choice.startswith("maybe"):
            st.write("hmm… progress.")
        else:
            st.write("yeah exactly.")

        if st.button("continue"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.write("i don’t like it when we’re like this.")
    st.write("i miss you btw.")

    if st.button("fine"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)
    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("fine… what do i have to do 😒"):
        st.session_state.page = "game"

# ---- GAME ----
elif st.session_state.page == "game":
    st.markdown("<h2>mini game 🎮</h2>", unsafe_allow_html=True)
    st.write("win this to unlock the call.")

    # countdown
    for i in range(3, 0, -1):
        st.write(f"starting in {i}...")
        time.sleep(0.5)

    # ---- QUESTION FLOW ----
    if st.session_state.game_step == 1:
        st.write("question 1:")

        if st.button("stay mad 😤"):
            st.warning("wrong. try again.")

        if st.button("call her 📞"):
            st.session_state.game_step = 2

    elif st.session_state.game_step == 2:
        st.write("question 2:")

        if st.button("ignore her 🙄"):
            st.error("you lost 😭 restart.")
            st.session_state.game_step = 1

        if st.button("fix it 😌"):
            st.session_state.page = "win"

# ---- WIN ----
elif st.session_state.page == "win":
    st.markdown("<h2>you win 🏆</h2>", unsafe_allow_html=True)
    st.write("okay… you’ve proven yourself.")

    if st.button("unlock call 📞"):
        st.session_state.page = "call"

# ---- CALL ----
elif st.session_state.page == "call":
    st.markdown("<h1>📞 incoming call…</h1>", unsafe_allow_html=True)

    st.write("you have no choice now 😌")

    st.markdown("""
    <div style="font-size:30px;">
    💖 💕 💗 💓 💞 💘 💝
    </div>
    """, unsafe_allow_html=True)

    st.success("good decision.")

    st.markdown("📞 call me now: +91 9819271926")
