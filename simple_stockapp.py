import yfinance as yfinance
import streamlit as streamlit
import pandas as pandas


st.write(
"""

Closing Price of Stock

""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2010-5-31', end = '2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)