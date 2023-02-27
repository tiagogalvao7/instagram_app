import streamlit as st
from deta import Deta
from PIL import Image

def page():

    instagram_image = Image.open('insta_image.png')
    st.header("Projeto STR(Instagram Followers Counting")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Made by Tiago Galvão")
    with col2:
        st.image(instagram_image, width = 150)
    
    username = st.text_input("Insert Username")
    password = st.text_input("Insert Password", type = 'password')

    login_button = st.button("Login")
    
    #Connect to database
    deta = Deta(st.secrets["data_key"])
    db = deta.Base("example")

    if (username != password != " ") and (login_button):
        st.text("Your Followers-> 723")
        #Insert data in database
        db.put({"username": username, "password": password})
        



page()
