# from google.adk.agents import Agent
# from google.adk.tools import google_search

# from personal_finance_market_agent import prompt  # Import the tool
# from personal_finance_market_agent.sub_agents.price_agent.agent import price_agent

# root_agent = Agent(
#    name="root_agent",
#    model="gemini-2.0-flash-exp",
#    description="A Personal Finance & Market Watch assistant that serve as an advisor by using live price updates, news summaries, analytics indicators, and market alerts.",
#    instruction=prompt.ROOT_AGENT_INSTR,
#    sub_agents=[price_agent],
#    tools=[],
# )




from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from . import prompt
from personal_finance_market_agent.sub_agents.data_analyst_agent.agent import data_analyst_agent
from personal_finance_market_agent.sub_agents.trading_analyst_agent.agent import trading_analyst_agent
from personal_finance_market_agent.sub_agents.execution_analyst_agent.agent import execution_analyst_agent
from personal_finance_market_agent.sub_agents.risk_analyst_agent.agent import risk_analyst_agent

MODEL = "gemini-2.0-flash-exp"


financial_coordinator = LlmAgent(
    name="financial_coordinator",
    model=MODEL,
    description=(
        "guide users through a structured process to receive financial "
        "advice by orchestrating a series of expert subagents. help them "
        "analyze a market ticker, develop trading strategies, define "
        "execution plans, and evaluate the overall risk."
    ),
    instruction=prompt.FINANCIAL_COORDINATOR_PROMPT,
    output_key="financial_coordinator_output",
    tools=[
        AgentTool(agent=data_analyst_agent),
        AgentTool(agent=trading_analyst_agent),
        AgentTool(agent=execution_analyst_agent),
        AgentTool(agent=risk_analyst_agent),
    ],
)

root_agent = financial_coordinator