from ml.matcher import match_resume_to_job
from ml.ai_matcher import ai_match_score


def final_ats_score(resume_text, job_text,
                    skill_weight=0.6, ai_weight=0.4):

    skill_result = match_resume_to_job(resume_text, job_text)
    skill_score = skill_result["score"]

    ai_score = ai_match_score(resume_text, job_text)

    final_score = round(
        (skill_score * skill_weight) +
        (ai_score * ai_weight),
        2
    )

    return {
        "final_score": final_score,
        "skill_score": skill_score,
        "ai_score": ai_score,
        "matched_skills": skill_result["matched_skills"],
        "missing_skills": skill_result["missing_skills"]
    }


if __name__ == "__main__":
    resume_text = """
    Python developer with experience in Machine Learning,
    SQL, Data Analysis, and Power BI.
    """

    job_description = """
    Looking for a Machine Learning Engineer with strong
    Python, SQL, NLP, and FastAPI experience.
    """

    result = final_ats_score(resume_text, job_description)

    print("FINAL ATS SCORE:", result["final_score"], "%")
    print("Skill Match Score:", result["skill_score"], "%")
    print("AI Similarity Score:", result["ai_score"], "%")
    print("Matched Skills:", result["matched_skills"])
    print("Missing Skills:", result["missing_skills"])
