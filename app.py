import streamlit as st

st.title("🚀 Hackathon Demo App")

name = st.text_input("Enter your name:")

if st.button("Greet"):
    st.success(f"Hello {name}! Your app is live 🎉")