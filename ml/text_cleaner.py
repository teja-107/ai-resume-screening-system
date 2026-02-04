import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", " ", text)
    doc = nlp(text)

    cleaned_words = [
        token.lemma_
        for token in doc
        if not token.is_stop and token.is_alpha
    ]

    return " ".join(cleaned_words)

if __name__ == "__main__":
    sample_text = """
    Experienced Python Developer with 3+ years of experience in
    Machine Learning, SQL, and Data Analysis.
    """

    cleaned = clean_text(sample_text)
    print("CLEANED TEXT:")
    print(cleaned)
