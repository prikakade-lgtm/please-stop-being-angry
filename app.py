import streamlit as st
import random
import time

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

html, body, .stApp {
    background-color: #ffdce5 !important;
    font-family: 'Quicksand', sans-serif;
    color: black !important;
}

.block-container {
    max-width: 420px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

h1, h2 { color: black; }

.stButton>button {
    background-color: #ff4d6d;
    color: white !important;
    border-radius: 25px;
    padding: 16px;
    width: 100%;
    border: none;
    margin-top: 10px;
    font-size: 16px;
}

.stButton>button:active {
    transform: scale(0.96);
}

.stButton>button:hover {
    background-color: #e6395c;
}

/* RADIO TEXT BLACK */
div[role="radiogroup"] label {
    color: black !important;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# ---- STATE ----
if "page" not in st.session_state:
    st.session_state.page = "home"

if "message" not in st.session_state:
    st.session_state.message = ""

# ---- HELPERS ----
def show_message(text):
    st.session_state.message = text

def clear_message():
    st.session_state.message = ""

# ---- HOME ----
if st.session_state.page == "home":
    st.markdown("<h1>hey you 😤</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", width=180)

    st.write("okay listen… just click this.")

    if st.button("okay fine 🙄"):
        clear_message()
        st.session_state.page = "step1"
        st.rerun()

    if st.button("no 😤"):
        show_message("wrong answer. try again 🙄")

    if st.session_state.message:
        st.write(st.session_state.message)

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done 😶"):
        clear_message()
        st.session_state.page = "step2"
        st.rerun()

    if st.button("i refuse 😤"):
        show_message("you’re being dramatic again 😭")

    if st.session_state.message:
        st.write(st.session_state.message)

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
        if choice.startswith("no"):
            show_message("no?? 😭 be serious. we both know that’s not true.\nthis attitude is not convincing anyone btw 🙄")

        elif choice.startswith("maybe"):
            show_message("maybe?? 🤨 okay… we’re getting somewhere.\nthat was dangerously close to honesty 😌")

        else:
            clear_message()
            show_message("okay fine 😒?? wow look who’s being real for once.\nsee? that wasn’t so hard 😏")
            st.session_state.page = "step3"
            st.rerun()

    if st.session_state.message:
        st.write(st.session_state.message)

        st.write(random.choice([
            "don’t be dramatic 🙄",
            "this could’ve been over 10 minutes ago btw",
            "you miss me. let’s not lie today.",
            "this is lowkey embarrassing for you 😭",
            "you’re definitely smiling right now"
        ]))

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    text_placeholder = st.empty()
    for t in ["...", "wait...", "okay listen..."]:
        text_placeholder.write(t)
        time.sleep(0.5)

    text_placeholder.write("i don’t like it when we’re like this.")

    st.write(random.choice([
        "i miss you btw.",
        "this is dumb, we should not be fighting.",
        "you’re my favorite person, even when you’re annoying."
    ]))

    if st.button("fine 😶"):
        st.session_state.page = "final"
        st.rerun()

    if st.button("still mad 😤"):
        show_message("ok but like… unnecessary 🙄")

    if st.session_state.message:
        st.write(st.session_state.message)

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("i don’t care about being right… i just don’t like us like this.")
    st.write("stop being stubborn and just call me.")

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("call me. now. 📞"):
        st.session_state.page = "call"
        st.rerun()

# ---- CALL ----
elif st.session_state.page == "call":
    st.markdown("<h1>📞 incoming call…</h1>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=200)

    st.write("you have no choice now 😌")

    time.sleep(1)
    st.write("connecting…")

    time.sleep(1)

    st.markdown("💖 💕 💗 💓 💞 💘 💝 💖")

    st.success("good decision. call me.")
