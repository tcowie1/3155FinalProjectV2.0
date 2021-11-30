import streamlit as st
from multiapp import MultiApp
from apps import home, data_stats, loans # import your app modules here

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("Loans", loans.app)

# The main app
app.run()