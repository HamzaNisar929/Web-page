import streamlit as st

st.header("Contact Us")

with st.form(key="form_key"):
    user_email = st.text_input("Enter your email")
    choice = st.selectbox("What topic do you want to discuss?", ("Job Inquiries", "Project Proposals", "Other"))
    user_message = st.text_area("Enter your message")
    button = st.form_submit_button("Submit")