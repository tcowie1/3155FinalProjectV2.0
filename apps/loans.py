import streamlit as st
import numpy as np
import pandas as pd
import math
import altair as alt
from collections import namedtuple
from data.create_data import create_table

#We gotta make sure to put the data in the data folder and then import it correctly.

def app():
    st.title('Loans')

    st.write("Loans are something most students will have to face when going to college, however, many students especially at the highschool age aren't aware of the true cost of a loan they take out for college.")
    st.write("This simple calculator will show you what a loan can cost you by the time you pay it off.")

    st.markdown("### Plot Data")
    
