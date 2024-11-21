import streamlit as st

def component_a():
    st.title("Component A")

    panjang = st.number_input("Masukkan nilai panjang", 0)
    lebar = st.number_input("Masukkan nilai lebar", 0)
    hitung = st.button("Hitung")

    if hitung:
        luas = panjang * lebar
        st.write("Luas persegi panjang adalah =", luas)