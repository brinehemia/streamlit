import streamlit as st
import json as json
from views import dashboard, component_a, component_upload
from streamlit_option_menu import option_menu
from services.auth import AuthManager

auth_manager = AuthManager()

if not auth_manager.is_authenticated():
    st.title('Login')
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')

    if st.button('Login'):
        if auth_manager.login(username, password):
            st.success('Login berhasil!')
            st.rerun()
else:
    with st.sidebar:
        selected = option_menu('Streamlit Test', ['Dashboard', 'Component A', 'Component Upload'], 
        icons=['house', 'gear', 'upload'], menu_icon=None, default_index=0)

    # menu
    if selected == 'Dashboard':
        dashboard() 
    elif selected == 'Component A':
        component_a()
    elif selected == 'Component Upload':
        component_upload()
   
    # Button Logout
    if st.sidebar.button('Logout'):
        auth_manager.logout()
        st.rerun()