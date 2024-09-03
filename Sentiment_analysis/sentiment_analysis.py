import streamlit as st



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


import streamlit as st
from textblob import TextBlob

# def initialize_sentiment_pipeline():
#     def analyze_sentiment(texts):
#         return [TextBlob(text).sentiment for text in texts]
#     return analyze_sentiment

# def fetch_news(query, language='en'):
#         api_key = "7c9628099fbd4d63be8c502113ad9ec7"  # Your News API key
#         url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={api_key}"
#         try:
#             response = requests.get(url, timeout=10)  # Add timeout to prevent hanging
#             response.raise_for_status()  # Check for request errors
#             news_data = response.json()
#             return news_data.get('articles', [])
#         except requests.exceptions.RequestException as e:
#             st.error(f"Error fetching news: {e}")
#             return []



# def analyze_sentiments(sentiment_pipeline, texts):
#     if sentiment_pipeline:
#         st.write("Analyzing sentiments...")
#         try:
#             return sentiment_pipeline(texts)
#         except Exception as e:
#             st.error(f"Error during sentiment analysis: {e}")
#             return []
#     else:
#         return []

# def show_sentiment_analysis():
#     st.title("Stock Market News Sentiment Analysis")

#     sentiment_pipeline = initialize_sentiment_pipeline()

#     stock_ticker = st.text_input("Enter the stock ticker or keyword to analyze:", "AAPL")

#     if st.button("Fetch News"):
#         with st.spinner("Fetching news articles..."):
#             articles = fetch_news(stock_ticker)
        
#         if articles:
#             st.write(f"Found {len(articles)} articles related to {stock_ticker}.")
            
#             max_articles = min(len(articles), 10)
#             with st.spinner("Analyzing sentiments..."):
#                 texts = [article['description'] for article in articles[:max_articles] if article['description']]
#                 if texts:
#                     sentiments = analyze_sentiments(sentiment_pipeline, texts)
                    
#                     st.subheader("Sentiment Analysis Results")
#                     for i, article in enumerate(articles[:max_articles]):
#                         st.write(f"**Title**: {article['title']}")
#                         st.write(f"**Description**: {article['description']}")
#                         if i < len(sentiments):
#                             st.write(f"**Sentiment**: {sentiments[i].label} (Confidence: {sentiments[i].score:.2f})")
#                         else:
#                             st.write("**Sentiment**: Not available")
#                         st.write("---")
#                 else:
#                     st.write("No descriptions found in the articles to analyze.")
#         else:
#             st.write("No articles found.")



# import streamlit as st
# from textblob import TextBlob
# import requests

# def initialize_sentiment_pipeline():
#     # Return a function for sentiment analysis using TextBlob
#     return TextBlob

# def fetch_news(stock_ticker):
#     # Dummy implementation for fetching news; replace with actual API call
#     return [
#         {"title": "Sample News", "description": "This is a sample news article."}
#     ]

# def analyze_sentiments(sentiment_pipeline, texts):
#     if sentiment_pipeline:
#         st.write("Analyzing sentiments...")
#         try:
#             return [sentiment_pipeline(text) for text in texts]
#         except Exception as e:
#             st.error(f"Error during sentiment analysis: {e}")
#             return []
#     else:
#         return []

# def show_sentiment_analysis():
#     st.title("Stock Market News Sentiment Analysis")

#     sentiment_pipeline = initialize_sentiment_pipeline()

#     stock_ticker = st.text_input("Enter the stock ticker or keyword to analyze:", "AAPL")

#     if st.button("Fetch News"):
#         with st.spinner("Fetching news articles..."):
#             articles = fetch_news(stock_ticker)
        
#         if articles:
#             st.write(f"Found {len(articles)} articles related to {stock_ticker}.")
            
#             max_articles = min(len(articles), 10)
#             with st.spinner("Analyzing sentiments..."):
#                 texts = [article['description'] for article in articles[:max_articles] if article['description']]
#                 if texts:
#                     sentiments = analyze_sentiments(sentiment_pipeline, texts)
                    
#                     st.subheader("Sentiment Analysis Results")
#                     for i, article in enumerate(articles[:max_articles]):
#                         st.write(f"**Title**: {article['title']}")
#                         st.write(f"**Description**: {article['description']}")
#                         if i < len(sentiments):
#                             sentiment = sentiments[i]
#                             polarity = sentiment.polarity
#                             sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
#                             st.write(f"**Sentiment**: {sentiment_label} (Polarity: {polarity:.2f})")
#                         else:
#                             st.write("**Sentiment**: Not available")
#                         st.write("---")
#                 else:
#                     st.write("No descriptions found in the articles to analyze.")
#         else:
#             st.write("No articles found.")



# def initialize_sentiment_pipeline():
#     # Return a function for sentiment analysis using TextBlob
#     return TextBlob

# def fetch_news(stock_ticker, num_articles=10):
#     # Dummy implementation for fetching latest news; replace with actual API call
#     return [
#         {"title": "Sample News", "description": "This is a sample news article with a positive sentiment."}
#         for _ in range(num_articles)
#     ]

# def analyze_sentiments(sentiment_pipeline, texts):
#     if sentiment_pipeline:
#         st.write("Analyzing sentiments...")
#         try:
#             return [sentiment_pipeline(text) for text in texts]
#         except Exception as e:
#             st.error(f"Error during sentiment analysis: {e}")
#             return []
#     else:
#         return []

