from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def ai_match_score(resume_text, job_text):
    documents = [resume_text, job_text]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2)
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])

    score = round(similarity[0][0] * 100, 2)
    return score


if __name__ == "__main__":
    resume_text = """
    Python developer with experience in machine learning,
    data analysis, SQL, and Power BI.
    """

    job_description = """
    Looking for a machine learning engineer with strong
    Python and SQL skills.
    """

    score = ai_match_score(resume_text, job_description)
    print("AI MATCH SCORE:", score, "%")
