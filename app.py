import streamlit as st
from multiapp import MultiApp
from apps import home, loans, salaries # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Loans", loans.app)
app.add_app("Salaries", salaries.app)

# The main app
app.run()