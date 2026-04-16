import streamlit as st
import random
import time

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS (PASTEL FIXED) ----
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Quicksand:wght@400;600&display=swap');

/* BACKGROUND */
html, body, .stApp {
    background-color: #ffdce5 !important;
    font-family: 'Quicksand', sans-serif;
    color: #000 !important;
}

/* CENTER */
.block-container {
    max-width: 420px;
    margin: auto;
    text-align: center;
    padding-top: 2rem;
}

/* TEXT */
h1, h2, p, div, span, label {
    color: #000 !important;
}

/* BUTTONS */
.stButton>button {
    background-color: #ff4d6d;
    color: white !important;
    border-radius: 25px;
    padding: 14px;
    width: 100%;
    border: none;
    margin-top: 10px;
    font-weight: 600;
}

.stButton>button:hover {
    background-color: #e6395c;
}

/* MOVING BUTTON */
.move-btn {
    position: relative;
    animation: move 1.5s infinite alternate;
}

@keyframes move {
    0% { left: -10px; }
    100% { left: 10px; }
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

    st.markdown('<div class="move-btn">', unsafe_allow_html=True)
    if st.button("no 😤"):
        st.write("wrong answer 🙄")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.write("take a deep breath 😌")

    if st.button("done 😶"):
        st.session_state.page = "step2"

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

        if st.button("continue"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.markdown("<h2>wait…</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.write("i don’t like it when we’re like this.")

    # typing animation
    placeholder = st.empty()
    for i in range(3):
        placeholder.write("typing" + "." * (i+1))
        time.sleep(0.5)

    st.write(random.choice([
        "i miss you btw.",
        "this is dumb, we should not be fighting.",
        "you’re my favorite person, even when you’re annoying."
    ]))

    if st.button("fine 😶"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("i don’t care about being right… i just don’t like us like this.")

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("call her 📞"):
            st.session_state.page = "call"

    with col2:
        st.markdown('<div class="move-btn">', unsafe_allow_html=True)
        if st.button("be stubborn 😤"):
            st.write("invalid option.")
        st.markdown('</div>', unsafe_allow_html=True)

# ---- INCOMING CALL ----
elif st.session_state.page == "call":
    st.markdown("<h1>📞 incoming call…</h1>", unsafe_allow_html=True)

    # ringtone
    st.audio("https://www.soundjay.com/phone/telephone-ring-01.mp3", autoplay=True)

    st.image("https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", width=200)

    st.write("answer it 😐")

    time.sleep(3)

    st.session_state.page = "missed"

# ---- MISSED CALL ----
elif st.session_state.page == "missed":
    st.markdown("<h1>📵 missed call</h1>", unsafe_allow_html=True)

    st.write("wow… you really ignored that 😭")

    if st.button("okay okay i’ll call back 😭"):
        st.markdown("[📞 call me now](tel:+1234567890)")

    if st.button("restart 🔄"):
        st.session_state.page = "home"
