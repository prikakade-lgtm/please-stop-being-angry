import streamlit as st
import random
import time

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS (ONLY VISUAL FIXES) ----
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

h1, h2, p, div, span, label {
    color: black !important;
}

.stButton>button {
    background-color: #ff4d6d;
    color: white !important;
    border-radius: 25px;
    padding: 14px;
    width: 100%;
    border: none;
    margin-top: 10px;
}

/* moving button */
.move {
    display: inline-block;
    animation: float 1s infinite alternate ease-in-out;
}

@keyframes float {
    0% { transform: translateX(-10px); }
    100% { transform: translateX(10px); }
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

    st.markdown('<div class="move">', unsafe_allow_html=True)
    if st.button("no 😤"):
        st.write("wrong answer. try again.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.markdown("<h2>step 1 🌸</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/3oriO0OEd9QIDdllqo/giphy.gif", width=200)

    st.markdown('<p class="cute-text">take a deep breath 😌<br>don’t skip this.</p>', unsafe_allow_html=True)

    if st.button("done 😶"):
        st.session_state.page = "step2"

    st.markdown('<div class="move">', unsafe_allow_html=True)
    if st.button("i refuse 😤"):
        st.write("you’re being dramatic again.")
    st.markdown('</div>', unsafe_allow_html=True)

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.markdown("<h2>important question 🧠</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/l3q2K5jinAlChoCLS/giphy.gif", width=200)

    st.markdown("do you miss me?")

    choice = st.radio("",
        ["no 😤", "maybe 😶", "okay fine 😒"]
    )

    if st.button("submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        st.markdown('<p class="cute-text">analysis complete 🧠<br>you are still attached 🤨</p>', unsafe_allow_html=True)

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

    st.image("https://media.giphy.com/media/9Y5BbDSkSTiY8/giphy.gif", width=200)

    st.markdown('<p class="cute-text">i don’t like it when we’re like this</p>', unsafe_allow_html=True)

    # typing effect (added, not replacing)
    placeholder = st.empty()
    for i in range(3):
        placeholder.write("typing" + "." * (i+1))
        time.sleep(0.4)

    if st.button("okay…"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.image("https://media.giphy.com/media/5GoVLqeAOo6PK/giphy.gif", width=200)
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.markdown('<p class="cute-text">choose wisely.</p>', unsafe_allow_html=True)

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    if st.button("click to decide our fate"):
        st.success(random.choice([
            "correct answer. you may proceed 😌",
            "hug required. no exceptions 🤗",
            "you text me right now 😏"
        ]))

    if st.button("📞 call me"):
        st.session_state.page = "call"

# ---- CALL SCREEN ----
elif st.session_state.page == "call":
    st.markdown("<h1>📞 incoming call…</h1>", unsafe_allow_html=True)

    st.audio("https://www.soundjay.com/phone/telephone-ring-01.mp3", autoplay=True)

    st.write("answer it 😐")

    time.sleep(3)

    st.session_state.page = "missed"

# ---- MISSED CALL ----
elif st.session_state.page == "missed":
    st.markdown("<h1>📵 missed call</h1>", unsafe_allow_html=True)

    st.write("wow. okay 😭")

    if st.button("call back"):
        st.markdown("📞 call me now: +91 9819271926")
