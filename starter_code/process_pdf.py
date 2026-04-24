import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

def extract_pdf_data(file_path):
    # --- FILE CHECK (Handled for students) ---
    if not os.path.exists(file_path):
        print(f"Error: File not found at {file_path}")
        return None
    # ------------------------------------------

    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-3-flash-preview')

    try:
        # Upload the file
        pdf_file = genai.upload_file(path=file_path)
        
        # Prompt for extraction
        prompt = """
        Extract the following information from this PDF:
        - Title
        - Author
        - A 3-sentence summary
        
        Return the result in JSON format with keys: 'title', 'author', 'summary'.
        """
        
        response = model.generate_content([pdf_file, prompt])
        
        # Clean the response to parse JSON
        json_text = response.text.replace('```json', '').replace('```', '').strip()
        data = json.loads(json_text)
        
        return {
            "document_id": "pdf-001",
            "content": data.get("summary", ""),
            "source_type": "PDF",
            "author": data.get("author", "Unknown"),
            "source_metadata": {
                "title": data.get("title", ""),
                "original_filename": os.path.basename(file_path)
            }
        }
    except Exception as e:
        print(f"Error processing PDF: {e}")
        return None

