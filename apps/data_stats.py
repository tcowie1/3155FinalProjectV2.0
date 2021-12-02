import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import re


def app():
    st.title('Data Stats')

    st.write("This page is used to compare graduation percentages per school in the US")

    st.markdown("### Sample Data")

    # 
    level = st.selectbox('Do you wish to view 2 year or 4 year institutions?', [
                          '2-year', '4-year'])
    df = create_table(level)
  
    
    school_choice = st.selectbox('Which school would you like to see data for?', df['chronname'])

    school_data = df[df['chronname']==school_choice]

    # st.plotly_chart(fig)

    # fig.update_layout(
    #     xaxis_tickangle=35,
    #     barmode='group',
    #     title="This graph is based on the current " + str(school_data['student_count'].values) + " enrolled at the time of sampling.",
    #     yaxis_title='Percent Graduated '
    #     )

    school_choice2 = st.selectbox('Select a second school to compare', df['chronname'])
    school_data2 = df[df['chronname']==school_choice2]

    if len(school_choice) and len(school_choice2):
    # fig2 = go.Figure()
        fig = go.Figure().set_subplots(1, 2,
                        shared_yaxes=True,
                        )
        # fig.add_trace(go.Bar(name='100% time taken to graduate', x=school_data['chronname'], y=school_data['grad_100_value']), row=1, col=1)
        # fig.add_trace(go.Bar(name='150% time taken to graduate', x=school_data['chronname'], y=school_data['grad_150_value']), row=1, col=1),
        fig.add_trace(go.Bar(x=school_data['chronname'], y=school_data['grad_100_value']), row=1, col=1)
        fig.add_trace(go.Bar(x=school_data['chronname'], y=school_data['grad_150_value']), row=1, col=1)
        fig.add_trace(go.Bar(x=school_data2['chronname'], y=school_data2['grad_100_value']), row=1, col=2)
        fig.add_trace(go.Bar(x=school_data2['chronname'], y=school_data2['grad_150_value']), row=1, col=2)
        fig.update_layout(
            barmode='group',
            yaxis_title='Percent Graduated',
            
            )
        fig.update_traces(showlegend=False)
        school_count = str(school_data['student_count'].values)
        school_count2 = str(school_data2['student_count'].values)
        for character in '[]':
            school_count = school_count.replace(character, '')
            school_count2 = school_count2.replace(character, '')

        st.write("This graph is based on the current `" + school_count + "` enrolled at the time of sampling.")
        st.write("This graph is based on the current `" + school_count2 + "` enrolled at the time of sampling.")
        st.plotly_chart(fig)

    else:
        return
    st.markdown("<h1 stlye='text-align: center;'> Description of Graph Above </h1>", unsafe_allow_html=True)
    st.markdown("""<div style='text-align: center;'>The above Graph represents the time students from each college take to finish their major. The bar to the very left
    of each graph represents the percentage of students who spent <strong>100%</strong> time (4/2 years depending on major) to complete their major.
    The Bar on the right represents the percentage of students who spent <strong>150%</strong> time (approx. 5-6 years/3-4 depending on major) to complete their major. </div>""", unsafe_allow_html=True)




    # st.write("### This graph is based on the current " + str(state_data['student_count'].values) + " enrolled at the time of sampling.")
    # st.markdown("### This graph is based on the current " + str(state_data2['student_count'].values) + " enrolled at the time of sampling.")

    # st.write(df)
    # st.write(state_data['student_count'])
    

