#Ibrahimr

#Join the cleaned Video Game Sales dataset with a generated platform _info dataset.


import pandas as pd

# Load main (clean) dataset
vgsales = pd.read_csv("../data/clean/vgsales_clean.csv")

# Load secondary dataset (generated lookup table)
platform_meta = pd.read_csv("../data/raw/Platform_info_data.csv")


# Merge on common key
merged = pd.merge(
    vgsales,
    platform_meta,
    how="left",
    on="Platform"
)

# Save merged dataset
merged.to_csv("../data/clean/vgsales_merged.csv", index=False)

print("Saved merged dataset to: data/clean/vgsales_merged.csv")
print("Merged shape:", merged.shape)
print("NA counts in new columns:")
print(merged[["Manufacturer", "ConsoleType", "ReleaseYear", "Generation"]].isna().sum())

