"""Shared Gemini client setup for the classroom examples."""

import os

from google import genai


def create_client():
    """Create a Gemini client using an environment variable."""
    api_key = "AQ.Ab8RN6JfyllxRBtnEyn_Mv0Bq7w9KM735-lrmcv1bOxp34mpNg"
    if not api_key:
        raise RuntimeError(
            "Set GEMINI_API_KEY before running this example."
        )

    return genai.Client(api_key=api_key)


def model_name():
    """Return the configured model or a small general-purpose default."""
    return os.getenv("GEMINI_MODEL", "gemini-3.8-flash")
