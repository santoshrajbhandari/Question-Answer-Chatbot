from app.huggingface_api import query_huggingface

DEFAULT_CONTEXT = """
Hugging Face is a company that provides open-source tools for natural language processing tasks.
"""

def answer_question(question: str, context: str = DEFAULT_CONTEXT) -> str:
    return query_huggingface(question, context)
