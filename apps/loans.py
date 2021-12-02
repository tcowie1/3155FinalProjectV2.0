import streamlit as st
import numpy as np
import pandas as pd
import math
import altair as alt
from collections import namedtuple
#from data.create_data import create_table

#We gotta make sure to put the data in the data folder and then import it correctly as above^

def app():
    #Title and intro to loans area
    st.title('Loans')
    st.write("Loans are something most students will have to face when going to college, however, many students especially at the highschool age aren't aware of the true cost of a loan they take out for college.")

    #Basic loan cost calculator intro
    st.markdown("### Simple Loan Cost Calculator")
    st.write("This simple calculator will show you what a loan can cost you by the time you pay it off.")
    st.write("By default it is loaded with values based on the average student loan borower.")
    st.write("This calculator is not financial advice and should not be used for calculating your loan costs. Ask your lender for verified information.")

    #Loan Cost Calculator
    loanAmount = st.number_input('Loan Amount: $', min_value=0, value=30000, step=5000)
    interest = st.slider(label='Interest in %:', min_value=3, max_value=10, value=6 ,help='This is the Annual Percent Interest on the loan.')
    payoffTime = st.slider(label='Time to Payoff (Yrs):', min_value=0, max_value=30, value=18, help='This is the amount of time in years it will take for you to pay off the loan.')

    #Calculations
    interestPayed = (loanAmount * (interest / 100)) * payoffTime    #principle * rate * time
    st.markdown("### Interest Paid: " + str(interestPayed))
    st.markdown("### Total Cost of Loan: " + str(interestPayed + loanAmount))

    #Data Visaulization
    st.markdown("### Symons Data Area")

    #Sources
    st.markdown("### Sources")
    st.write("https://educationdata.org/average-student-loan-debt")
    st.write("https://educationdata.org/average-student-loan-debt")
    st.write("https://educationdata.org/average-student-loan-interest-rate#:~:text=5.8%25%20is%20the%20average%20student%20loan%20interest%20rate%20among%20all,rates%20fell%20an%20average%2031.24%25.")