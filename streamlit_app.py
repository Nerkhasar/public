import streamlit as st
file = open("index.html", "r")
rfile = file.read()
st.title("My Hosted Text")
st.write(rfile)
