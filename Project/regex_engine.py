import re
import random
import pandas as pd
from typing import Tuple, Dict

# Add PII_PATTERNS dictionary for import compatibility
PII_PATTERNS: Dict[str, str] = {
    "email": "",
    "phone": "",
    "pan": "",
    "aadhaar": ""
}

def mask_deterministic(df: pd.DataFrame) -> Tuple[pd.DataFrame, Dict[str, int]]:
    """
    Master function to mask direct PII in all columns of a DataFrame.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Tuple of (masked_df, total_counts)
    """
    # 1. Clean float artifacts
    df = df.astype(str).replace(r'\.0$', '', regex=True)
    masked_df = df.copy()
    
    # 2. Dynamic unique randomizers
    symbols = ['*', '#', 'X', 'Y', '@', '$']
    random.shuffle(symbols)
    phone_sym = symbols.pop()
    aadhaar_sym = symbols.pop()
    email_sym = symbols.pop()
    pan_sym = symbols.pop()
    
    total_counts = {
        "email": 0,
        "phone": 0,
        "pan": 0,
        "aadhaar": 0
    }
    
    # Helper function to count matches column-wise
    def count_and_mask_col(series, pattern, replacement):
        # Count matches
        count = series.str.contains(pattern, regex=True, na=False).sum()
        # Apply mask
        masked_series = series.str.replace(pattern, replacement, regex=True)
        return masked_series, count
    
    # 3. Structural Masking via Regex Capture Groups - apply column-wise
    # Phone Numbers
    phone_pattern = r'(\b[6-9]\d{7})(\d{2}\b)'
    phone_replacement = (phone_sym * 8) + r'\2'
    for col in masked_df.columns:
        masked_df[col], col_count = count_and_mask_col(masked_df[col], phone_pattern, phone_replacement)
        total_counts["phone"] += col_count
    
    # Aadhaar Cards
    # First count matches across all columns
    aadhaar_pattern = r'(?<!\d)(\d{2})(?:\d{2}[\s\-]*\d{4}[\s\-]*\d{2})(\d{2})(?!\d)'
    for col in masked_df.columns:
        total_counts["aadhaar"] += masked_df[col].str.contains(aadhaar_pattern, regex=True, na=False).sum()
    # Then apply mask
    masked_df = masked_df.replace(
        to_replace=aadhaar_pattern,
        value=r'\g<1>' + (aadhaar_sym * 8) + r'\g<2>',
        regex=True
    )
    
    # PAN Cards
    pan_pattern = r'(\b[A-Z])([A-Z]{4}\d{4})([A-Z]\b)'
    pan_replacement = r'\1' + (pan_sym * 8) + r'\3'
    for col in masked_df.columns:
        masked_df[col], col_count = count_and_mask_col(masked_df[col], pan_pattern, pan_replacement)
        total_counts["pan"] += col_count
    
    # Emails
    email_pattern = r'(\b[a-zA-Z0-9._%+-]+)(@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b)'
    email_replacement = (email_sym * 4) + r'\2'
    for col in masked_df.columns:
        masked_df[col], col_count = count_and_mask_col(masked_df[col], email_pattern, email_replacement)
        total_counts["email"] += col_count
    
    return masked_df, total_counts
