import streamlit as st
import re
import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    return score, feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

st.title("🔐 Project 02: Password Strength Meter")

password = st.text_input("Enter your password:")

if st.button("Check Strength"):
    if not password:
        st.warning("Please enter a password.")
    else:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password!")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider adding more security features.")
        else:
            st.error("❌ Weak Password - Improve it using the suggestions below.")
        
        if feedback:
            st.write("### Suggestions:")
            for suggestion in feedback:
                st.write(suggestion)

if st.button("🔁 Suggest a Strong Password"):
    strong_password = generate_strong_password()
    st.text_input("Suggested Password:", strong_password)
    st.info("✅ This is a strong and secure password.")

st.markdown("---")
st.markdown("🚀 Built by [Ali](https://github.com/AliHasan06)")
