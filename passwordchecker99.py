import re
import streamlit as st

# Page Styling
st.set_page_config(page_title="Password Strength Checker By Sana Jameel", page_icon="🔐", layout="centered")

# Custom CSS
st.markdown("""
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}   
        .stButton button {width: 50%; background-color: #4CAF50; color: white; font-size: 18px;}
        .stButton button:hover {background-color: #45a049;}
    </style>
""", unsafe_allow_html=True)

# Page Title and Description
st.title("🔒 Password Strength Checker")
st.write("Enter your password below to check its security level. 🔎")

# Function to check password strength
def check_password_strength(password):
    score = sum([len(password) >= 8, 
                 bool(re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)), 
                 bool(re.search(r"\d", password)), 
                 bool(re.search(r"[!@#$%^&*]", password))])

    feedback = []
    if len(password) < 8:
        feedback.append("❌ Password should be **at least 8 characters long**.")
    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        feedback.append("❌ Password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")
    if not re.search(r"\d", password):
        feedback.append("❌ Include **at least one number (0-9)**")
    if not re.search(r"[!@#$%^&*]", password):
        feedback.append("❌ Include **at least one special character (!@#$%^&*)**")

    # Display password strength and feedback
    st.success("🔒 Your password is **strong**! 🔑") if score == 4 else (
        st.info("🔒 **Moderate Password** - Consider improving security 🔑") if score == 3 else 
        st.error("❌ **Weak Password** - Improve security 🔑")
    )

    # Feedback
    if feedback:
        with st.expander("🔎 **Improve your password**"):
            for item in feedback:
                st.write(item)

# User Input
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

# Button Functionality
if st.button("Check Strength"):
    st.warning("Please enter a password first.") if not password else check_password_strength(password)
