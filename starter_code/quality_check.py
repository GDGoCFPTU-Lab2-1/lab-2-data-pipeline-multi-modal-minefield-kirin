# ==========================================
# ROLE 3: OBSERVABILITY & QA ENGINEER
# ==========================================
# Task: Implement quality gates to reject corrupt data or logic discrepancies.

def run_quality_gate(document_dict):
    content = document_dict.get('content', '')
    
    # Reject documents with 'content' length < 20 characters
    if len(content) < 20:
        print(f"Quality Gate Fail: Content too short for {document_dict.get('document_id')}")
        return False
        
    # Reject documents containing toxic/error strings
    toxic_strings = ['Null pointer exception', 'Segmentation fault', 'Access denied']
    for ts in toxic_strings:
        if ts.lower() in content.lower():
            print(f"Quality Gate Fail: Toxic/Error string found in {document_dict.get('document_id')}")
            return False
            
    # Flag discrepancies (check metadata)
    meta = document_dict.get('source_metadata', {})
    if 'discrepancies' in meta and meta['discrepancies']:
        print(f"Quality Gate Warning: Discrepancy found in {document_dict.get('document_id')}: {meta['discrepancies']}")
        # We might still allow it but with a flag, or reject it. 
        # For this lab, let's allow it but log it.
    
    return True
