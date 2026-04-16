# ---- FINAL ----
elif st.session_state.page == "final":
    st.markdown("<h2>final decision 🎲</h2>", unsafe_allow_html=True)

    st.markdown('<p class="cute-text">you know what needs to be done.</p>', unsafe_allow_html=True)

    # 🔥 Drake Hotline Bling GIF
    st.image("https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif", width=220)

    st.markdown('<p class="cute-text">don’t make this harder than it needs to be 😌</p>', unsafe_allow_html=True)

    if st.button("fine… i’ll call you 😒📞"):
        st.success("correct decision. i’ll be waiting 😌")

        st.balloons()

    if st.button("still thinking about it 🤨"):
        st.write("unacceptable. try again.")

    if st.button("restart 🔄"):
        st.session_state.page = "home"
