
import pandas as pd
from regex_engine import mask_deterministic

print("Testing final Aadhaar masking fix...")

df = pd.DataFrame({
    "test": ["1234 5678 9012", "9876-5432-1098", "111122223333", "No PII here", "12a34-5678-9012"]
})

print("\nOriginal:")
print(df)

masked_df, counts = mask_deterministic(df)
print("\nMasked:")
print(masked_df)
print("\nCounts:", counts)
