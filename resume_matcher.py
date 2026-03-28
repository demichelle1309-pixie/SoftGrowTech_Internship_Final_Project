import re
from sklearn.feature_extraction.text import TfidfVectorizer, ENGLISH_STOP_WORDS
from sklearn.metrics.pairwise import cosine_similarity

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text

print("AI Resume Screening System")
print("---------------------------")

resume = clean_text(input("Paste Resume Text:\n"))
job_desc = clean_text(input("\nPaste Job Description:\n"))

vectorizer = TfidfVectorizer(stop_words='english')
vectors = vectorizer.fit_transform([resume, job_desc])

similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]

resume_words = set(resume.split()) - ENGLISH_STOP_WORDS
job_words = set(job_desc.split()) - ENGLISH_STOP_WORDS
common_words = resume_words.intersection(job_words)

print("\nMatch Score: {:.2f}%".format(similarity * 100))
print("\nMatching Keywords:", common_words)