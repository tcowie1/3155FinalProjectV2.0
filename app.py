import streamlit as st
st.set_page_config(initial_sidebar_state="collapsed")
#st.set_page_config(page_title='UniSight', page_icon=":goat:")
from multiapp import MultiApp
from apps import home, loans, salaries, about, data_stats # import your app modules here

# hide_footer_style = """
#     <style>
#     .reportview-container .main footer {visibility: hidden;}    
#     """
# st.markdown(hide_footer_style, unsafe_allow_html=True)

app = MultiApp()

# Add all your application here
app.add_app("Home", home.app)
app.add_app("Loans", loans.app)
app.add_app("Salaries", salaries.app)
app.add_app("Data Stats", data_stats.app)
app.add_app("About", about.app)

# The main app
app.run()