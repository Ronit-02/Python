import streamlit as st
import pandas as pd
import numpy as np


st.markdown("#  Main Page")
st.sidebar.markdown("# Main Page")


if st.checkbox('Show table'):
    "## Regular data table"

    df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

    st.caption("just a random data")
    st.table(df)



"## Random number line chart "

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)



"## This is Square widget"

x = st.slider('x')
st.write(x, 'squared is', x * x)



"## Enter your name here!"

st.text_input("Your name", key="name")
st.write(st.session_state.name, " is the user")



df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })



"## Lucky number"

arr= [1,2,3,4,5,6,7,8,9]
option = st.selectbox(
    'Choose your number',
     arr)

'Your lucky number is : ', option

