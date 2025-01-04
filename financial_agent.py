from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import openai
import os 

openai.api_key = os.getenv('OPENAI_API_KEY')

web_search_agent = Agent(
    name="Web Search agent",
    role = "Searcg the web for relevant information",
    model = OpenAIChat(id="gpt-4o"),
    tools=[DuckDuckGo()],
    show_tool_calls=True,
    markdown= True,
    description="You are  an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Always show sources of the informtion."],
) 

finance_agent = Agent(
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    model = OpenAIChat(id="gpt-4o"),
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True,
)

multi_ai_agent = Agent(
    team= [web_search_agent, finance_agent ],
    model = OpenAIChat(id="gpt-4o"),
    instructions= ["Always show sources of the informtion.","Format your response using markdown and use tables to display data where possible."],
    show_tool_calls=True,
    markdown=True,
)

multi_ai_agent.print_response("Summarize analyst recommendations and also share latest TSLA news.", stream=True)