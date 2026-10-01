# Communication with LLM provider

import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

from src.schemas import SupportTicketSchema

MAX_RETRIES = 3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def extract_information(system_prompt: str, user_prompt: str):
    for attempt in range(MAX_RETRIES):
        try:
            response = client.responses.parse(
                model="gpt-4o-mini",
                input=[
                    {
                        "role": "system",
                        "content": system_prompt,
                    },
                    {
                        "role": "user",
                        "content": user_prompt,
                    },
                ],
                text_format=SupportTicketSchema,
            )

            if response.output_parsed is None:
                raise ValueError("The model response did not contain parsed ticket data.")

            return response.output_parsed
        except Exception:
            if attempt == MAX_RETRIES - 1:
                raise

            logger.warning(
                "LLM request failed on attempt %d/%d; retrying.",
                attempt + 1,
                MAX_RETRIES,
                exc_info=True,
            )
