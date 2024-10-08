import streamlit as st
from prophet import Prophet
import pandas as pd
from prophet.plot import plot_plotly
import yfinance as yf
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date, timedelta
import plotly.graph_objects as go
from statsmodels.tsa.arima.model import ARIMA
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from prophet import Prophet
from prophet.plot import plot_plotly
from scipy.stats import skew, kurtosis
import requests
from transformers import pipeline
import torch
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
from scipy.stats import zscore
import plotly.graph_objects as go
from sklearn.model_selection import ParameterGrid

def show_stock_price_prediction():
    st.title("Stock Price Prediction with Prophet")

    @st.cache
    def get_data():
        path = 'stock.csv'
        return pd.read_csv(path, low_memory=False)

    df = get_data()
    df = df.drop_duplicates(subset="Name", keep="first")

    START = "2015-01-01"
    TODAY = date.today().strftime("%Y-%m-%d")

    st.title("Stock Prediction")
    st.write("###")

    stocks = df['Name']
    selected_stock = st.selectbox("Select dataset and years for prediction", stocks)

    index = df[df["Name"] == selected_stock].index.values[0]
    symbol = df["Symbol"][index]

    n_years = st.slider("", 1, 5)
    period = n_years * 365

    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    data_load_state = st.text("Load data ...")
    data = load_data(symbol)
    data_load_state.text("Loading data ... Done!")

    st.write("###")

    st.subheader("Raw data")
    st.write(data.tail())

    def plot_raw_data():
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name='stock_open'))
        fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name='stock_close'))
        fig.layout.update(title_text="Time Series Data", xaxis_rangeslider_visible=True)
        st.plotly_chart(fig)

    plot_raw_data()

    # Forecasting
    df_train = data[['Date', 'Close']]
    df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

    m = Prophet()
    m.fit(df_train)

    future = m.make_future_dataframe(periods=period)
    forecast = m.predict(future)

    st.write("***")
    st.write("###")

    st.subheader("Forecast data")
    st.write(forecast.tail())

    fig1 = plot_plotly(m, forecast)
    st.plotly_chart(fig1)

    st.subheader("Forecast Components")
    fig2 = m.plot_components(forecast)
    st.write(fig2)

