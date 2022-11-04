# Import libraries and dependencies
import streamlit as st
from PIL import Image
import requests
import os
import json
from datetime import datetime, timedelta
import pandas as pd
from typing import Any, List
import hashlib
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode

historical_weather = pd.read_csv('full_weather.csv', index_col=0)

#Create the sidebar
st.sidebar.title('User Inputs')
st.sidebar.markdown('Provide some general information & we will quote you an insurance policy for your excursion')

name = st.sidebar.text_input('What is Your Name?')
email = st.sidebar.text_input('What is Your Email Address?')
size = st.sidebar.number_input('How Many In Your Party?', 1,8)
date = st.sidebar.date_input('What is the date of your excursion')
type = st.sidebar.selectbox('What is your excursion type', ['Sail', 'Golf', 'Scuba', 'ZipLine', 'Moped', 'Other'])
cost = st.sidebar.number_input('What is the Total Cost of Your Excursion?')

uploaded_file = st.sidebar.file_uploader('Upload Copy of Receipt')

#Set domain for API calls
domain = 'https://api.openweathermap.org/data/3.0/onecall&lat=21.31&lon=-157.86&exclude=current,minutely,hourly,alerts&units=imperial&appid='

# Load credentials for the API calls into the auth variable
#credential_upload = st.file_uploader('Upload Open Weather MAP API credentials')
#if credential_upload:
#    creds = []
#    for line in credential_upload:
#        creds.append(line.decode().strip())
#    auth = (creds[0])

st.image('./Images/logo.png')

#st.caption('Upload the API key within a .txt file', unsafe_allow_html = True)

# Create a button to generate the forecast
#if st.button('Generate Forecast'):
#    st.write('generating forecast')
#st.write()


st.header('Find the 30 year historical weather conditions for the day of excursion here:')


#Tutorial available at: https://towardsdatascience.com/make-dataframes-interactive-in-streamlit-c3d0c4f84ccb
#AgGrid(historical_weather)
gb = GridOptionsBuilder.from_dataframe(historical_weather)
gb.configure_pagination(paginationAutoPageSize=False) #Add pagination
gb.configure_side_bar() #Add a sidebar
gb.configure_selection('multiple', use_checkbox=True, groupSelectsChildren='Group checkbox select children') # Enable multirow selection
gridOptions = gb.build()

grid_response = AgGrid(
    historical_weather,
    gridOptions=gridOptions,
    data_return_mode='AS_INPUT',
    update_mode='MODEL_CHANGED',
    fit_columns_on_grid_load=False,
    theme='blue', #add the color to the table
    enable_enterprise_modules=True,
    height=350,
    width='100%',
    reload_data=True 
)

#historical_weather = grid_response['historical_weather']
#selected = grid_response['selected_rows']
#df = pd.DataFrame(selected) #pass the selected rows to a new dataframe df


def fetch(session, url):
    try:
        result = session.get(url)
        return result.json
    except Exception:
        return{}

#st.caption('Temperature: ')
#st.caption('Cloud Cover:')
#st.caption('Percipitation:')
#st.caption('Wind Speed:')

st.image('./Images/sail.png')

#st.header('Here is the 5 day weather forecast for your excursion location')

#st.image('./Images/scuba.png')

st.write('Based on the info provided & historical weather data you qualify for ExcurAssure!')
st.caption('Cost to insure your excursion: $87.50') #17.5% of $500 excursion.  Hard coded at this time
st.radio('Do you wish to proceed', ['Yes', 'No'])

st.button('Create Contract')



#if(st.sidebar.selectbox('Sail')):
 #   st.image('./Images/sail.png')

