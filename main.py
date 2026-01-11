import streamlit as st
from langchain_ollama import ChatOllama

st.title("Simple Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

model = ChatOllama(model="gemma3:270m", temperature=0.7)

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Type your message...")
if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    reply = model.invoke(prompt).content
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
