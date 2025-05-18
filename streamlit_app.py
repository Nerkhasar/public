import streamlit as st
file = open("index.html", "r")
rfile = file.read()
st.write(rfile)
