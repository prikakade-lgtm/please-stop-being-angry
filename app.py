import streamlit as st
import random
import time

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

html, body, .stApp {
    background: linear-gradient(180deg, #ffe4ec, #ffd6e0) !important;
    font-family: 'Quicksand', sans-serif;
    color: #333 !important;
}

.block-container {
    max-width: 420px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

h1 { color: #ff4d6d; }
h2 { color: #ff758f; }

.stButton>button {
    background-color: #ffd6e0;
    color: #333 !important;
    border-radius: 25px;
    padding: 14px;
    width: 100%;
    border: none;
    margin-top: 10px;
}

.stButton>button:hover {
    background-color: #ffb3c6;
}
</style>
""", unsafe_allow_html=True)

# ---- STATE ----
if "page" not in st.session_state:
    st.session_state.page = "home"

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# ---- HOME ----
if st.session_state.page == "home":
    st.markdown("<h1>hey you 😤</h1>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", width=180)

    st.write("okay listen… just click this.")

    if st.button("okay fine 🙄", key="home_btn"):
        st.session_state.page = "step1"

    if st.button("no 😤", key="home_no"):
        st.write("wrong answer. try again 🙄")

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done 😶", key="step1_btn"):
        st.session_state.page = "step2"

    if st.button("i refuse 😤", key="step1_refuse"):
        st.write("you’re being dramatic again.")

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>one question 🧠</h2>", unsafe_allow_html=True)

    st.write("do you miss me?")

    choice = st.radio(
        "",
        [
            "no 😤 (lying)",
            "maybe 😶 (hmm)",
            "okay fine 😒 (correct)"
        ],
        key="radio_q"
    )

    if st.button("submit", key="submit_btn"):
        st.session_state.submitted = True

    if st.session_state.submitted:

        if choice.startswith("no"):
            st.write("be serious for one second 😭")
        elif choice.startswith("maybe"):
            st.write("hmm… progress.")
        else:
            st.write("yeah exactly.")

        st.write("you are still emotionally attached 🤨")

        st.write(random.choice([
            "don’t be dramatic 🙄",
            "this is a safe space (for you to stop being mad)",
            "you’re definitely smiling right now"
        ]))

        if st.button("okay continue 😒", key="continue_btn"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.write("i don’t like it when we’re like this.")

    st.write(random.choice([
        "i miss you btw.",
        "this is dumb, we should not be fighting.",
        "you’re my favorite person, even when you’re annoying."
    ]))

    if st.button("fine 😶", key="step3_btn"):
        st.session_state.page = "final"

    if st.button("still mad 😤", key="step3_mad"):
        st.write("ok but like… unnecessary 🙄")


# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("i don’t care about being right… i just don’t like us like this.")

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("fine… what do i have to do 😒", key="start_game"):
        st.session_state.page = "game"

# ---- GAME ----
elif st.session_state.page == "game":
    st.markdown("<h2>mini game 🎮</h2>", unsafe_allow_html=True)

    st.write("win this and you get to call me.")

    st.image("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif", width=180)

    st.write("question 1:")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("stay mad 😤", key="wrong1"):
            st.write("embarrassing choice.")

    with col2:
        if st.button("call her 📞", key="correct1"):
            st.session_state.page = "game2"

    st.write("---")

    st.write("question 2:")

    col3, col4 = st.columns(2)

    with col3:
        if st.button("ignore her 🙄", key="wrong2"):
            st.write("you’re really committed to being annoying huh")

    with col4:
        if st.button("fix it 😌", key="correct2"):
            st.session_state.page = "win"

# ---- WIN ----
elif st.session_state.page == "win":
    st.markdown("<h2>you win 🏆</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", width=200)

    st.write("okay… you’ve proven yourself.")

    if st.button("unlock call 📞", key="unlock"):
        st.session_state.page = "call"

# ---- CALL ----
elif st.session_state.page == "call":
    st.markdown("<h1>📞 incoming call…</h1>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=200)

    st.write("you have no choice now 😌")

    st.markdown("""
    <div style="font-size:40px;">
    💖 💕 💗 💓 💞 💘 💝 💖 💕 💗
    </div>
    """, unsafe_allow_html=True)

    st.success("good decision. call me.")

    st.markdown("📞 call her now: +91 9819271926")
