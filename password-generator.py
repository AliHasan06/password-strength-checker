import streamlit as st  
import random  
import string  

def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation
    return "".join(random.choice(characters) for _ in range(length))

def check_password_strength(password):
    if len(password) < 8:
        return "🔴 Weak"
    elif len(password) < 12:
        return "🟡 Medium"
    else:
        return "🟢 Strong"

st.title("🔐 Password Generator")

length = st.slider("Select password length:", min_value=6, max_value=32, value=16)
use_digits = st.checkbox("Include numbers (0-9)")
use_special = st.checkbox("Include special characters (!@#$%^&*)")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    strength = check_password_strength(password)
    st.text_input("Generated Password:", password, key="password")
    st.write(f"🔍 **Strength:** {strength}")
    st.write("---------------------------")
    st.write("🚀 Built by [Ali](https://github.com/AliHasan06)")
