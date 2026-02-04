
from ml.text_cleaner import clean_text

# A basic, extensible skills list
SKILLS_DB = [
    "python",
    "java",
    "c",
    "c++",
    "sql",
    "mysql",
    "postgresql",
    "machine learning",
    "deep learning",
    "data analysis",
    "nlp",
    "fastapi",
    "django",
    "flask",
    "pandas",
    "numpy",
    "scikit learn",
    "power bi",
    "excel"
]

def extract_skills(text):
    cleaned = clean_text(text)
    found_skills = set()

    for skill in SKILLS_DB:
        # normalize skill text the same way
        skill_clean = clean_text(skill)
        if skill_clean in cleaned:
            found_skills.add(skill)

    return sorted(found_skills)

if __name__ == "__main__":
    sample_resume_text = """
    Experienced Python Developer with experience in Machine Learning,
    SQL, Data Analysis, and Power BI.
    """

    skills = extract_skills(sample_resume_text)
    print("EXTRACTED SKILLS:")
    print(skills)
