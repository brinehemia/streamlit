import requests
import streamlit as st
from decouple import config
from services.cookies import cookiesManager

class AuthManager:
    def __init__(self, base_url=None):
        self.base_url = base_url or config("BASE_URL")
        self.jwt_token = None
        self.cookies = cookiesManager

    def login(self, username, password):
        url = f"{self.base_url}auth/login"
        payload = {"username": username, "password": password}
        response = requests.post(url, json=payload)

        if response.status_code == 200:
            self.jwt_token = response.json().get("accessToken")
            self.cookies["jwt_token"] = self.jwt_token
            self.cookies.save()
            return True
        else:
            st.error("Login gagal: " + response.text)
            return False

    def get_token(self):
        return self.cookies.get("jwt_token")

    def is_authenticated(self):
        return self.get_token() is not None

    def logout(self):
        self.jwt_token = None
        self.cookies["jwt_token"] = None
        self.cookies.save()