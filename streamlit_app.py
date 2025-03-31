"""
30 days of Streamlit practice

to open streamlit demo in cmd line:

python -m streamlit hello

"""

#day 1 Launch demo app

#day 2 Make own streamlit
import streamlit as st

#st.write('Hello World!')

#day 3 button

# st.header('st.button')
# if st.button('Say hello'): #if you button is clicked
#     st.write('Why hello there')
# else:
#     st.write('Goodbye') #written by default 


#day 4 long video

#day 5

#st.write displays text like a print statment
#but also displays dicts, pandas DataFrame, and plots

import numpy as np
import altair as alt
import pandas as pd

# st.header('st.write')

# st.write('Helo, *World!* :sunglasses:')
# st.write(1234)
# df = pd.DataFrame({
#     'first column': [1,2,3,4],
#     'second column': [10,20,30,40]})
# st.write(df)
# st.write('Below is a DtaFrame:', df, 'Above is a dataframe.')
# df2 = pd.DataFrame(
#     np.random.randn(200, 3),
#      columns=['a', 'b', 'c'])
# c = alt.Chart(df2).mark_circle().encode(
#      x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
# st.write(c)

#day 8 slider
from datetime import time, datetime

# st.header('st.slider')

# st.subheader('Slider')
# age = st.slider('How old are you?', 0, 130, 25)
# st.write("I'm ", age, 'years od')
# st.subheader('Range slider')
# values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
# st.write('Values:', values)
# st.subheader('Range time slider')
# appointment = st.slider(
#     "Schedule your appointment:", value=(time(11, 30), time(12, 45))
# )
# st.write("You're scheduled for:", appointment)
# st.subheader('Datetime slider')
# start_time = st.slider(
#     "When do you start?", value=datetime(2020, 1, 1, 9, 30), format="MM/DD/YY - hh:mm")
# st.write("Start time:", start_time)

#Day 9 st.line_chart

# st.header('Line chart')
# chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
# st.line_chart(chart_data)

#day 10 st.select box

# st.header('st.selectbox')
# option = st.selectbox('What is your favorite color?', ('Blue', 'Red', 'Green'))
# st.write('Your favorite color is ', option)

#day 11 st.multiselect

# st.header('st.multiselect')
# options = st.multiselect('What are your favorite colors', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
# st.write('You selected:', options)

#day 12 st.checkbox

st.header('st.checkbox')
st.write('What would you like to order?')
icecream = st.checkbox('Ice cream')
coffee = st.checkbox('Coffee')
cola = st.checkbox('Cola')

if icecream:
    st.write("Great! Here's some more :icecream:")
if coffee:
    st.write("Okay, here's some coffee :coffee:")
if cola:
    st.write("Here you go :drink:")