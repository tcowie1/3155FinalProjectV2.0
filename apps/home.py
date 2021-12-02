import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
from collections import namedtuple
from data.create_data import create_table

def app():
    st.set_page_config(initial_sidebar_state="collapsed")
    st.title('UniSight')
    st.write("At Unisight, we want to provide accessable, easy-to-read data and visuals to help potential and current students make informed decisions on college degrees and the careers they lead to. Guiding individuals through major college and career decisions, with up-to-date information, is our objective.")



