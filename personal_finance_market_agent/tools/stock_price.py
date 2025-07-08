"""Custom tool to fetch data from the Alpha Vantage API."""

import os
import requests

def get_stock_market_data(
    symbol: str,
    function: str,
    time_period: int = 60
) -> dict:
    """
    Fetches financial data for a given stock symbol from the Alpha Vantage API.

    To use this tool, you MUST first get a free API key from Alpha Vantage
    and set it as an environment variable named 'ALPHA_VANTAGE_API_KEY'.

    Args:
        symbol: The stock ticker symbol (e.g., 'GOOGL', 'MSFT').
        function: The specific Alpha Vantage function to call. Must be one of:
                  'TIME_SERIES_DAILY_ADJUSTED' - Gets daily open, high, low, close, volume.
                  'OVERVIEW' - Gets company details like Market Cap, P/E Ratio, 52-week high/low.
                  'SMA' - Calculates the Simple Moving Average. Requires 'time_period'.
                  'RSI' - Calculates the Relative Strength Index. Requires 'time_period'.
        time_period: The time period in days for technical indicators like SMA or RSI.
                     Default is 60. This is ignored by OVERVIEW and TIME_SERIES_DAILY_ADJUSTED.

    Returns:
        A dictionary containing the JSON response from the Alpha Vantage API.
    """
    api_key = os.getenv("ALPHA_VANTAGE_API_KEY")
    if not api_key:
        raise ValueError("ALPHA_VANTAGE_API_KEY environment variable not set.")

    base_url = "https://www.alphavantage.co/query"
    params = {
        "symbol": symbol,
        "function": function,
        "apikey": api_key
    }

    # Add parameters specific to certain functions
    if function in ['SMA', 'RSI']:
        params['interval'] = 'daily'
        params['time_period'] = str(time_period)
        params['series_type'] = 'close'

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API request failed: {e}"}
    except ValueError as e:
        # For JSON decoding errors
        return {"error": f"Failed to decode API response: {e}"}