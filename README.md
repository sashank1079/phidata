# Financial Agent Chatbot

The Financial Agent Chatbot is a Python-based application that leverages AI-powered agents to assist with financial analysis and web-based research. This project integrates tools for stock price analysis, analyst recommendations, and the latest financial news to provide an interactive and efficient platform for investment analysis.

## Features

- **Financial Analysis**:
  - Provides stock prices, analyst recommendations, and stock fundamentals.
  - Formats responses in Markdown with tables for easy readability.

- **Web Search Integration**:
  - Retrieves the latest financial news and other relevant information using DuckDuckGo.

- **Interactive Interface**:
  - Built with the `phi` library's Playground, allowing seamless interaction with AI agents.

- **Multi-Agent Collaboration**:
  - Combines specialized agents for finance and web search to deliver comprehensive insights.

## Setup Instructions

### Prerequisites

1. **Python**: Ensure Python 3.8+ is installed. You can download it [here](https://www.python.org/downloads/).
2. **Install Required Libraries**: Dependencies are listed in the `requirements.txt` file.

### Usage
Financial Analysis:

Query the Finance Agent for stock prices, fundamentals, and analyst recommendations.
Web Search:

Ask the Web Search Agent for the latest financial news or information on specific topics.
Interactive Playground:

Access the AI agents through a web-based interactive interface. (Run the chatbot.py file)

### Technologies Used
Python: Core programming language.
phi Library: Used for building and managing AI agents.
OpenAI GPT: For natural language processing and financial analysis.
YFinance: For retrieving stock data.
DuckDuckGo Search: For web-based financial news and information.
FastAPI: For serving the interactive playground interface.
Uvicorn: ASGI server for running the application.


### Acknowledgements
OpenAI for the GPT models.
YFinance for stock market data.
DuckDuckGo for web search capabilities.
