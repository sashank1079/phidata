# AI Agent Suite with Phidata Playground

This repository features a suite of AI-powered agents designed to assist with various tasks, including video analysis, financial data retrieval, and PDF document processing. Leveraging the Phidata Playground, these agents provide an interactive platform for efficient data analysis and research.

## Table of Contents

- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Agents](#running-the-agents)



## Features

- **Video Analyzer Agent**: Analyzes video content to extract key information and insights.
- **Financial Agent**: Retrieves and analyzes financial data, including stock prices, analyst recommendations, and company news.
- **PDF Assistant**: Processes PDF documents to extract and summarize relevant information.
- **Interactive Interface**: Utilizes the Phidata Playground for seamless interaction with AI agents.

## Setup Instructions

### Prerequisites

- **Python**: Ensure Python 3.8 or higher is installed. Download it from the [official website](https://www.python.org/downloads/).
- **Phidata**: Install the Phidata library to utilize the Playground feature.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sashank1079/phidata.git
   cd phidata

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Agents

**1. Video Analyzer agent:**
    ```
    streamlit run video_analyzer.py
    ```

**2. Financial agent:**
    ```
    python financial_agent.py
    ```

**3. PDF assistant agent:**
    ```
    python pdfassistant.py
    ```

