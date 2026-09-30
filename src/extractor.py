# Extraction/business logic

from src.llm_client import extract_information
from src.prompts import SYSTEM_PROMPT, build_prompt

def extract_ticket(text: str): 

    user_prompt = build_prompt(text)

    result = extract_information(
        SYSTEM_PROMPT,
        user_prompt
    )

    return result