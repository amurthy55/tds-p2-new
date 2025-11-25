# Quiz Solver (TDS LLM Analysis Project)

A FastAPI-based automated solver for the TDS LLM Analysis Quiz. The server receives POST
requests with a quiz URL and a shared secret, renders the quiz page (including JavaScript),
extracts the task, performs required data processing (CSV/JSON/PDF/visualization), and
submits answers to the quiz submit endpoint — all within the 3‑minute limit.

## Project Structure
- main.py — FastAPI app exposing /solve
- config.py — configuration (email, secret, API keys)
- solver/
  - browser_utils.py — Playwright page fetcher
  - quiz_solver.py — orchestration loop
  - data_utils.py — data processing helpers
  - llm_utils.py — LLM wrappers (AIPipe/OpenAI)
- requirements.txt
- LICENSE

## Setup
```
python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
```

## Run
```
uvicorn main:app --reload --port 8000
```

## Test
```
curl -X POST "http://127.0.0.1:8000/solve"  -H "Content-Type: application/json"  -d '{"email":"you@x","secret":"y","url":"https://tds-llm-analysis.s-anand.net/demo"}'
```

## License
MIT License included in LICENSE file.
