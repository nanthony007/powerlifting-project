import streamlit as st
import utils


df = utils.load_data()

st.write("Our Dashboard")

"This is cool stuff right here"
st.header("Entries/Athletes:")
st._legacy_dataframe(df.head(100))

st.header("Meets:")
st._legacy_dataframe(df.head(100))
