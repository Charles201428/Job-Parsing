# email_generator.py
import os
from dotenv import load_dotenv
import openai


load_dotenv()


client = openai.OpenAI()

def generate_email(job_details, resume_data):
    """
    Combines job posting details and candidate resume data to generate a personalized,
    concise, and professional cold outreach email using the GPT-4O model.
    
    Returns:
      The generated email as a string, or an error message if something goes wrong.
    """
    prompt = f"""
You are a professional career advisor. Based on the following job posting and candidate's resume details,
please craft a concise, engaging, and professional cold outreach email. Highlight the candidate's relevant skills,
projects, and experiences.

Job Posting:
- Title: {job_details.get('title', 'N/A')}
- Description: {job_details.get('description', 'N/A')}
- Key Points: {job_details.get('key_points', [])}

Candidate Resume:
{resume_data.get('full_text', 'N/A')}

Please generate the email below.
    """
    
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Using GPT-4O instead of GPT-3.5
            messages=[
                {"role": "system", "content": "You are a helpful career advisor."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.7  # A bit higher temperature for creative but relevant content
        )
        # Use dot notation to access the response content
        email_content = completion.choices[0].message.content.strip()
    except Exception as e:
        email_content = f"Error generating email: {str(e)}"
    
    return email_content

