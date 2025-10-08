# app.py
import streamlit as st
import random
import string

# --- Password generator ---
def generate_password(length=12, include_numbers=True, include_symbols=True):
    """
    Generate a secure and simple password.
    """
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Ensure at least one lowercase, one uppercase, optional number/symbol
    password = []
    password.append(random.choice(lowercase_letters))
    password.append(random.choice(uppercase_letters))
    if include_numbers and digits:
        password.append(random.choice(digits))
    if include_symbols and symbols:
        password.append(random.choice(symbols))

    remaining_length = length - len(password)
    for _ in range(remaining_length):
        password.append(random.choice(all_characters))

    random.shuffle(password)
    return ''.join(password)

# --- Streamlit interface ---
st.set_page_config(page_title="Easy Password Generator", page_icon="🔐", layout="centered")

st.title("🔐 Easy Password Generator")
st.markdown("Generate secure passwords easily, designed especially for older adults.")

# User settings
st.subheader("Password Settings")

col1, col2 = st.columns(2)
length = col1.slider("Password length", min_value=8, max_value=20, value=12, step=1)
include_numbers = col1.checkbox("Include numbers (0-9)", value=True)
include_symbols = col2.checkbox("Include symbols (!@#...)", value=True)

# Generate button
if st.button("Generate password"):
    password = generate_password(length, include_numbers, include_symbols)
    st.success("✅ Password generated successfully!")
    st.text_input("Your password:", value=password, type="default", disabled=False)
    st.info("💡 To copy: select the text and press **Ctrl+C** (Windows) or **Cmd+C** (Mac).")
else:
    st.warning("Click 'Generate password' to start.")

# Tips
st.markdown("---")
st.markdown("""
**Tips:**
- Use 8–20 characters for a balance between security and ease.
- For easier remembering, avoid symbols.
- Keep your passwords private and do not share them.
""")
