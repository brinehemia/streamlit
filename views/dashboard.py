import streamlit as st
import pandas as pd
import json

def dashboard():
    st.title("Dashboard")

    with open("data/data.json", "r") as file:
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

    st.dataframe(df, width=None, height=200)
    st.subheader("Nilai rata-rata bulanan")
    st.line_chart(average)
    st.subheader("Nilai rata-rata bulanan (Bar Chart)")
    st.bar_chart(average)