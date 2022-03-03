import streamlit as st
import pandas as pd


st.write("Our Dashboard")

df = pd.read_csv('data/2406/entries.csv')

"This is cool stuff right here"
st.write("Table 1")
st.dataframe(df)
