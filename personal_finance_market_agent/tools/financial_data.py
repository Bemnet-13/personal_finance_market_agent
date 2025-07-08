import yfinance as yf

def financial_data(ticker_name: str):
    """
    Fetches comprehensive financial data for a given ticker using yfinance.

    Args:
        ticker_name (str): The stock ticker symbol.

    Returns:
        dict: Dictionary containing key financial metrics and full financial statements.
    """
    ticker = yf.Ticker(ticker_name)
    info = ticker.info

    # Get financial statements as DataFrames and convert to dict
    try:
        financials = ticker.financials.to_dict() if hasattr(ticker, "financials") and ticker.financials is not None else {}
    except Exception:
        financials = {}

    try:
        balance_sheet = ticker.balance_sheet.to_dict() if hasattr(ticker, "balance_sheet") and ticker.balance_sheet is not None else {}
    except Exception:
        balance_sheet = {}

    try:
        cashflow = ticker.cashflow.to_dict() if hasattr(ticker, "cashflow") and ticker.cashflow is not None else {}
    except Exception:
        cashflow = {}

    data = {
        "Market Cap": info.get("marketCap", "Not Available"),
        "P/E Ratio": info.get("trailingPE", "Not Available"),
        "52-Week High": info.get("fiftyTwoWeekHigh", "Not Available"),
        "52-Week Low": info.get("fiftyTwoWeekLow", "Not Available"),
        "Previous Close": info.get("previousClose", "Not Available"),
        "Open": info.get("open", "Not Available"),
        "Volume": info.get("volume", "Not Available"),
        "Currency": info.get("currency", "Not Available"),
        "Short Name": info.get("shortName", "Not Available"),
        "Sector": info.get("sector", "Not Available"),
        "Industry": info.get("industry", "Not Available"),
        # "Financials": financials,
        # "Balance Sheet": balance_sheet,
        # "Cashflow": cashflow,
    }
    return data

# print(financial_data("GOOGL"))