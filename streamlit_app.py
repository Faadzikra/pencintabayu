import streamlit as st

st.title("Agus kopling")
st.write(
    "Muka buronan bayu"
)
st.image (""), width=200)

st.title("Aplikasi Sederhana")
st.header("Aplikasi mengecek nilai Genap/Ganjil")
angka = st.number_input("Tulis sebuah angka:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} Adalah bilangan Ganjil")
    
