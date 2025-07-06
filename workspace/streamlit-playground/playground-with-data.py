import streamlit as st
import pandas as pd

st.title("Data Playground")

file = st.file_uploader("upload you csv file", type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)


if file:
    st.subheader("Data Summary")
    st.write(df.describe())


if file:
    genders= df["Sex"].unique()
    gender=st.selectbox("Select the Gender",genders)
    filtered_df=df[df["Sex"] == gender]
    st.dataframe(filtered_df)
    
