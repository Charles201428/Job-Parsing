# job_scraper.py
import os
import json
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import openai

# Load environment variables from the .env file
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def extract_job_details(url):
    """
    Fetches the webpage at the given URL, extracts its text content,
    and then uses the OpenAI API to extract structured job details.
    
    The OpenAI API is prompted to return a JSON string with the following keys:
    - "title": The job title.
    - "description": A summary of the job description.
    - "key_points": Any additional relevant points extracted from the job posting.
    
    Returns a dictionary with the extracted details or an error message.
    """
    # Step 1: Retrieve webpage content
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        return {"error": f"Error fetching URL: {str(e)}"}
    
    # Step 2: Extract text from the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # For demonstration, extract all text; you might want to narrow this down to a specific section
    text_content = soup.get_text(separator='\n', strip=True)
    
    # Step 3: Create a prompt for the OpenAI API to extract structured job details
    prompt = f"""
You are a professional content analyzer. Given the following webpage text from a company's careers page, 
extract the most relevant job details. Please provide the following information in valid JSON format with these keys:
- "title": The job title.
- "description": A concise summary of the job description.
- "key_points": A bullet-point list (as an array) of any additional key points or requirements mentioned.

Here is the webpage content:
{text_content}
    """
    
    # Step 4: Call the OpenAI API to process the text and return structured job details
    try:
        response_openai = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or another appropriate model
            messages=[
                {"role": "system", "content": "You are a helpful assistant that extracts structured job details from text."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=300,
            temperature=0.2  # Lower temperature for more deterministic output
        )
        # Extract the content from the API response
        api_output = response_openai.choices[0].message['content'].strip()
        
        # Attempt to parse the output as JSON
        job_details = json.loads(api_output)
    except Exception as e:
        return {"error": f"Error processing job details: {str(e)}"}
    
    return job_details

# For testing purposes: Uncomment the following lines to test the function locally
# if __name__ == "__main__":
#     test_url = "https://example.com/job-posting"  # Replace with a valid job URL
#     details = extract_job_details(test_url)
#     print(json.dumps(details, indent=2))
