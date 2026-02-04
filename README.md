AI-Powered Resume Screening & Job Matching System

Problem Statement
Recruiters often need to manually screen hundreds of resumes for a single job opening. This process is time-consuming, inconsistent, and prone to human bias.  
This project automates the initial resume screening process by matching resumes with job descriptions using NLP and AI-based similarity scoring.

Project Overview
This system evaluates how well a candidate’s resume matches a given job description by:
- Cleaning and preprocessing text using NLP
- Extracting technical skills from resumes and job descriptions
- Calculating a rule-based skill match score
- Calculating an AI-based semantic similarity score
- Combining both scores into a final ATS-style score
- Exposing the system via a REST API using FastAPI

What the System Does
- Accepts resume text and job description text as input
- Performs NLP preprocessing (lowercasing, stopword removal, lemmatization)
- Extracts relevant technical skills
- Computes:
  - Skill match score  
  - AI similarity score  
  - Final ATS score
- Returns matched skills and missing skills in structured JSON format

High-Level Workflow
1. Resume text is cleaned using NLP preprocessing.
2. Skills are extracted using a curated skills database.
3. A rule-based skill overlap score is calculated.
4. An AI-based similarity score is calculated using TF-IDF and cosine similarity.
5. Both scores are combined using weighted logic.
6. Results are returned through a REST API.

Tech Stack
- Python  
- spaCy – NLP preprocessing  
- scikit-learn – TF-IDF vectorization & cosine similarity  
- FastAPI – REST API framework  
- Uvicorn – ASGI server  

Key Learnings
- NLP text preprocessing and normalization
- Skill extraction from unstructured text
- Rule-based vs AI-based matching approaches
- Semantic similarity using TF-IDF and cosine similarity
- Building and exposing ML logic using FastAPI
- Designing explainable AI systems

Future Improvements
- Resume file upload (PDF/DOC) via API
- Database integration for storing results
- Weight tuning for scoring logic
- Frontend interface for recruiters
- Cloud deployment (AWS / Render)



