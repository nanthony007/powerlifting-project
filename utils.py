import streamlit as st
import pandas as pd


@st.cache
def load_data() -> pd.DataFrame:
    data = pd.read_feather("./data/openipf.feather")
    return data
