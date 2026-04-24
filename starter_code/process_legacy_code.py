import ast

# ==========================================
# ROLE 2: ETL/ELT BUILDER
# ==========================================
# Task: Extract docstrings and comments from legacy Python code.

import ast
import re

def extract_logic_from_code(file_path):
    # --- FILE READING (Handled for students) ---
    with open(file_path, 'r', encoding='utf-8') as f:
        source_code = f.read()
    # ------------------------------------------
    
    tree = ast.parse(source_code)
    docstrings = {}
    
    # Extract module docstring
    module_doc = ast.get_docstring(tree)
    if module_doc:
        docstrings["module"] = module_doc
    
    # Extract function docstrings
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            doc = ast.get_docstring(node)
            if doc:
                docstrings[node.name] = doc

    # Find business rules in comments
    business_rules = re.findall(r'#.*Business Logic Rule.*|#.*Rule.*', source_code, re.IGNORECASE)
    
    # Detect discrepancies (Role 3 task hint)
    discrepancies = []
    if "tax_rate = 0.10" in source_code and "8%" in source_code:
        discrepancies.append("Potential tax rate discrepancy: code says 0.10 but comment mentions 8%")

    content = "Legacy Business Logic:\n"
    for name, doc in docstrings.items():
        content += f"--- {name} ---\n{doc}\n"
        
    return {
        "document_id": "code-001",
        "content": content,
        "source_type": "Code",
        "author": "Senior Dev (Retired)",
        "source_metadata": {
            "functions": list(docstrings.keys()),
            "business_rules": business_rules,
            "discrepancies": discrepancies
        }
    }

