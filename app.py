# app.py
import streamlit as st
import random
import string

# --- Generador de contraseñas ---
def generate_password(length=12, include_numbers=True, include_symbols=True):
    """
    Generate a secure but simple password suitable for older adults.
    """
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits if include_numbers else ''
    symbols = string.punctuation if include_symbols else ''

    all_characters = lowercase_letters + uppercase_letters + digits + symbols

    # Aseguramos que haya al menos una minúscula, una mayúscula, y opcionalmente número/símbolo
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

# --- Interfaz de Streamlit ---
st.set_page_config(page_title="Easy Password Generator", page_icon="🔐", layout="centered")

st.title("🔐 Easy Password Generator")
st.markdown("Crea contraseñas seguras y fáciles de recordar, diseñadas especialmente para adultos mayores.")

# Parámetros de usuario
st.subheader("Ajustes de generación")

col1, col2 = st.columns(2)
length = col1.slider("Longitud", min_value=8, max_value=20, value=12, step=1)
include_numbers = col1.checkbox("Incluir números (0-9)", value=True)
include_symbols = col2.checkbox("Incluir símbolos (!@#...)", value=True)

# Botón de generación
if st.button("Generar contraseña"):
    password = generate_password(length, include_numbers, include_symbols)
    st.success("✅ ¡Contraseña generada con éxito!")
    st.text_input("Tu contraseña:", value=password, type="default", disabled=False)
    st.info("💡 Para copiarla, selecciona el texto y usa **Ctrl+C** (Windows) o **Cmd+C** (Mac).")
else:
    st.warning("Haz clic en *Generar contraseña* para comenzar.")

# Consejos
st.markdown("---")
st.markdown("""
**Consejos:**
- Usa entre 8 y 20 caracteres para un equilibrio entre seguridad y facilidad.
- Si quieres algo más fácil de recordar, evita los símbolos.
- Mantén tus contraseñas privadas y no las compartas.
""")
