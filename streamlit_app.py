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

st.header('st.write')

st.write('Helo, *World!* :sunglasses:')
st.write(1234)
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]})
st.write(df)
st.write('Below is a DtaFrame:', df, 'Above is a dataframe.')
df2 = pd.DataFrame(
    np.random.randn(200, 3),
     columns=['a', 'b', 'c'])
c = alt.Chart(df2).mark_circle().encode(
     x='a', y='b', size='c', color='c', tooltip=['a', 'b', 'c'])
st.write(c)