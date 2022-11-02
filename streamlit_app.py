# Import libraries and dependencies
import streamlit as st
from PIL import Image
import requests
import os
import json
from datetime import datetime, timedelta
import pandas as pd

#Create the sidebar
st.sidebar.title('User Inputs')
st.sidebar.markdown('Provide some general information & we will quote you an insurance policy for your excursion')

name = st.sidebar.text_input('What is Your Name?')
email = st.sidebar.text_input('What is Your Email Address?')
size = st.sidebar.number_input('How Many In Your Party?', 1,8)
date = st.sidebar.date_input('What is the Date of Your Excursion')
type = st.sidebar.selectbox('What is your excursion type', ['Sail', 'Golf', 'Scuba', 'ZipLine', 'Moped', 'Other'])
cost = st.sidebar.number_input('What is the Total Cost of Your Excursion?')

uploaded_file = st.sidebar.file_uploader('Upload Copy of Receipt')

#Set domain for API calls
domain = 'https://api.openweathermap.org/data/3.0/onecall&lat=21.31&lon=-157.86&exclude=current,minutely,hourly,alerts&units=imperial&appid='

# Load credentials for the API calls into the auth variable
credential_upload = st.file_uploader('Upload Open Weather MAP API credentials')
if credential_upload:
    creds = []
    for line in credential_upload:
        creds.append(line.decode().strip())
    auth = (creds[0])

st.caption('Upload the API key within a .txt file', unsafe_allow_html = True)

# Create a button to generate the forecast
if st.button('Generate Forecast'):
    st.write('generating forecast')

st.image('./Images/logo.png')

st.header('Here are the average weather conditions on the day of your excursion:')

def fetch(session, url):
    try:
        result = session.get(url)
        return result.json
    except Exception:
        return{}

st.caption('Temperature: ')
st.caption('Cloud Cover:')
st.caption('Percipitation:')
st.caption('Wind Speed:')

st.image('./Images/sail.png')

st.header('Here is the 5 day weather forecast for your excursion location')

st.image('./Images/scuba.png')

st.write('Based on the info provided & historical weather data you qualify for ExcurAssure!')
st.caption('Cost to insure your excursion:')
st.radio('Do you wish to proceed', ['Yes', 'No'])



#if(st.sidebar.selectbox('Sail')):
 #   st.image('./Images/sail.png')

