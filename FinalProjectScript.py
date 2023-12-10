import streamlit as st
import pandas as pd

import numpy as np
import pandas as pd
import seaborn as sns
import altair as alt
import matplotlib.pyplot as plt
import plotnine as p9
from plotnine import *
import numpy as np
import statsmodels.formula.api as smf



st.markdown('Hello')
st.markdown('Holy **** its working!')

st.markdown('Rerun testing')

user_name = st.text_input('What is your name?')
if user_name: 
    st.write(f'{user_name} is a very nice name')


question = st.text_input('Who is the TEST mom in the world?')
if question:
    st.write(f'{user_name} is the best mom in the world')
