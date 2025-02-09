# AI-Powered Cold Outreach Tool

This project is a Streamlit web application that uses Generative AI to help generate personalized cold outreach emails for job opportunities. It extracts job details from a provided company careers page URL, parses an uploaded resume, and then uses the OpenAI API (with the GPT-4O model) to generate a tailored email.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Setup](#setup)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Environment Variables](#environment-variables)
- [Notes](#notes)
- [License](#license)

## Features

- **Job Data Extraction:**  
  Fetch and parse the content of a provided job/careers URL.

- **Resume Parsing:**  
  Upload a resume (PDF or DOCX) and extract its text content.

- **Email Generation:**  
  Generate a concise and professional cold outreach email by combining job details and resume information using GPT-4O.

- **User-Friendly Interface:**  
  A simple Streamlit UI that allows you to input a URL, upload a resume, and view the generated email.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/Charles201428/Job-Parsing.git
   cd ai_cold_outreach



2. **Create a Virtual Environment:**

On Windows:
python -m venv env
env\Scripts\activate
pip install -r requirements.txt




On macOS/Linux:
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt