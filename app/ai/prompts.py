RESUME_ANALYSIS_PROMPT = """
You are an AI recruitment assistant.

Analyze the following resume.

Return ONLY valid JSON.

Extract:

- full_name
- email
- phone
- skills
- experience
- education
- certifications
- languages
- projects
- summary

Resume:

{text}
"""


JOB_MATCH_PROMPT = """
You are an AI hiring assistant.

Compare the candidate resume with the job description.

Return JSON only.

Fields:

match_score

strengths

weaknesses

missing_skills

reason

Resume:

{resume}

Job:

{job}
"""