from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY

def get_gemini_pro():
    """Returns Gemini 3.0 Pro configured for complex reasoning."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.0-pro", # Using user-requested model identifier
        google_api_key=GOOGLE_API_KEY,
        temperature=0.2, # Low temperature for factual reporting
        max_output_tokens=8192
    )

def get_gemini_flash():
    """Returns Gemini 3.0 Flash configured for speed/extraction."""
    return ChatGoogleGenerativeAI(
        model="gemini-3.0-flash", # Using user-requested model identifier
        google_api_key=GOOGLE_API_KEY,
        temperature=0.1,
        max_output_tokens=8192
    )
