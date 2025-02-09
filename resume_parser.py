# resume_parser.py
import io
from pdfminer.high_level import extract_text
import docx

def parse_resume(file):
    """
    Extracts text content from a resume file. Supports PDF and DOCX formats.
    Returns a dictionary with the full text extracted.
    """
    resume_data = {}
    file_type = file.name.split('.')[-1].lower()
    
    if file_type == 'pdf':
        try:
            # The file is a BytesIO object; extract text using pdfminer
            text = extract_text(file)
        except Exception as e:
            text = f"Error extracting PDF text: {str(e)}"
        resume_data["full_text"] = text
        
    elif file_type == 'docx':
        try:
            # Use python-docx to read DOCX files
            doc = docx.Document(file)
            full_text = [para.text for para in doc.paragraphs]
            text = "\n".join(full_text)
        except Exception as e:
            text = f"Error extracting DOCX text: {str(e)}"
        resume_data["full_text"] = text
        
    else:
        resume_data["full_text"] = "Unsupported file type."
    
    # (Optional) Here you can add further processing to extract key skills or projects.
    return resume_data
