import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from datetime import date
from scipy.stats import zscore
import plotly.graph_objects as go
from sklearn.model_selection import ParameterGrid

def show_quantitative_trading_strategy():
    # Load data function
    @st.cache
    def load_data(ticker):
        data = yf.download(ticker, START, TODAY)
        data.reset_index(inplace=True)
        return data

    # Initialize Streamlit app
    st.title("Optimized Statistical Arbitrage Trading Bot with Risk Management")

    # User inputs for stock tickers and number of years for simulation
    ticker1 = st.selectbox('Select first stock for pair trading', ('AAPL', 'MSFT', 'GOOGL', 'AMZN'))
    ticker2 = st.selectbox('Select second stock for pair trading', ('AAPL', 'MSFT', 'GOOGL', 'AMZN'))
    n_years = st.slider('Years of historical data:', 1, 10)
    initial_threshold = st.slider('Initial Z-score threshold for trading:', 1.0, 3.0, step=0.1)

    # Risk management inputs
    stop_loss = st.slider('Stop-loss percentage (0.01 = 1%)', 0.01, 0.1, step=0.01)
    take_profit = st.slider('Take-profit percentage (0.01 = 1%)', 0.01, 0.3, step=0.01)
    max_drawdown = st.slider('Maximum allowable drawdown percentage', 0.05, 0.3, step=0.01)
    max_concurrent_trades = st.slider('Maximum number of concurrent trades', 1, 5, step=1)

    # Capital invested
    capital_invested = st.number_input('Capital invested per trade (in USD):', min_value=0.0, value=1000.0)

    # Date range setup
    START = (date.today().replace(year=date.today().year - n_years)).strftime("%Y-%m-%d")
    TODAY = date.today().strftime("%Y-%m-%d")

    # Load stock data
    data1 = load_data(ticker1)
    data2 = load_data(ticker2)

    # Ensure the two data sets have the same date range
    data = pd.merge(data1[['Date', 'Close']], data2[['Date', 'Close']], on='Date', suffixes=(f'_{ticker1}', f'_{ticker2}'))

    st.write("### Stock Data")
    st.write(data.tail())

    # Calculate the spread and z-score for pair trading
    data['Spread'] = data[f'Close_{ticker1}'] - data[f'Close_{ticker2}']
    data['Z-Score'] = zscore(data['Spread'])

    # Initialize the 'PnL' and 'Cumulative PnL' columns
    data['PnL'] = 0.0
    data['Cumulative PnL'] = 0.0

    # Optimization: Define parameter grid
    param_grid = {'threshold': np.arange(1.0, 3.0, 0.1), 'lookback': range(20, 100, 10)}

    best_params = None
    best_sharpe = -np.inf

    # Function to calculate Sharpe Ratio with risk management
    def calculate_sharpe_ratio(data, threshold, lookback):
        data['Rolling Mean'] = data['Spread'].rolling(window=lookback).mean()
        data['Rolling Std'] = data['Spread'].rolling(window=lookback).std()
        data['Z-Score'] = (data['Spread'] - data['Rolling Mean']) / data['Rolling Std']

        data['Signal'] = 0
        data['Position'] = 0
        positions = 0
        cumulative_pnl = 0
        max_drawdown_reached = False
        message_printed = False  # Flag to ensure the message is printed only once

        for i in range(1, len(data)):
            if data['Z-Score'].iloc[i] > threshold:
                if positions < max_concurrent_trades:
                    data['Signal'].iloc[i] = -1  # Short the spread
                    positions += 1
            elif data['Z-Score'].iloc[i] < -threshold:
                if positions < max_concurrent_trades:
                    data['Signal'].iloc[i] = 1  # Long the spread
                    positions += 1

            data['Position'].iloc[i] = data['Signal'].cumsum().iloc[i]

            # Calculate PnL
            if positions > 0:
                data['PnL'].iloc[i] = data['Position'].iloc[i-1] * (data['Spread'].iloc[i] - data['Spread'].iloc[i-1]) * capital_invested

                # Apply stop-loss and take-profit
                if data['PnL'].iloc[i] / capital_invested < -stop_loss:
                    data['Signal'].iloc[i] = 0  # Close position
                    positions -= 1
                elif data['PnL'].iloc[i] / capital_invested > take_profit:
                    data['Signal'].iloc[i] = 0  # Close position
                    positions -= 1

                cumulative_pnl += data['PnL'].iloc[i]
                data['Cumulative PnL'].iloc[i] = cumulative_pnl

                # Check for maximum drawdown
                if data['Cumulative PnL'].iloc[i] < -max_drawdown * cumulative_pnl:
                    max_drawdown_reached = True
                    if not message_printed:  # Check if the message has been printed
                        #st.write("### Max Drawdown Limit Reached - Stopping Simulation")
                        message_printed = True  # Set flag to True after printing
                    break
            else:
                data['PnL'].iloc[i] = 0
                data['Cumulative PnL'].iloc[i] = cumulative_pnl

        sharpe_ratio = data['PnL'].mean() / data['PnL'].std() * np.sqrt(252) if data['PnL'].std() != 0 else 0
        return sharpe_ratio

    # Grid search for optimization
    for params in ParameterGrid(param_grid):
        threshold = params['threshold']
        lookback = params['lookback']
        sharpe_ratio = calculate_sharpe_ratio(data.copy(), threshold, lookback)
        if sharpe_ratio > best_sharpe:
            best_sharpe = sharpe_ratio
            best_params = params

    st.write(f"### Best Parameters Found")
    st.write(f"Optimal Z-score threshold: {best_params['threshold']}")
    st.write(f"Optimal lookback period: {best_params['lookback']} days")
    st.write(f"Best Sharpe Ratio: {best_sharpe:.2f}")

    # Plot optimized strategy
    calculate_sharpe_ratio(data, best_params['threshold'], best_params['lookback'])
    buy_signals = data[data['Signal'] == 1]
    sell_signals = data[data['Signal'] == -1]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data['Date'], y=data['Spread'], mode='lines', name='Spread'))
    fig.add_trace(go.Scatter(x=buy_signals['Date'], y=buy_signals['Spread'], mode='markers', marker=dict(color='green', size=10), name='Buy Signal'))
    fig.add_trace(go.Scatter(x=sell_signals['Date'], y=sell_signals['Spread'], mode='markers', marker=dict(color='red', size=10), name='Sell Signal'))
    fig.layout.update(title_text='Optimized Spread and Trading Signals', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig)

    fig2 = go.Figure()
    fig2.add_trace(go.Scatter(x=data['Date'], y=data['Cumulative PnL'], mode='lines', name='Cumulative PnL'))
    fig2.layout.update(title_text='Cumulative Profit and Loss (in USD)', xaxis_rangeslider_visible=True)
    st.plotly_chart(fig2)

    # Show trade metrics
    st.write(f"### Trade Metrics")
    st.write(f"Number of Trades: {len(buy_signals) + len(sell_signals)}")
    st.write(f"Total PnL: {data['PnL'].sum():.2f} USD")
    st.write(f"Max Drawdown: {max_drawdown * 100:.2f}%")

