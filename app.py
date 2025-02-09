# app.py
import streamlit as st
from job_scraper import extract_job_details
from resume_parser import parse_resume
from email_generator import generate_email

# Set the page configuration
st.set_page_config(page_title="AI-Powered Cold Outreach Tool", layout="wide")

st.title("AI-Powered Cold Outreach Tool")

# Input: Company Careers Page URL
job_url = st.text_input("Enter the Company Careers Page URL:")

# Input: Resume file uploader (supports PDF and DOCX)
resume_file = st.file_uploader("Upload your resume (PDF or DOCX)", type=["pdf", "docx"])

# Process inputs only when both URL and resume are provided
if job_url and resume_file:
    # Extract job details
    with st.spinner("Extracting job details..."):
        job_details = extract_job_details(job_url)
    st.subheader("Job Details")
    st.write(job_details)
    
    # Parse resume content
    with st.spinner("Parsing resume..."):
        resume_data = parse_resume(resume_file)
    st.subheader("Resume Data")
    st.write(resume_data)
    
    # Generate the outreach email when the button is clicked
    if st.button("Generate Outreach Email"):
        with st.spinner("Generating personalized email..."):
            email_content = generate_email(job_details, resume_data)
        st.subheader("Generated Outreach Email")
        st.write(email_content)
