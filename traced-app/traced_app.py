
import os
from pathlib import Path
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# Load environment variables from the project folder
env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)

# Check required API keys
required_keys = ["OPENAI_API_KEY", "LANGSMITH_API_KEY"]

for key in required_keys:
    if not os.getenv(key):
        raise ValueError(f"{key} is missing. Check your .env file.")

if os.getenv("LANGSMITH_TRACING", "").lower() != "true":
    raise ValueError("LangSmith tracing is not enabled.")

print("Environment configuration loaded successfully!")
print("OpenAI API key: Configured")
print("LangSmith API key: Configured")
print("Tracing:", os.getenv("LANGSMITH_TRACING"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))

# Initialize the language model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Three test prompts
prompts = [
    "Explain artificial intelligence in two sentences.",

    "Explain five ways AI can improve Shopee, Lazada and TikTok Shop operations.",

    """Act as an e-commerce operations consultant.
    Explain how AI can automate order processing,
    returns, refunds, shipping follow-ups and product
    listing management across Thailand, Singapore
    and Malaysia.
    Include challenges, opportunities and business benefits."""
]

# Execute prompts
for i, prompt in enumerate(prompts, start=1):
    print("\n" + "=" * 50)
    print(f"RUN {i}")
    print("=" * 50)

    response = llm.invoke(prompt)

    print("Prompt:", prompt)
    print("Response:", response.content)

print("\nAll three prompts completed successfully!")
