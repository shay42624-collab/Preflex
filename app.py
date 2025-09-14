import streamlit as st

st.set_page_config(page_title="Preflex AI", page_icon="📊")
st.title("📊 Welcome to Preflex AI")

st.write("Upload your customer data to get powerful insights into behavior, preferences, and trends.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    import pandas as pd
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of your data", df.head())
