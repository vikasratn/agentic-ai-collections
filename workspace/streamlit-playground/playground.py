import streamlit as st

st.title("Welcome to My Playground")
st.subheader("Created by streamlit")
st.text("This is output of st.text")
st.write("This is output of st.write")

ground = st.selectbox("You favourite playground : ",["MCG","ACB","LCG"])

st.write(f"You have selected : {ground}")

st.success(f"Successfully selected {ground}")