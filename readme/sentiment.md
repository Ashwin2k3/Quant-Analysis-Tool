Here’s a `README.md` for your project:


# Stock Market Sentiment Analysis with Streamlit

This project is a Stock Market Sentiment Analysis tool built using `Streamlit`, `yfinance`, `requests`, and `TextBlob`. It analyzes real-time news articles related to specific companies, performs sentiment analysis, and generates a buy/sell/hold signal based on the sentiments.

## Features

- **Fetch company-specific news** using the News API.
- **Perform sentiment analysis** on the fetched news articles using TextBlob.
- **Generate trading signals** (Buy, Sell, Hold) based on sentiment analysis results.
- **Select stock ticker** from a global dataset and analyze relevant news.

Here’s an explanation of the code in the `README.md`:

### Libraries Used

1. **`yfinance`**: This library is used to access historical market data from Yahoo Finance, though it is not used in the provided code snippet.
2. **`requests`**: Used to make HTTP requests to external APIs, specifically the News API, to fetch news articles.
3. **`csv`**: Enables reading and writing of CSV (Comma Separated Values) files, which are used to load stock company data.
4. **`streamlit`**: A web application framework for building interactive apps in Python, used here to create a user interface for the sentiment analysis.
5. **`TextBlob`**: A library for processing textual data, specifically for performing sentiment analysis in this context.

### Functions Overview

#### 1. `load_company_data(file_path='stock.csv')`
- **Purpose**: Loads company data from a CSV file (`stock.csv`). The file contains stock symbols and company names. The data is stored in a dictionary where the stock symbol is the key.
- **Logic**: 
  - Reads the file using the `csv.DictReader` to interpret the CSV.
  - For each row, it extracts the stock symbol and company name, storing them in a dictionary.
  - Handles errors with `st.error` if the file cannot be loaded.
  
#### 2. `fetch_news(query, language='en', num_articles=10)`
- **Purpose**: Fetches news articles related to a specific company using the News API.
- **Logic**: 
  - Constructs the API request URL with the query, language, number of articles, and your News API key.
  - Uses `requests.get` to retrieve the news.
  - Raises errors if the request fails and returns a list of articles.
  - Timeout is set to 10 seconds to prevent the request from hanging.
  
#### 3. `initialize_sentiment_pipeline()`
- **Purpose**: Initializes the sentiment analysis pipeline.
- **Logic**: Returns the `TextBlob` library, which will be used to analyze the sentiment of news articles.

#### 4. `analyze_sentiments(sentiment_pipeline, texts)`
- **Purpose**: Analyzes the sentiments of the news articles' descriptions using `TextBlob`.
- **Logic**: 
  - It iterates through each text (article description) and applies `TextBlob` to analyze sentiment polarity.
  - Sentiment polarity: Positive (> 0), Negative (< 0), or Neutral (≈ 0).
  - Handles errors if the sentiment analysis fails and returns the results.

#### 5. `get_signal_from_sentiments(sentiments)`
- **Purpose**: Generates a trading signal based on the sentiment analysis results.
- **Logic**:
  - Counts the number of positive and negative sentiments from the analyzed articles.
  - Based on the counts:
    - More positive sentiments -> **Buy** signal.
    - More negative sentiments -> **Sell** signal.
    - Equal positive and negative sentiments -> **Hold** signal.

#### 6. `get_company_description(company_data, ticker)`
- **Purpose**: Builds a search query for the News API, specific to the company selected by the user.
- **Logic**:
  - Retrieves the company’s name based on the stock ticker from the `company_data` dictionary.
  - Constructs a search query using variations of the company name to ensure accurate news retrieval, avoiding ambiguous names.
  - If the company is not found, it returns the ticker as a fallback.

#### 7. `show_sentiment_analysis()`
- **Purpose**: This is the main function that integrates the other functions into a cohesive Streamlit app for sentiment analysis.
- **Logic**:
  - Displays the app title.
  - Loads the company data from the CSV file.
  - Provides a dropdown for selecting a stock ticker.
  - When the "Fetch News" button is clicked:
    1. Fetches news articles related to the selected stock.
    2. Analyzes the sentiment of the articles.
    3. Displays the overall market signal (Buy, Sell, Hold) based on sentiment.
    4. Shows individual article titles, descriptions, and sentiment analysis results.
  - Handles cases where no articles or descriptions are found.

### Flow of the Application

1. **Load Stock Data**: The app first loads the stock ticker and company names from the CSV file (`stock.csv`).
2. **Select Ticker**: The user selects a stock ticker from the dropdown menu.
3. **Fetch News**: When the user clicks "Fetch News," the app sends a request to the News API to retrieve relevant news articles about the selected company.
4. **Sentiment Analysis**: Once the news articles are retrieved, the app analyzes their sentiment using `TextBlob`, which determines whether the sentiment is positive, negative, or neutral.
5. **Market Signal**: Based on the results of the sentiment analysis, the app displays an overall market signal (Buy, Sell, Hold) and details about each article’s sentiment.

### Error Handling
- The code includes error handling for file reading, HTTP requests, and sentiment analysis. If any step fails, the app notifies the user via `st.error` messages in the Streamlit interface.

This combination of news fetching, sentiment analysis, and real-time interactivity provides users with a decision-support tool for stock market insights based on news articles.
