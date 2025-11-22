import time, json, requests
from solver.browser_utils import fetch_page
from solver.data_utils import process_task
from config import STUDENT_EMAIL, STUDENT_SECRET

async def solve_quiz(email, url):
    start_time = time.time()
    print(f"Starting quiz at {url}")

    while time.time() - start_time < 180:  # 3-minute deadline
        html = await fetch_page(url)
        # html = await fetch_page(url)
        print("Fetched HTML length:", len(html))
        print(html[:1000])  # preview

        task = await process_task(html)

        payload = {
            "email": email,
            "secret": STUDENT_SECRET,
            "url": url,
            "answer": task["answer"]
        }

        res = requests.post(task["submit_url"], json=payload)
        if res.status_code != 200:
            print("Submission failed:", res.text)
            break

        result = res.json()
        print("Result:", result)

        if result.get("correct"):
            next_url = result.get("url")
            if not next_url:
                print("✅ Quiz completed successfully.")
                break
            url = next_url
        else:
            print("❌ Incorrect answer, retrying...")