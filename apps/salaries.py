import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table

#We gotta make sure to put the data in the data folder and then import it correctly.

def app():
    #Title and Introduction
    st.title('Salaries')
    st.write("Salaries are something to hopefully expect once you finish you academic career, in this page we will dive into what the job market looks like for certain degree holders and what that will mean for your loan payments in realtion to your income.")
