"""
LLM model configuration for Open Sousveillance Studio System.

Provides configured Gemini models for different use cases:
- Pro: Complex reasoning, analysis, synthesis
- Flash: Fast extraction, simple tasks

Uses native google.genai SDK to avoid PyTorch/transformers dependency issues.
"""

import os
from typing import Any, Type, TypeVar
from google import genai
from google.genai import types
from pydantic import BaseModel

T = TypeVar('T', bound=BaseModel)


def _get_client() -> genai.Client:
    """Get configured Gemini client."""
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment variables.")
    return genai.Client(api_key=api_key)


class GeminiModel:
    """Wrapper for Gemini models with structured output support."""

    def __init__(self, model_name: str, temperature: float = 0.2, max_output_tokens: int = 8192):
        self.model_name = model_name
        self.temperature = temperature
        self.max_output_tokens = max_output_tokens
        self._client = None

    @property
    def client(self) -> genai.Client:
        if self._client is None:
            self._client = _get_client()
        return self._client

    def invoke(self, prompt: str) -> str:
        """Send a prompt and get a text response."""
        response = self.client.models.generate_content(
            model=self.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=self.temperature,
                max_output_tokens=self.max_output_tokens
            )
        )
        return response.text

    def with_structured_output(self, schema: Type[T]) -> "StructuredGeminiModel[T]":
        """Return a model that outputs structured data matching the schema."""
        return StructuredGeminiModel(self, schema)


class StructuredGeminiModel[T]:
    """Gemini model that returns structured Pydantic output."""

    def __init__(self, base_model: GeminiModel, schema: Type[T]):
        self.base_model = base_model
        self.schema = schema

    def invoke(self, prompt: str) -> T:
        """Send a prompt and get a structured response."""
        response = self.base_model.client.models.generate_content(
            model=self.base_model.model_name,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=self.base_model.temperature,
                max_output_tokens=self.base_model.max_output_tokens,
                response_mime_type="application/json",
                response_schema=self.schema
            )
        )

        # Parse JSON response into Pydantic model
        import json
        data = json.loads(response.text)
        return self.schema.model_validate(data)


def get_gemini_pro() -> GeminiModel:
    """Returns Gemini 2.5 Pro configured for complex reasoning."""
    return GeminiModel(
        model_name="gemini-2.5-pro",
        temperature=0.2,
        max_output_tokens=8192
    )


def get_gemini_flash() -> GeminiModel:
    """Returns Gemini 2.5 Flash configured for speed/extraction."""
    return GeminiModel(
        model_name="gemini-2.5-flash",
        temperature=0.1,
        max_output_tokens=8192
    )
