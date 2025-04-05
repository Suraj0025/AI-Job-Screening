import spacy
import re
import warnings
from pdfminer.high_level import extract_text

# Suppress pdfminer warnings
warnings.filterwarnings("ignore", category=UserWarning, module='pdfminer')

# Load a spaCy model with word vectors
try:
    nlp = spacy.load("en_core_web_md")
except:
    print("Downloading 'en_core_web_md' model. Please run: python -m spacy download en_core_web_md")
    exit()

# Skill keywords
skill_keywords = [
    "Python", "Java", "C++", "SQL", "Machine Learning", "Deep Learning",
    "Data Analysis", "Data Visualization", "Communication", "Teamwork",
    "Problem Solving", "Leadership", "Cloud Computing", "AWS", "Excel"
]

def extract_text_from_pdf(pdf_path):
    """Extract raw text from a PDF file"""
    return extract_text(pdf_path)

def extract_name(text):
    """Extract the first PERSON entity as the name"""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return "Name not found"

def extract_emails(text):
    """Find all email addresses in the text"""
    return re.findall(r"[\w\.-]+@[\w\.-]+", text)

def extract_phone_numbers(text):
    """Find all phone numbers (basic pattern)"""
    return re.findall(r"\+?\d[\d\s\-()]{7,}\d", text)

def extract_skills(text, skill_keywords):
    """Extract skills using exact keyword matching (case-insensitive)"""
    found_skills = []
    for skill in skill_keywords:
        pattern = re.compile(rf"\b{re.escape(skill)}\b", re.IGNORECASE)
        if pattern.search(text) and skill not in found_skills:
            found_skills.append(skill)
    return found_skills

def match_resume_to_job(text, job_skills, threshold=0.75):
    """Match resume to a job role using semantic similarity"""
    doc = nlp(text)
    matched_skills = []
    unmatched_skills = []

    for job_skill in job_skills:
        skill_found = False
        job_skill_doc = nlp(job_skill.lower())
        for token in doc:
            similarity = job_skill_doc.similarity(token)
            if similarity > threshold:
                matched_skills.append(job_skill)
                skill_found = True
                break
        if not skill_found:
            unmatched_skills.append(job_skill)

    match_score = len(matched_skills) / len(job_skills) if job_skills else 0
    return matched_skills, unmatched_skills, round(match_score * 100, 2)

# Run the parser
if __name__ == "__main__":
    pdf_path = r"C:\Users\Suraj\Downloads\John Doe.pdf"  # Update path if needed
    text = extract_text_from_pdf(pdf_path)

    name = extract_name(text)
    email = extract_emails(text)
    phone = extract_phone_numbers(text)
    skills = extract_skills(text, skill_keywords)

    # Define job role requirements
    job_role_skills = ["Python", "SQL", "Data Analysis", "Machine Learning", "Communication"]
    matched, missing, score = match_resume_to_job(text, job_role_skills)

    print("\n--- Resume Parsing Result ---")
    print(f"Name: {name}")
    print(f"Email(s): {email}")
    print(f"Phone Number(s): {phone}")
    print(f"Skills Found: {skills}")

    print("\n--- Job Role Match ---")
    print("Target Role: Data Analyst")
    print("Matched Skills:", matched)
    print("Missing Skills:", missing)
    print("Match Score:", f"{score}%")

import warnings
warnings.filterwarnings("ignore", message=r"\[W008\]", category=UserWarning)
