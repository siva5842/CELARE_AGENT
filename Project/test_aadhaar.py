
import pandas as pd
from regex_engine import mask_deterministic

print("Testing Aadhaar masking with separators...")

# Test dataframe with various Aadhaar formats
df = pd.DataFrame({
    "id": [1, 2, 3],
    "aadhaar": ["1234 5678 9012", "9876-5432-1098", "111122223333"]  # Spaces, hyphens, no separators
})

print("\nOriginal DataFrame:")
print(df)

masked_df, counts = mask_deterministic(df)

print("\nMasked DataFrame:")
print(masked_df)
