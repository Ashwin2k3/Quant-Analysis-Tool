
from home import show_home
from quant_strategies.quantitative_trading_strategy import show_quantitative_trading_strategy
from Prediction_model.stock_price_prediction import show_stock_price_prediction
from Sentiment_analysis.sentiment_analysis import show_sentiment_analysis

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


# Dictionary to map page names to functions
pages = {
    "Home": show_home,
    "Quantitative Trading Strategy": show_quantitative_trading_strategy,
    "Stock Price Prediction": show_stock_price_prediction,
    "Sentiment Analysis": show_sentiment_analysis,
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()))

# Call the corresponding page function
pages[selection]()
