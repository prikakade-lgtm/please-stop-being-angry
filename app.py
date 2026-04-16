import streamlit as st
import random

# ---- PAGE CONFIG ----
st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CUTE CSS ----
st.markdown("""
    <style>
    body {
        background-color: #fff0f5;
    }
    .main {
        background-color: #fff0f5;
    }
    h1, h2, h3 {
        text-align: center;
        color: #ff4d6d;
    }
    .stButton>button {
        background-color: #ffd6e0;
        color: #333;
        border-radius: 20px;
        height: 3em;
        width: 100%;
        font-size: 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #ffb3c6;
    }
    .center-text {
        text-align: center;
        font-size: 18px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# ---- STATE ----
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---- HOME ----
if st.session_state.page == "home":
    st.markdown("<h1>hey you 😤</h1>", unsafe_allow_html=True)
    st.markdown('<p class="center-text">before you stay mad... click this</p>', unsafe_allow_html=True)

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"
        st.rerun()

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>step 1 🌸</h2>", unsafe_allow_html=True)
    st.markdown('<p class="center-text">take a deep breath (yes actually)</p>', unsafe_allow_html=True)

    if st.button("done 😶"):
        st.session_state.page = "step2"
        st.rerun()

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>important question 🧠</h2>", unsafe_allow_html=True)

    answer = st.radio("do you miss me?", ["no 😤", "maybe 😶", "okay fine 😒"])

    if st.button("submit"):
        st.markdown('<p class="center-text">analyzing...</p>', unsafe_allow_html=True)
        st.markdown('<p class="center-text">result: you are still attached 🤨</p>', unsafe_allow_html=True)

        if st.button("continue"):
            st.session_state.page = "step3"
            st.rerun()

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>...</h2>", unsafe_allow_html=True)
    st.markdown('<p class="center-text">i don’t like it when we’re like this</p>', unsafe_allow_html=True)

    if st.button("okay…"):
        st.session_state.page = "final"
        st.rerun()

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    if st.button("click to decide our fate"):
        outcomes = [
            "we stop fighting 😌",
            "you come hug me 🤗",
            "you text me right now 😏"
        ]
        st.success(random.choice(outcomes))

        if st.button("restart 🔄"):
            st.session_state.page = "home"
            st.rerun()
