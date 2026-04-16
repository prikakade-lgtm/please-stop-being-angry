import streamlit as st
import random

st.set_page_config(page_title="for u 😶", layout="centered")

# ---- CSS ----
st.markdown("""
<style>
html, body, .stApp {
    background-color: #fff5f7 !important;
    color: #333 !important;
}

.block-container {
    max-width: 500px;
    margin: auto;
    text-align: center;
}

.stButton>button {
    background-color: #ffd6e0;
    border-radius: 25px;
    padding: 14px;
    width: 100%;
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
    st.title("hey you 😤")
    st.image("https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif", width=180)

    if st.button("okay fine 🙄"):
        st.session_state.page = "step1"

# ---- STEP 1 ----
elif st.session_state.page == "step1":
    st.title("step 1 🌸")
    st.write("take a deep breath 😌")

    if st.button("done 😶"):
        st.session_state.page = "step2"

# ---- STEP 2 ----
elif st.session_state.page == "step2":
    st.title("important question 🧠")

    st.radio("do you miss me?", ["no 😤", "maybe 😶", "okay fine 😒"])

    if st.button("submit"):
        st.session_state.submitted = True

    if st.session_state.submitted:
        st.write("you are still emotionally attached 🤨")

        if st.button("continue"):
            st.session_state.page = "step3"
            st.session_state.submitted = False

# ---- STEP 3 ----
elif st.session_state.page == "step3":
    st.title("...")
    st.write("i don’t like it when we’re like this.")

    if st.button("fine 😶"):
        st.session_state.page = "final"

# ---- FINAL ----
elif st.session_state.page == "final":
    st.title("final decision 🎲")

    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.write("you know what needs to be done 😌")

    if st.button("fine… i’ll call you 😒📞"):
        st.success("correct decision. i’ll be waiting 😌")
        st.balloons()

    if st.button("still thinking 🤨"):
        st.write("unacceptable.")

    if st.button("restart 🔄"):
        st.session_state.page = "home"
