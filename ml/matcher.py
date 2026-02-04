from ml.skill_extractor import extract_skills


def match_resume_to_job(resume_text, job_text):
    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_text))

    if not job_skills:
        return {
            "score": 0,
            "matched_skills": [],
            "missing_skills": []
        }

    matched = resume_skills.intersection(job_skills)
    missing = job_skills - resume_skills

    score = round((len(matched) / len(job_skills)) * 100, 2)

    return {
        "score": score,
        "matched_skills": sorted(matched),
        "missing_skills": sorted(missing)
    }


if __name__ == "__main__":
    resume_text = """
    Python developer with experience in Machine Learning, SQL,
    Data Analysis, and Power BI.
    """

    job_description = """
    Looking for a Python developer with experience in
    Machine Learning, SQL, NLP, and FastAPI.
    """

    result = match_resume_to_job(resume_text, job_description)

    print("MATCH SCORE:", result["score"], "%")
    print("MATCHED SKILLS:", result["matched_skills"])
    print("MISSING SKILLS:", result["missing_skills"])
