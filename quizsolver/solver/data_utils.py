import re, pandas as pd
from solver.llm_utils import query_llm

async def process_task(html):
    """
    Parse the HTML to detect what the quiz asks.
    Use regex + LLM reasoning to interpret it.
    """
    # Basic extraction example
    submit_url = re.search(r'"(https://[^"]+/submit)"', html)
    submit_url = submit_url.group(1) if submit_url else None

    question_text = re.sub("<[^>]+>", "", html)  # crude HTML cleanup
    answer = query_llm(f"Analyze this quiz text and give the correct numeric answer:\n\n{question_text}")

    return {"answer": answer, "submit_url": submit_url}
