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
    padding: 14px;
    width: 100%;
    border: none;
    margin-top: 10px;
    transition: 0.2s;
}

.stButton>button:active {
    transform: scale(0.96);
}

.stButton>button:hover {
    background-color: #e6395c;
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

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"
        st.rerun()

    if st.button("no 😤"):
        st.write("wrong answer. try again 🙄")

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done 😶"):
        st.session_state.page = "step2"
        st.rerun()

    if st.button("i refuse 😤"):
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
        ]
    )

    if st.button("submit"):
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
            "you miss me. let’s not lie today.",
            "this could’ve been over already btw",
            "you’re doing too much 😭",
            "this attitude is not helping you win",
        ]))

        if st.button("okay continue 😒"):
            st.session_state.page = "step3"
            st.session_state.submitted = False
            st.rerun()

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    # CLEAN DRAMATIC PAUSE
    with st.empty():
        st.write("...")
        time.sleep(0.5)
        st.write("wait...")
        time.sleep(0.5)

    st.write("i don’t like it when we’re like this.")

    st.write(random.choice([
        "i miss you btw.",
        "this is dumb, we should not be fighting.",
        "you’re my favorite person, even when you’re annoying."
    ]))

    if st.button("fine 😶"):
        st.session_state.page = "final"
        st.rerun()

    if st.button("still mad 😤"):
        st.write("ok but like… unnecessary 🙄")

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("i don’t care about being right… i just don’t like us like this.")

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("call me 📞"):
        st.session_state.page = "call"
        st.rerun()

    if st.button("be stubborn 😤"):
        st.write("invalid option. try again.")

    # SIMPLE OPTION D (WORKING)
    if st.button("try your luck again 🎲"):
        st.write(random.choice([
            "call her.",
            "call her now.",
            "still call her.",
            "you already know what to do.",
        ]))

    st.markdown("[📞 call me now](tel:+919819271926)")

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
