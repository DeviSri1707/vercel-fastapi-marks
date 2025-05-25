from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()  # <-- This 'app' variable is REQUIRED by Vercel

# Enable CORS so any frontend can call your API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("marks.json") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: List[str] = []):
    return {"marks": [data.get(n, None) for n in name]}
