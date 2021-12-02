import pandas as pd
import numpy as np
degree_data = pd.read_excel('data/degrees-that-pay-back.xlsx')


def create_table(level):
    data = pd.read_excel('data/cc_institution_details.xlsx')
    
    df = pd.DataFrame(data, 
        columns=['chronname', 'state', 'level', 'student_count', 'grad_100_value', 'grad_150_value' ])

    if (level == '2-year'):
        df = pd.DataFrame(df[df['level']==level])
    elif (level == '4-year'): 
        df = pd.DataFrame(df[df['level']==level])

    

    return df

def create_degreedf():
    degree_df = pd.DataFrame(degree_data, 
        columns=['Undergraduate Major', 'start_med_salary', 'mid_med_salary', 'percent_change', 'mid-10', 'mid-25', 'mid-75', 'mid-90'])

    return degree_df




    hide_footer_style = """
    <style>
    .reportview-container .main footer {visibility: hidden;}    
    """
    st.markdown(hide_footer_style, unsafe_allow_html=True)