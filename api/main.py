from fastapi import FastAPI
from pydantic import BaseModel
import sys
import os

# allow api to access ml folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ml.final_matcher import final_ats_score

app = FastAPI(title="AI Resume Screening API")

class MatchRequest(BaseModel):
    resume_text: str
    job_description: str


@app.get("/")
def home():
    return {"message": "ATS API is running"}


@app.post("/match")
def match_resume(request: MatchRequest):
    result = final_ats_score(
        request.resume_text,
        request.job_description
    )
    return result
