import os
from pathlib import Path
from dotenv import load_dotenv

# Load env vars from .env file
load_dotenv()

# API Keys
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
FIRECRAWL_API_KEY = os.getenv("FIRECRAWL_API_KEY")
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent
PROMPT_LIB_DIR = BASE_DIR / "prompt_library"
OUTPUT_DIR = BASE_DIR / "outputs"

# Ensure output directories exist
(OUTPUT_DIR / "daily").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "weekly").mkdir(parents=True, exist_ok=True)
(OUTPUT_DIR / "monthly").mkdir(parents=True, exist_ok=True)

if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in environment variables.")
