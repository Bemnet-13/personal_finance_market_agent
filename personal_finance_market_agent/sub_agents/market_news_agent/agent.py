"""News sentiment analysis agent for market news"""

from google.adk import Agent

from . import prompt
from personal_finance_market_agent.tools.news_sentiment import market_news_sentiment

MODEL="gemini-2.5-pro"

market_news_agent = Agent(
    model=MODEL,
    name="market_news_agent",
    instruction=prompt.NEWS_AGENT_PROMPT,
    tools=[market_news_sentiment],
    output_key="news_sentiment_analysis_output",
)