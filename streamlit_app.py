import streamlit as st

st.title("Agus kopling")
st.write(
    "Muka buronan bayu"
)
st.image (""), width=200)

st.title("Aplikasi buronan bandung")
st.header("Aplikasi mengecek kondisi bayu")
angka = st.number_input("Angka kesehatan bayu:", value=0, step=1)

if (angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan stres")
else:
    st.write(f"{angka} Adalah bilangan gila")
    
