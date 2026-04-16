import streamlit as st
import random

# ---- PAGE CONFIG ----
st.set_page_config(page_title="for u 🙈", layout="centered")

# ---- CUTE CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

html, body, [class*="css"]  {
    font-family: 'Quicksand', sans-serif;
    background-color: #fff5f7;
}

/* Center content */
.block-container {
    text-align: center;
    padding-top: 3rem;
}

/* Titles */
h1 {
    color: #ff4d6d;
    font-size: 42px;
}
h2 {
    color: #ff758f;
}

/* Buttons */
.stButton>button {
    background-color: #ffd6e0;
    color: #333;
    border-radius: 25px;
    height: 3.2em;
    width: 80%;
    margin: auto;
    display: block;
    font-size: 16px;
    border: none;
    transition: 0.2s;
}

.stButton>button:hover {
    background-color: #ffb3c6;
    transform: scale(1.05);
}

/* Text */
.cute-text {
    font-size: 18px;
    color: #555;
    margin-bottom: 20px;
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
    
    st.image("https://media.giphy.com/media/MDJ9IbxxvDUQM/giphy.gif", width=200)
    
    st.markdown('<p class="cute-text">i know you’re mad… but just click this 🙄</p>', unsafe_allow_html=True)

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>step 1 🌸</h2>", unsafe_allow_html=True)
    
    st.markdown('<p class="cute-text">take a deep breath 😌<br>yes, i’m serious.</p>', unsafe_allow_html=True)

    st.markdown("💖 💖 💖")

    if st.button("done 😶"):
        st.session_state.page = "step2"

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>important question 🧠</h2>", unsafe_allow_html=True)

    st.markdown("💭")

    st.radio("do you miss me?", ["no 😤", "maybe 😶", "okay fine 😒"])

    if st.button("submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        st.markdown('<p class="cute-text">analysis complete 🧠<br>you are still emotionally attached 🤨</p>', unsafe_allow_html=True)

        st.write(random.choice([
            "don’t be dramatic 🙄",
            "this is a safe space (for you to stop being mad)",
            "you’re lowkey smiling right now"
        ]))

        if st.button("continue"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>...</h2>", unsafe_allow_html=True)

    st.markdown('<p class="cute-text">i don’t like it when we’re like this.</p>', unsafe_allow_html=True)

    st.markdown("💖 💖 💖")

    if st.button("okay…"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.markdown('<p class="cute-text">choose wisely.</p>', unsafe_allow_html=True)

    if st.button("click to decide our fate"):
        st.success(random.choice([
            "correct answer. you may proceed 😌",
            "hug required. no exceptions 🤗",
            "you text me right now 😏"
        ]))

    if st.button("restart 🔄"):
        st.session_state.page = "home"
