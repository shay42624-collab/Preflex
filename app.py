import streamlit as st
import pandas as pd
import openai

openai.api_key = st.secrets["openai"]["api_key"]

st.set_page_config(page_title="Preflex AI", page_icon="📊")
st.title("📊 Welcome to Preflex AI")

st.write("Upload your customer data to get insights into behavior, preferences, and trends.")

uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("### Preview of your data", df.head())
    st.write("### Summary Statistics")
    st.write(df.describe())

    prompt = f"Analyze this customer data:\n{df.head(10).to_string()}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    st.write("### 🤖 GPT Insights")
    st.write(response.choices[0].message.content)
