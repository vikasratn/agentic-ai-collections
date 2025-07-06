import streamlit as st
import requests
st.title("Currency Converter")

amount=st.number_input("Enter the amount (INR) :",min_value=1)

target_currency=st.selectbox("Convert to : ",["USD","GBP","EUR"])

if st.button("Convert"):
    url="https://api.exchangerate-api.com/v4/latest/INR"
    response=requests.get(url)

    if response.status_code == 200:
        data= response.json()
        rate= data["rates"][target_currency]
        converted = amount * rate
        st.success(f"{amount} INR  = {converted:.2f} {target_currency}")
    else:
        st.error("Currency Conversion failed")
