import streamlit as st
import random
import time

st.set_page_config(page_title="for my naaraaz 🦝", layout="centered")

# ---- RANDOM EMOJI BACKGROUND ----
def render_cute_background():
    emojis = ["💚","🤩","😍","😻","💋","🫦","💅","👩‍❤️‍💋‍👨","👗","🐶","🐼","🐷","🐥","🐙","🦄","🍄","💐","🌷","🌹","🪻","🪷","🌺","🌸","🌼","🌻","💥","☁️","🍇","🍓","🍒","🍡","🎂","🍭","🍬","🎆","💎","🎈","🎀","🪅","🎊","🎉","🩷","❤️","🧡","💛","💚","🩵","💙","💜","🖤","🩶","🤍","🤎","❤️‍🔥","❣️","💕","💞","💓","💗","💖","💘","💝"]

    elements = ""
    for _ in range(45):
        emoji = random.choice(emojis)
        left = random.randint(0, 100)
        top = random.randint(0, 100)
        size = random.randint(18, 50)
        rotate = random.randint(-30, 30)

        elements += f"""
        <div style="
            position: fixed;
            left: {left}%;
            top: {top}%;
            font-size: {size}px;
            transform: rotate({rotate}deg);
            opacity: 0.50;
            pointer-events: none;
            z-index: 0;
        ">
            {emoji}
        </div>
        """

    st.markdown(elements, unsafe_allow_html=True)

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
    position: relative;
    z-index: 1;
}

h1, h2 { color: black; }

/* BUTTONS */
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
div[role="radiogroup"] * {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# 👉 RENDER BACKGROUND
render_cute_background()

# ---- STATE ----
if "page" not in st.session_state:
    st.session_state.page = "home"

if "message" not in st.session_state:
    st.session_state.message = ""

if "wrong_clicks" not in st.session_state:
    st.session_state.wrong_clicks = 0

if "last_page" not in st.session_state:
    st.session_state.last_page = ""

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

    if "msg_list" not in st.session_state:
        st.session_state.msg_list = []

    if st.button("submit"):

        if choice.startswith("no"):
            st.session_state.msg_list = [
                "no?? 😭 be serious.",
                "we both know that’s not true.",
                "this attitude is not convincing anyone btw 🙄"
            ]

        elif choice.startswith("maybe"):
            st.session_state.msg_list = [
                "maybe?? 🤨 okay…",
                "we’re getting somewhere.",
                "that was dangerously close to honesty 😌"
            ]

        else:
            clear_message()
            st.session_state.msg_list = []
            st.session_state.page = "step3"
            st.rerun()

    if st.session_state.msg_list:
        for msg in st.session_state.msg_list:
            st.write(msg)

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
        clear_message()
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

    st.video("https://www.youtube.com/watch?v=uxpDa-c-4Mc")

    # ---- RESPONSE SYSTEM (NO REPEATS) ----
    def get_response():
        if "responses_pool" not in st.session_state:
            st.session_state.responses_pool = [
                "no 😭",
                "wrong choice.",
                "try again.",
                "you know that’s not the one.",
                "be serious.",
                "this is embarrassing 😭",
                "you’re doing this on purpose.",
                "why are you like this.",
                "HELLO??",
                "this is not a game.",
                "call me.",
                "i know you see the right button.",
                "stop avoiding it.",
                "this is painful to watch.",
                "just press the right one 😭"
            ]
            st.session_state.used_responses = []

        # reset when exhausted
        if len(st.session_state.responses_pool) == 0:
            st.session_state.responses_pool = st.session_state.used_responses
            st.session_state.used_responses = []

        choice = random.choice(st.session_state.responses_pool)
        st.session_state.responses_pool.remove(choice)
        st.session_state.used_responses.append(choice)

        return choice

    # ---- CALL BUTTON ----
    if st.button("call me. now. 📞"):
        st.markdown(
            '<meta http-equiv="refresh" content="0; url=tel:+919819271926">',
            unsafe_allow_html=True
        )

    # ---- WRONG OPTIONS ----
    if st.button("be stubborn 😤"):
        show_message(get_response())
        st.rerun()

    if st.button("be a bitch 😡"):
        show_message(get_response())
        st.rerun()

    # ---- DISPLAY MESSAGE ----
    if st.session_state.message:
        st.write(st.session_state.message)
