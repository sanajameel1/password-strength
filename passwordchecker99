import re
import streamlit as st

#page styling
st.set_page_config(page_title="Password Strength Checker By Sana Jameel", page_icon="🔐", layout="centered")
#custom css
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }   
    .stButton button {width: 50%; background-color #4CAF50; color: white; font-size: 18px; }
    .stButton button:hover { background-color: #45a049;}
</style>     
""", unsafe_allow_html=True)

#page title and decription
st.title("🔒 Password Strength Generator")
st.write("Enter your password below to check its security level. 🔎")

#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = [] 

    if len(password) >= 8:
        score += 1 #increased score by 1
    else:
        feedback.append("❌ password should be **atlest 8 character long**.")

    if re.search(r"[A-Z]", password and re.search(r"a-z"), password):
        score += 1
    else:
        feedback.append("❌  password should include **both uppercase (A-Z) and lowercase (a-z) letters**.")

    #special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌  Include **at least one special character (!@#$%^&*)**")

   #display password strength and feedback
    if score == 4:
       st.success("🔒 Your password is **strong**! 🔑")
    elif score == 3:
        st.info("🔒 **Moderate Password** - Consider impoving security by adding more features 🔑")
    else:
        st.error("❌ **Weak Password** - Consider improving your password security 🔑")

    #feedback
    if feedback:
        with st.expander("🔎 **Improve your password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong 🔐")

#button working
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("Please enter a password first.")
