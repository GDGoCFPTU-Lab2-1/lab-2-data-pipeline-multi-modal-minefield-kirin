import pandas as pd

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Process sales records, handling type traps and duplicates.

def process_sales_csv(file_path):
    # --- FILE READING (Handled for students) ---
    df = pd.read_csv(file_path)
    # ------------------------------------------
    
    # Remove duplicate rows based on 'id'
    df = df.drop_duplicates(subset=['id'], keep='first')
    
    def clean_price(price):
        if pd.isna(price) or str(price).lower() in ['n/a', 'liên hệ', 'null']:
            return 0.0
        
        price_str = str(price).replace('$', '').replace(',', '').strip().lower()
        
        if price_str == 'five dollars':
            return 5.0
        
        try:
            val = float(price_str)
            return abs(val) # Handle negative prices if any (like -350000)
        except ValueError:
            return 0.0

    def normalize_date(date_str):
        if pd.isna(date_str):
            return None
        try:
            # Try multiple formats
            for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%Y/%m/%d", "%d-%m-%Y", "%d %b %Y", "%B %dth %Y", "%B %dst %Y", "%B %dnd %Y", "%B %drd %Y"]:
                try:
                    # Handle "th", "st", "nd", "rd" in dates like "January 16th 2026"
                    clean_date_str = re.sub(r'(\d+)(st|nd|rd|th)', r'\1', str(date_str))
                    return pd.to_datetime(clean_date_str, format=fmt, errors='raise').strftime("%Y-%m-%d")
                except:
                    continue
            # Fallback to pandas automatic parsing
            return pd.to_datetime(date_str).strftime("%Y-%m-%d")
        except:
            return None

    import re
    
    results = []
    for _, row in df.iterrows():
        clean_p = clean_price(row['price'])
        norm_date = normalize_date(row['date_of_sale'])
        
        content = f"Product: {row['product_name']}, Category: {row['category']}, Price: {clean_p} {row['currency']}"
        
        results.append({
            "document_id": f"csv-{row['id']}",
            "content": content,
            "source_type": "CSV",
            "author": f"Seller {row['seller_id']}",
            "timestamp": norm_date,
            "source_metadata": {
                "product_name": row['product_name'],
                "category": row['category'],
                "price": clean_p,
                "currency": row['currency'],
                "stock": row['stock_quantity']
            }
        })
    
    return results

