from fastapi import FastAPI, Request, HTTPException
import asyncio
from solver.quiz_solver import solve_quiz
from config import STUDENT_SECRET

app = FastAPI(title="Quiz Solver")

@app.get("/")
def root():
    return {"message": "Quiz Solver API is running!"}

@app.post("/solve")
async def solve(request: Request):
    try:
        data = await request.json()
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    secret = data.get("secret")
    if secret != STUDENT_SECRET:
        raise HTTPException(status_code=403, detail="Invalid secret")

    email = data.get("email")
    url = data.get("url")

    if not (email and url):
        raise HTTPException(status_code=400, detail="Missing email or url")

    asyncio.create_task(solve_quiz(email, url))
    return {"status": "accepted", "email": email, "url": url}
