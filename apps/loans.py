import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table

#We gotta make sure to put the data in the data folder and then import it correctly.

def app():
    st.title('Loans')

    st.write("This is a sample data stats in the mutliapp.")
    st.write("See `apps/data_stats.py` to know how to use it.")

    st.markdown("### Plot Data")
    df = create_table()

    st.line_chart(df)
