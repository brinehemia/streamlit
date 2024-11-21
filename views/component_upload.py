import streamlit as st
import requests
from services.api import ApiClient

def component_upload():
    api_client = ApiClient()
    st.title("Upload File Excel atau CSV")

    # Field upload file
    uploaded_file = st.file_uploader(
        "Pilih file untuk diunggah (format CSV atau Excel)", 
        type=["csv", "xlsx"]
    )

    if uploaded_file is not None:
        st.write("Nama file:", uploaded_file.name)
        
        with open(uploaded_file.name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:
            response = api_client.upload_file("upload/excel", uploaded_file.name)
            print(response)
            st.success("File berhasil diunggah!")
            st.json(response)
        except requests.exceptions.RequestException as e:
            st.error(f"Terjadi kesalahan saat mengunggah file: {e}")