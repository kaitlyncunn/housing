import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

df = pd.read_csv('housing.csv')

st.title('California Housing Date (1990) by Kaitlyn Cunningham')

st.subheader('See more filters in the sidebar:')

median_housing_price_filter = st.slider('choose min. house price', 0,500001,20)

df = df[df.median_house_value>median_housing_pirce_filter]

location_filter = st.sidebar.mulitselect('Choose Location',
    df.ocean_proximity.unique())

df = df[df.ocean_proximity.isin(location_filter)]

income = st.sidebar.radio(
    "select income level",
    ('low', 'medium', 'high'))

if income == 'low':
        df = df[df.median_income <= 2.5],
elif income == 'medium':
        df = df[df.median_income > 2.5 and df.median_income <+ 4.5],
else:
        df = df[df.median_income > 4.5]
        
st.map(df)

fig, ax = plt.subplots (figsize = (20, 5))
df.median_house_value.hist (ax=ax, bins=30)
st.pyplot(fig)