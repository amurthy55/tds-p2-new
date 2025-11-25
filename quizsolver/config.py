import os

STUDENT_EMAIL = "25ds2000003@ds.study.iitm.ac.in"
STUDENT_SECRET = "0ct0b3r"

# Choose which LLM to use
USE_AIPIPE = True

AIPIPE_API_KEY = os.getenv("AIPIPE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")