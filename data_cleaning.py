import pandas as pd

# Load dataset
df = pd.read_csv("/content/whc-sites-2019.csv")
fields = df,columns
print(fields)

missing_values = df.isnull().sum()
print(missing_values[missing_values > 0])

# Fix missing values properly
df = df.copy()  # Ensure we're working on a separate copy of the DataFrame
df["date_end"] = df["date_end"].fillna(0).astype(int)  # Replace NULL with 0 and convert to int
df["danger_list"] = df["danger_list"].fillna("Not in Danger")  # Replace NULL with 'Not in Danger'
df["area_hectares"] = df["area_hectares"].fillna(df["area_hectares"].median())  # Replace NULL with median
df["iso_code"] = df["iso_code"].fillna("Unknown")  # Replace NULL with 'Unknown'
df["udnp_code"] = df["udnp_code"].fillna("Unknown")  # Replace NULL with 'Unknown'

# Save cleaned dataset
df.to_csv("cleaned_heritage_sites.csv", index=False)

print("Data cleaning complete! 🎉 Check 'cleaned_heritage_sites.csv'.")
