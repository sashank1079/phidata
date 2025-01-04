import phi
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
import openai
import os 
from dotenv import load_dotenv

from phi.playground import Playground, serve_playground_app

load_dotenv()
phi.api =os.getenv('PHIDATA_API_KEY')
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
    name= "Finance Agent",
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tool_calls=True,
    model = OpenAIChat(id="gpt-4o"),
    description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
    instructions=["Format your response using markdown and use tables to display data where possible."],
    markdown=True,
)

app= Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("chatbot:app",reload=True)
