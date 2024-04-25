import streamlit as st
from streamlit_authenticator import Authenticate

# Define your users and passwords (in practice, use secure password hashing)
users = {
    "usernames": ["admin", "user"],
    "passwords": ["admin", "user123"]
}

# Instantiate the authenticator
authenticator = Authenticate(
    users,
    'streamlit_authenticator',  # Cookie name
    'some_random_string',       # Cookie key
    'sqlite'                    # Database backend
)

# Protect your Streamlit app with authentication
name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    st.write(f'Welcome *{name}*')
    # Your main app goes here
elif authentication_status == False:
    st.error('Username/password is incorrect')
elif authentication_status == None:
    st.warning('Please enter your username and password')
