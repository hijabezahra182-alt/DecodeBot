
import streamlit as st

from chatbot import get_response
from utils.interface import get_custom_css


# PAGE CONFIGURATION

st.set_page_config(
    page_title="DecodeBot | AI Assistant",
    page_icon="✦",
    layout="wide"
)


# CUSTOM CSS

st.markdown(
    get_custom_css(),
    unsafe_allow_html=True
)


# SESSION STATE

if "messages" not in st.session_state:
    st.session_state.messages = []


# SIDEBAR

with st.sidebar:

    st.markdown("# ✦ DecodeBot")
    st.caption("YOUR FRIENDLY DIGITAL ASSISTANT")

    st.divider()

    if st.button("＋ New Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.markdown("### RECENT CHAT")

    if st.session_state.messages:

        for message in st.session_state.messages:

            if message["role"] == "user":
                st.caption("💬 " + message["content"][:35])

    else:
        st.caption("Your conversations will appear here.")

    st.divider()

    st.markdown("### ABOUT DECODEBOT")

    st.caption(
        "A rule-based conversational assistant "
        "developed as an Artificial Intelligence project."
    )

    st.divider()

    st.markdown("### QUICK COMMANDS")

    st.caption("• hi / hello / hy")
    st.caption("• help")
    st.caption("• what is AI")
    st.caption("• what is Python")
    st.caption("• tell me a joke")
    st.caption("• bye / exit")

    if st.button("Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# MAIN HEADER

st.markdown(
    '<div class="welcome-icon">✦</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">Your ideas, decoded.</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Meet DecodeBot, your friendly rule-based assistant.'
    '</div>',
    unsafe_allow_html=True
)


# WELCOME SCREEN

if not st.session_state.messages:

    st.markdown("### What would you like to explore?")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown(
            """
            <div class="feature-card">
                <h4>🧠 Artificial Intelligence</h4>
                <p>Explore AI, machine learning and deep learning.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            """
            <div class="feature-card">
                <h4>💻 Python Programming</h4>
                <p>Learn about variables, loops and functions.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-card">
                <h4>🌐 Technology</h4>
                <p>Discover algorithms, APIs and data science.</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        st.write("")

        st.markdown(
            """
            <div class="feature-card">
                <h4>✨ Fun & Motivation</h4>
                <p>Enjoy jokes, facts and motivational messages.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# DISPLAY CHAT HISTORY

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# CHAT INPUT

user_input = st.chat_input("Message DecodeBot...")


if user_input:

    # SAVE USER MESSAGE

    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # GENERATE BOT RESPONSE

    response = get_response(user_input)

    # SAVE BOT RESPONSE

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    # REFRESH APPLICATION

    st.rerun()


# FOOTER

st.markdown(
    '<div class="footer">'
    'DecodeBot 1.0 | Rule-Based AI Assistant | DecodeLabs Project 1'
    '</div>',
    unsafe_allow_html=True
)
