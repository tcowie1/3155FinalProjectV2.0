import streamlit as st
import pandas as pd
import numpy as np
import math
import altair as alt
from collections import namedtuple
from data.create_data import create_table

def app():
    st.title('UniSight')
    st.write("At Unisight, we want to provide accessable, easy-to-read data and visuals to help potential and current students make informed decisions on college degrees")
    st.write("See `apps/home.py` to know how to use it.")

    st.markdown("### Sample Data")
    df = create_table()
    st.write(df)

    st.write('Navigate to `Data Stats` page to visualize the data')

