import streamlit as st
import pandas as pd


@st.cache
def load_data() -> pd.DataFrame:
    data = pd.read_feather("./data/open-powerlifting.feather")
    return data


def initialize_sidebar():
    with st.sidebar:
        st.header("Filter")
        st.subheader("Athletes")
        st.sidebar.markdown(
            """
        ### Athlete
        """
        )
