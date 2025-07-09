import os

def market_news_sentiment(ticker_symbol: str):
    """
    Fetches news sentiment for a given stock ticker symbol using the Alpha Vantage API.

    Args:
        ticker_symbol (str): The stock ticker symbol (e.g., 'AAPL', 'GOOGL').

    Returns:
        dict: A dictionary containing the news sentiment data.
    """
    import requests

    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
 # Replace with your actual API key
    url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers={ticker_symbol}&apikey={api_key}'
    
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch data from Alpha Vantage API"}

# url = 'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=demo'
# r = requests.get(url)
# data = r.json()

# print(data)