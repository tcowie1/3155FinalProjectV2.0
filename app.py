import streamlit as st
#Page Config
st.set_page_config(initial_sidebar_state="collapsed")
from multiapp import MultiApp
from apps import home, loans, salaries # import your app modules here

#st.set_page_config(page_title='UniSight', page_icon=":goat:")  #These dont work with multipage. Need to investigate.

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Loans", loans.app)
app.add_app("Salaries", salaries.app)

# The main app
app.run()