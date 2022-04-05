import streamlit as st
import utils


df = utils.load_data()
utils.initialize_sidebar()
st.write("Our Dashboard")

"This is cool stuff right here"

user_input = st.text_input("What is your name?")
if user_input:
    st.write("Hello, %s" % user_input)
    user_table = df[df.Name == user_input]
    st.dataframe(user_table)
else:
    st.header("Entries/Athletes:")
    st.dataframe(df.head(100))
