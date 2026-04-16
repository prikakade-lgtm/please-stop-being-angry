import streamlit as st
import random

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- FIXED + IMPROVED CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

/* FORCE LIGHT MODE BACKGROUND */
html, body, .stApp {
    background-color: #fff5f7 !important;
    color: #333 !important;
    font-family: 'Quicksand', sans-serif;
}

/* CENTER EVERYTHING */
.block-container {
    max-width: 500px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

/* HEADINGS */
h1 {
    color: #ff4d6d;
    font-size: 36px;
}
h2 {
    color: #ff758f;
}

/* BUTTONS (FIX SIZE ISSUE) */
.stButton>button {
    background-color: #ffd6e0;
    color: #333;
    border-radius: 25px;
    padding: 14px 20px;
    width: 100%;
    font-size: 16px;
    border: none;
    white-space: normal;
    height: auto;
    margin-top: 10px;
}

.stButton>button:hover {
    background-color: #ffb3c6;
    transform: scale(1.03);
}

/* TEXT */
.cute-text {
    font-size: 17px;
    margin-bottom: 15px;
}

/* RADIO ALIGN */
div[role="radiogroup"] {
    text-align: left;
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
    st.image("https://media.giphy.com/media/ICOgUNjpvO0PC/giphy.gif", width=180)

    st.markdown('<p class="cute-text">i know you’re mad… but this is important 😔</p>', unsafe_allow_html=True)

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"

    if st.button("no 😤"):
        st.write("wrong answer. try again.")

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>step 1 🌸</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.markdown('<p class="cute-text">take a deep breath 😌<br>don’t skip this.</p>', unsafe_allow_html=True)

    if st.button("done 😶"):
        st.session_state.page = "step2"

    if st.button("i refuse 😤"):
        st.write("you’re being dramatic again.")

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>important question 🧠</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", width=200)

    st.radio("do you miss me?", ["no 😤", "maybe 😶", "okay fine 😒"])

    if st.button("submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        st.markdown('<p class="cute-text">analysis complete 🧠<br>you are still emotionally attached 🤨</p>', unsafe_allow_html=True)

        st.write(random.choice([
            "don’t be dramatic 🙄",
            "this is a safe space (for you to stop being mad)",
            "you’re definitely smiling right now"
        ]))

        if st.button("okay continue 😒"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>...</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.markdown('<p class="cute-text">i don’t like it when we’re like this.</p>', unsafe_allow_html=True)

    if st.button("fine 😶"):
        st.session_state.page = "final"

    if st.button("still mad 😤"):
        st.write("ok but like… unnecessary.")

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", width=200)

    st.markdown('<p class="cute-text">choose wisely.</p>', unsafe_allow_html=True)

    if st.button("click to decide our fate"):
        st.success(random.choice([
            "correct answer. you may proceed 😌",
            "hug required. no exceptions 🤗",
            "you text me right now 😏"
        ]))

    if st.button("restart 🔄"):
        st.session_state.page = "home"
