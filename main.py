import streamlit as st
import pandas as pd
import json
from streamlit_option_menu import option_menu

with st.sidebar:
    selected = option_menu('Learn Streamlit', ['Dashboard', 'Component Test A', 'Component Test B'], 
        icons=['house', 'gear', 'gear'], menu_icon="cast", default_index=0)
    
#Dashboard Page
if (selected == "Dashboard") :
    with open("data.json", "r") as file:
        dataSiswa = json.load(file)

    rows = []
    for siswa in dataSiswa["students"]:
        name = siswa["name"]
        for month, scores in siswa["scores"].items():
            row = {"Name": name, "Month": month}
            row.update(scores)
            rows.append(row)

    df = pd.DataFrame(rows)
    df.index = df.index + 1
    df.index.name = "No"

    df["Month"] = pd.Categorical(df["Month"], categories=["Januari", "Februari", "Maret", "April", "Mei", "Juni"], ordered=True)

    average = df.groupby("Month")[["Matematika", "Fisika", "Bahasa Indonesia", "Sosiologi", "Kesenian"]].mean()

    st.title("Daftar Nilai Kelas")
    st.dataframe(df)

    st.subheader("Nilai rata-rata bulanan")
    st.line_chart(average)

    st.subheader("Nilai rata-rata bulanan (Bar Chart)")
    st.bar_chart(average)

    

#Component Test A Page
if (selected == "Component Test A") : 
    st.title('Component Test A')
    panjang = st.number_input ('Masukkan nilai panjang', 0)
    lebar = st.number_input('Masukkan nilai lebar', 0)

    hitung = st.button('Hitung')

    if hitung :
        luas = panjang * lebar
        st.write('Luas pesergi panjang adalah =', luas)