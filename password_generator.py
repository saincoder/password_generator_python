import streamlit as st
import random
import string

def generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special, custom_chars):
    chars = ''
    if include_lowercase:
        chars += string.ascii_lowercase
    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_special:
        chars += string.punctuation
    if custom_chars:
        chars += custom_chars

    if not chars:
        st.error("Please select at least one character set or enter custom characters.")
        return ''

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

st.title("Password Generator")

# Add developer name
st.markdown("Developed by Shahid")

st.subheader("Select the criteria for your password:")
length = st.slider("Select Password Length", 8, 30, 12)
include_lowercase = st.checkbox("Include Lowercase Letters", value=True)
include_uppercase = st.checkbox("Include Uppercase Letters", value=True)
include_numbers = st.checkbox("Include Numbers", value=True)
include_special = st.checkbox("Include Special Characters", value=False)
custom_chars = st.text_input("Enter Custom Characters (optional)")

if st.button("Generate Password"):
    password = generate_password(length, include_lowercase, include_uppercase, include_numbers, include_special, custom_chars)
    if password:
        st.success(f"Generated Password: {password}")