# def get_signal_from_sentiments(sentiments):
#     positive_count = sum(1 for sentiment in sentiments if sentiment.polarity > 0)
#     negative_count = sum(1 for sentiment in sentiments if sentiment.polarity < 0)
    
#     if positive_count > negative_count:
#         return "Buy"
#     elif negative_count > positive_count:
#         return "Sell"
#     else:
#         return "Hold"

# def show_sentiment_analysis():
#     st.title("Stock Market News Sentiment Analysis")

#     sentiment_pipeline = initialize_sentiment_pipeline()

#     stock_ticker = st.text_input("Enter the stock ticker or keyword to analyze:", "AAPL")

#     if st.button("Fetch News"):
#         with st.spinner("Fetching news articles..."):
#             articles = fetch_news(stock_ticker, num_articles=10)
        
#         if articles:
#             st.write(f"Found {len(articles)} articles related to {stock_ticker}.")
            
#             max_articles = min(len(articles), 10)
#             with st.spinner("Analyzing sentiments..."):
#                 texts = [article['description'] for article in articles[:max_articles] if article['description']]
#                 if texts:
#                     sentiments = analyze_sentiments(sentiment_pipeline, texts)
                    
#                     # Determine the overall market signal
#                     overall_signal = get_signal_from_sentiments(sentiments)
                    
#                     # Display the overall market signal at the top
#                     st.subheader("Overall Market Signal")
#                     st.write(f"The overall market signal based on the latest news is: **{overall_signal}**")
                    
#                     st.subheader("Sentiment Analysis Results")
#                     for i, article in enumerate(articles[:max_articles]):
#                         st.write(f"**Title**: {article['title']}")
#                         st.write(f"**Description**: {article['description']}")
#                         if i < len(sentiments):
#                             sentiment = sentiments[i]
#                             polarity = sentiment.polarity
#                             sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
#                             st.write(f"**Sentiment**: {sentiment_label} (Polarity: {polarity:.2f})")
#                         else:
#                             st.write("**Sentiment**: Not available")
#                         st.write("---")
#                 else:
#                     st.write("No descriptions found in the articles to analyze.")
#         else:
#             st.write("No articles found.")



#-------

import streamlit as st
import requests
from textblob import TextBlob

# Function to fetch news articles from the News API
def fetch_news(query, language='en', num_articles=10):
    api_key = "7c9628099fbd4d63be8c502113ad9ec7"  # Your News API key
    url = f"https://newsapi.org/v2/everything?q={query}&language={language}&apiKey={api_key}&pageSize={num_articles}"
    try:
        response = requests.get(url, timeout=10)  # Add timeout to prevent hanging
        response.raise_for_status()  # Check for request errors
        news_data = response.json()
        return news_data.get('articles', [])
    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching news: {e}")
        return []

# Initialize the sentiment analysis pipeline
def initialize_sentiment_pipeline():
    return TextBlob

# Analyze sentiments of fetched texts
def analyze_sentiments(sentiment_pipeline, texts):
    if sentiment_pipeline:
        st.write("Analyzing sentiments...")
        try:
            return [sentiment_pipeline(text) for text in texts]
        except Exception as e:
            st.error(f"Error during sentiment analysis: {e}")
            return []
    else:
        return []

# Determine market signal based on sentiment analysis results
def get_signal_from_sentiments(sentiments):
    positive_count = sum(1 for sentiment in sentiments if sentiment.polarity > 0)
    negative_count = sum(1 for sentiment in sentiments if sentiment.polarity < 0)
    
    if positive_count > negative_count:
        return "Buy"
    elif negative_count > positive_count:
        return "Sell"
    else:
        return "Hold"

# Show sentiment analysis results in the Streamlit app
def show_sentiment_analysis():
    st.title("Stock Market News Sentiment Analysis")

    sentiment_pipeline = initialize_sentiment_pipeline()

    stock_ticker = st.text_input("Enter the stock ticker or keyword to analyze:", "AAPL")

    if st.button("Fetch News"):
        with st.spinner("Fetching news articles..."):
            articles = fetch_news(stock_ticker, num_articles=10)
        
        if articles:
            st.write(f"Found {len(articles)} articles related to {stock_ticker}.")
            
            max_articles = min(len(articles), 10)
            with st.spinner("Analyzing sentiments..."):
                texts = [article['description'] for article in articles[:max_articles] if article['description']]
                if texts:
                    sentiments = analyze_sentiments(sentiment_pipeline, texts)
                    
                    # Determine the overall market signal
                    overall_signal = get_signal_from_sentiments(sentiments)
                    
                    # Display the overall market signal at the top
                    st.subheader("Overall Market Signal")
                    st.write(f"The overall market signal based on the latest news is: **{overall_signal}**")
                    
                    st.subheader("Sentiment Analysis Results")
                    for i, article in enumerate(articles[:max_articles]):
                        st.write(f"**Title**: {article['title']}")
                        st.write(f"**Description**: {article['description']}")
                        if i < len(sentiments):
                            sentiment = sentiments[i]
                            polarity = sentiment.polarity
                            sentiment_label = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"
                            st.write(f"**Sentiment**: {sentiment_label} (Polarity: {polarity:.2f})")
                        else:
                            st.write("**Sentiment**: Not available")
                        st.write("---")
                else:
                    st.write("No descriptions found in the articles to analyze.")
        else:
            st.write("No articles found.")
