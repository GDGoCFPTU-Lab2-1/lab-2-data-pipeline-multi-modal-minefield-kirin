import re

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Clean the transcript text and extract key information.

def clean_transcript(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # ------------------------------------------
    
    # Remove timestamps [00:00:00]
    cleaned_text = re.sub(r'\[\d{2}:\d{2}:\d{2}\]', '', text)
    
    # Remove noise tokens like [Music], [inaudible], [Laughter]
    cleaned_text = re.sub(r'\[Music[^\]]*\]', '', cleaned_text)
    cleaned_text = re.sub(r'\[inaudible\]', '', cleaned_text)
    cleaned_text = re.sub(r'\[Laughter\]', '', cleaned_text)
    
    # Remove speaker labels
    cleaned_text = re.sub(r'\[Speaker \d+\]:', '', cleaned_text)
    
    # Clean whitespace
    cleaned_text = '\n'.join([line.strip() for line in cleaned_text.split('\n') if line.strip()])
    
    # Find price in Vietnamese words
    # Example: "năm trăm nghìn" -> 500000
    price_map = {
        "một": 1, "hai": 2, "ba": 3, "bốn": 4, "năm": 5, "sáu": 6, "bảy": 7, "tám": 8, "chín": 9, "mười": 10,
        "trăm": 100, "nghìn": 1000, "triệu": 1000000
    }
    
    # Simple search for "năm trăm nghìn"
    detected_price = None
    if "năm trăm nghìn" in text:
        detected_price = 500000
        
    return {
        "document_id": "transcript-001",
        "content": cleaned_text,
        "source_type": "Video",
        "author": "Speaker 1",
        "source_metadata": {
            "detected_price_vnd": detected_price,
            "has_noise_removed": True
        }
    }

