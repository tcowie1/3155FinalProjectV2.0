import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
from collections import namedtuple
import altair as alt
import math

def app():

#Home and Navigation Setup
st.set_page_config(page_title='UniSight', page_icon=":goat:")
"""
# UniSight

At UniSight, we want to provide accessible, easy-to-read data and 
visuals to help potential and current students make informed decisions 
on college degrees and the careers they lead to. Guiding individuals through 
major college and career decisions, with up-to-date information, is our 
objective.

"""
#Sidebar Navigation
st.sidebar.header("Home")
navChoice = st.sidebar.selectbox('Navigation', ('Home', 'Salaries', 'Loans'))
