import streamlit as st
from main import get_exchange_rate, convert_currency
from constants import curencies

st.title(":moneybag: Currency convertor")
st.write("You can use this tool to calculate currency exchange")

base = st.selectbox('From:', curencies)
target = st.selectbox('To: ', curencies)
amount = st.number_input('Enter number', min_value=0.0, value=100.0)

if amount > 0 and base and target:
    exchange_rate = get_exchange_rate(base, target)
    converted_amount = convert_currency(amount, exchange_rate)
    

st.success(f'{converted_amount}')