import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt

st.title("📊 Simple Stock Dashboard")

ticker = st.text_input("Enter a stock ticker:", "AAPL")
data = yf.download(ticker, period="6mo", interval="1d")

st.line_chart(data["Close"])
st.write(data.tail())