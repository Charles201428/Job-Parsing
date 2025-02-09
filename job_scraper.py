# job_scraper.py
import os
import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()


client = openai.OpenAI()

def extract_job_details(url):
    """
    Fetches the webpage from the given URL, extracts its text content,
    and then uses the OpenAI API (with the new SDK syntax) to extract structured job details.
    
    The assistant is instructed to return a JSON-formatted string with these keys:
      - "title": The job title.
      - "description": A concise summary of the job description.
      - "key_points": A list of any additional key points or requirements.
    
    Returns:
      A dictionary with the extracted details, or an error message.
    """

    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Error fetching URL: {str(e)}"}
    

    soup = BeautifulSoup(response.text, "html.parser")
    # For simplicity, extract all text; in practice, you might target a specific section.
    text_content = soup.get_text(separator="\n", strip=True)
    

    prompt = f"""
You are an expert job posting analyzer. Given the following webpage text extracted from a company's careers page, 
please extract the relevant job details and return the output in valid JSON format with the following keys:

- "title": The job title.
- "description": A concise summary of the job description.
- "key_points": A list of any additional key points or requirements mentioned.

Here is the webpage content:
{text_content}
    """

    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Update this to the appropriate model name if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured job details from text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.2  # Lower temperature for more deterministic output
        )
        # Access the generated content using dot notation
        api_output = completion.choices[0].message.content.strip()
        
        # Attempt to parse the output as JSON
        job_details = json.loads(api_output)
    except Exception as e:
        return {"error": f"Error processing job details: {str(e)}"}
    
    return job_details


