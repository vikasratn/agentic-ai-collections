import streamlit as st
from datetime import datetime

st.title("Mobile App Maker")

if st.button("Make App"):
    st.success("Your App is Ready")


add_permission= st.checkbox("Add Location Permission")

if add_permission:
    st.write("Location Permission Addes to the App")


    
tea_type = st.radio("Pick the OS",["None","Andriod","iOS"])

if tea_type == 'Andriod':
    st.success("Andriod Operating System Selected.")
elif tea_type == 'Andriod':
    st.success("Apple IOS Operating System Selected.")
else:
    st.success("None Operating System Selected.")


manufaturer = st.selectbox("Select your target Mobile Manufaturer",["Samsung","Apple","Redime"])

st.success(f"The manufaturer is {manufaturer}")

month=st.slider("Month of manufacturing",1,12,4)

st.success(f"The manufaturing month is {month}")

quantity = st.number_input("App quantity",min_value=2,max_value=10,step=2)

st.success(f"The App quantity is {quantity}")

name = st.text_input("The customer name")
if name:
    st.success(f"Thank for giving order {name}")

order_date = st.date_input("Provide the Order Date")
if order_date:
    # Get today's date
    today = datetime.today().date()
    # Calculate the difference
    days_difference = (today - order_date).days
    st.success(f"Your consignment will be dispetched in {days_difference} days")
