import json
import os
from difflib import get_close_matches

# Load the FAQ data once
FAQ_FILE = "data/airline_faq.json"

try:
    with open(FAQ_FILE, "r", encoding="utf-8") as f:
        FAQ_DATA = json.load(f)
except Exception as e:
    FAQ_DATA = []
    print(f"❌ Error loading FAQ data: {e}")

def retrieve_faq_answer(query: str) -> dict:
    """
    Simple keyword-based FAQ retriever using fuzzy matching.
    Returns a dictionary with an 'answer' field.
    """
    if not FAQ_DATA:
        return {"answer": "FAQ data is not available right now."}

    questions = [item["question"] for item in FAQ_DATA]
    matches = get_close_matches(query.lower(), questions, n=1, cutoff=0.5)

    if matches:
        matched_question = matches[0]
        for item in FAQ_DATA:
            if item["question"].lower() == matched_question.lower():
                return {"answer": item["answer"]}

    return {"answer": "Sorry, I couldn't find a relevant answer. Please try rephrasing your question."}
