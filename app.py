import streamlit as st
import random

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS (STRONG FIXES) ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

/* FULL BACKGROUND */
html, body, .stApp {
    background: linear-gradient(180deg, #ffe4ec, #ffd6e0) !important;
    font-family: 'Quicksand', sans-serif;
    color: #333 !important;
}

/* CENTER */
.block-container {
    max-width: 420px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

/* FORCE TEXT COLOR */
p, div, span, label {
    color: #333 !important;
}

/* HEADINGS */
h1 { color: #ff4d6d; }
h2 { color: #ff758f; }

/* BUTTONS */
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

    st.write("i know you’re mad… but click this.")

    if st.button("okay fine 🙄", key="home_btn"):
        st.session_state.page = "step1"

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>step 1 🌸</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done 😶", key="step1_btn"):
        st.session_state.page = "step2"

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>important question 🧠</h2>", unsafe_allow_html=True)

    st.write("be honest:")

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
        st.write("you are still emotionally attached 🤨")

        if st.button("continue", key="continue_btn"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>...</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.write("i don’t like it when we’re like this.")

    if st.button("fine 😶", key="step3_btn"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("you know what you need to do.")

    # 🎵 DRake
    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("fine… i’ll call you 😒📞", key="call_btn"):
        st.success("correct decision 😌")
        st.balloons()

    if st.button("restart 🔄", key="restart_btn"):
        st.session_state.page = "home"
