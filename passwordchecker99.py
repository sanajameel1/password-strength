import re
import streamlit as st

# Page styling
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

# Page title and description
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔎")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be *at least 8 characters long*.")

    # Uppercase and lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should include *both uppercase (A-Z) and lowercase (a-z) letters*.")

    # Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one special character (!@#$%^&).")

    # Digit check
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Include *at least one numeric digit (0-9)*.")

    # Display password strength and feedback
    if score == 4:
        st.success("🔒 Your password is *strong*! 🔑")
    elif score == 3:
        st.info("🔒 *Moderate Password* - Consider improving security by adding more features 🔑")
    else:
        st.error("❌ *Weak Password* - Consider improving your password security 🔑")

    # Feedback
    if feedback:
        with st.expander("🔎 *Improve your password*"):
            for item in feedback:
                st.write(item)

# Password input
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

# Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first.")

