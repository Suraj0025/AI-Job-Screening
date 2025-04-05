# AI-Job-Screening
AI-based job screening system with resume parsing, skill-based scoring, and bias detection

# Resume Parsing and Job Matching System

This project is designed to parse resumes from PDF files, extract key information such as the candidate's name, email, phone number, and skills. It also compares the extracted skills with a predefined set of job skills to calculate how well the resume matches the job requirements.

### Features:
- **PDF Resume Parsing**: Extracts text from PDF resumes using the `pdfminer` library.
- **Name Extraction**: Identifies and extracts the candidate's name from the resume text using `spaCy`.
- **Contact Information Extraction**: Extracts emails and phone numbers from the resume text using regular expressions.
- **Skills Extraction**: Searches for predefined skill keywords in the resume text and returns the found skills.
- **Job Role Matching**: Compares the skills found in the resume with the required job skills and calculates a match score based on semantic similarity using `spaCy`.

### Prerequisites:
Before running this project, make sure you have the following libraries installed:

- `spaCy` for natural language processing and semantic similarity calculations.
- `pdfminer` for extracting text from PDF files.
- `re` (Regular Expressions) for pattern matching in the resume text.

To install the required dependencies, you can use the following commands:

```bash
pip install spacy
pip install pdfminer.six
```

Additionally, you will need to download the `en_core_web_md` model for `spaCy`. You can do this by running:

```bash
python -m spacy download en_core_web_md
```

### How It Works:

1. **PDF Text Extraction**: 
   - The `extract_text_from_pdf` function extracts raw text from a given PDF file using the `pdfminer` library.

2. **Text Processing**:
   - The `extract_name` function uses `spaCy` to identify and extract the first person entity (assumed to be the candidate's name).
   - The `extract_emails` function finds all email addresses in the resume text.
   - The `extract_phone_numbers` function finds phone numbers using a basic pattern.
   - The `extract_skills` function matches predefined skill keywords against the resume text and extracts the skills found.

3. **Job Role Matching**:
   - The `match_resume_to_job` function compares the extracted skills with the job skills for a predefined role (e.g., "Data Analyst") using `spaCy`'s semantic similarity function to calculate a match score.

### Usage:

1. **Prepare a PDF Resume**:
   - Make sure you have a resume in PDF format. Update the path in the `pdf_path` variable to point to your PDF file.

2. **Run the Script**:
   - Run the script by executing the following command:

   ```bash
   python resume_job_matcher.py
   ```

   The script will print out the following details:
   - Extracted candidate information: Name, Email(s), Phone Number(s).
   - Extracted skills.
   - Job role match results: Matched Skills, Missing Skills, and Match Score.

### Example Output:

```
--- Resume Parsing Result ---
Name: John Doe
Email(s): ['johndoe@example.com']
Phone Number(s): ['+1 (555) 123-4567']
Skills Found: ['Python', 'SQL', 'Data Analysis']

--- Job Role Match ---
Target Role: Data Analyst
Matched Skills: ['Python', 'SQL', 'Data Analysis']
Missing Skills: ['Machine Learning', 'Communication']
Match Score: 60.0%
```

### How to Customize:
- **Skill Keywords**: Modify the `skill_keywords` list to include the skills relevant to your use case.
- **Job Role Requirements**: Modify the `job_role_skills` list to specify the skills required for a particular job role.

### License:
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
