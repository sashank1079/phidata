import streamlit as st
import google.generativeai as genai
from google.generativeai import upload_file, get_file

from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo

import time
import mimetypes
import tempfile
import os
from dotenv import load_dotenv
from pathlib import Path

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

# Streamlit page configuration
st.set_page_config(
    page_title="Video Summarizer",
    page_icon="🎥",
    layout="wide"
)

st.title("Video Summarizer Agent")
st.header("Built using Gemini Flash :)")

@st.cache_resource
def create_summarizer_agent() -> Agent:
    """
    Initializes and returns the summarizer agent with Gemini model and DuckDuckGo tool.
    """
    return Agent(
        name="Video Summarizer Agent",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

def upload_and_process_video(filepath: str):
    """
    Uploads a video file to the Generative AI service and waits until processing is complete.
    Returns the processed video object.
    """
    # Determine the MIME type (fallback if unknown)
    mime_type, _ = mimetypes.guess_type(filepath)
    if not mime_type:
        mime_type = "application/octet-stream"
    
    processed_video = upload_file(filepath, mime_type=mime_type)
    
    # Wait for video processing to complete
    while processed_video.state.name == "PROCESSING":
        time.sleep(1)
        processed_video = get_file(processed_video.name)
    
    return processed_video

def create_analysis_prompt(question: str) -> str:
    """
    Builds the prompt that instructs the agent on how to analyze the video.
    """
    return f"""
    Analyze the uploaded video for content and context.
    Respond to the following query using video insights and supplementary web research:
    {question}

    Don't use any words which may indicate that the video does not have relevant info. Use web search to fill in any information you need.
    Provide a firendly, detailed, and actionable response.
    Do not mention any tools you may use to gather information.
    Include any relevant links or images.
    """

def analyze_with_agent(agent: Agent, prompt: str, processed_video) -> str:
    """
    Runs the analysis prompt through the agent, referencing the processed video,
    and returns the agent's response content.
    """
    response = agent.run(prompt, videos=[processed_video])
    return response.content

# Initialize the summarizer agent
summarizer_agent = create_summarizer_agent()

# File uploader for video
uploaded_video = st.file_uploader(
    "Upload a video file",
    type=["mp4", "mov", "avi"],
    help="Upload a video for AI analysis"
)

if uploaded_video:
    # Save uploaded video to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
        temp_file.write(uploaded_video.read())
        video_filepath = temp_file.name

    # Display the uploaded video
    st.video(video_filepath, format="video/mp4", start_time=0)

    # Text area to receive user questions
    question = st.text_area(
        "Questions or Insights?",
        placeholder="Ask anything about the video's content. The AI will analyze and gather additional context as needed.",
        help="Provide specific questions or insights you want from the video."
    )

    # Button to trigger analysis
    if st.button("Analyze Video", key="analyze_video_button"):
        if not question:
            st.warning("Please provide a question or insight to analyze the video.")
        else:
            try:
                with st.spinner("Processing your video..."):
                    # Upload and process the video
                    processed_video = upload_and_process_video(video_filepath)
                    
                    # Build the analysis prompt
                    prompt = create_analysis_prompt(question)
                    
                    # Run the prompt through the agent
                    analysis_result = analyze_with_agent(summarizer_agent, prompt, processed_video)

                # Display the AI-generated analysis
                st.subheader("Analysis Result")
                st.markdown(analysis_result)

            except Exception as e:
                st.error(f"An error occurred during the analysis: {e}")
            finally:
                # Remove the temporary video file
                Path(video_filepath).unlink(missing_ok=True)
else:
    st.info("Upload a video file to begin analysis.")

# Additional custom styles (e.g., adjust the text area height)
st.markdown(
    """
    <style>
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
