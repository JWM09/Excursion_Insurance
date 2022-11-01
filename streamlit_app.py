import streamlit as st
from PIL import Image

st.sidebar.title('ExcurAssure')
st.sidebar.markdown('Provide some general information & we will quote you an insurance policy for your excursion')

name = st.sidebar.text_input('What is Your Name?')
email = st.sidebar.text_input('What is Your Email Address?')
size = st.sidebar.number_input('How Many In Your Party?', 1,8)
date = st.sidebar.date_input('What is the Date of Your Excursion')
st.sidebar.selectbox('What is your excursion type', ['Sail', 'Golf', 'Scuba', 'ZipLine', 'Moped', 'Other'])
cost = st.sidebar.number_input('What is the Total Cost of Your Excursion?')

uploaded_file = st.sidebar.file_uploader('Upload Copy of Receipt')

if(st.sidebar.selectbox('Sail')):
    st.image('../Images/sail.png')

