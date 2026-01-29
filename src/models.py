"""
LLM model configuration for Alachua Civic Intelligence System.

Provides configured Gemini models for different use cases:
- Pro: Complex reasoning, analysis, synthesis
- Flash: Fast extraction, simple tasks
"""

import os
from langchain_google_genai import ChatGoogleGenerativeAI


def _get_api_key() -> str:
    """Get Google API key from environment."""
    key = os.getenv("GOOGLE_API_KEY")
    if not key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    return key


def get_gemini_pro():
    """Returns Gemini 2.5 Pro configured for complex reasoning."""
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-pro",
        google_api_key=_get_api_key(),
        temperature=0.2,  # Low temperature for factual reporting
        max_output_tokens=8192
    )


def get_gemini_flash():
    """Returns Gemini 2.5 Flash configured for speed/extraction."""
    return ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=_get_api_key(),
        temperature=0.1,
        max_output_tokens=8192
    )
