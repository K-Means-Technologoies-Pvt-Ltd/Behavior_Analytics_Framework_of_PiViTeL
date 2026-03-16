
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Path to merged dataset
DATA_PATH = "data/processed/pivitel_merged_dataset.csv"

# ---------------------------------------------------
# Step 1: Load Dataset
# ---------------------------------------------------

print("Loading dataset...\n")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)


# ---------------------------------------------------
# Step 2: Inspect Dataset Structure
# ---------------------------------------------------

print("\nDataset Information\n")

print(df.info())


# ---------------------------------------------------
# Step 3: Count Missing Values
# ---------------------------------------------------

print("\nMissing Value Count Per Column\n")

missing_count = df.isnull().sum()

print(missing_count)


# ---------------------------------------------------
# Step 4: Calculate Missing Value Percentage
# ---------------------------------------------------

missing_percent = (df.isnull().sum() / len(df)) * 100

print("\nMissing Percentage Per Column\n")

print(missing_percent)


# ---------------------------------------------------
# Step 5: Create Missing Value Summary Table
# ---------------------------------------------------

missing_summary = pd.DataFrame({
    "Column_Name": df.columns,
    "Missing_Count": df.isnull().sum(),
    "Missing_Percent": missing_percent
})

print("\nMissing Value Summary\n")

print(missing_summary)


# ---------------------------------------------------
# Step 6: Save Missing Value Summary
# ---------------------------------------------------

missing_summary.to_csv("data/processed/missing_value_summary.csv", index=False)

print("\nMissing value summary saved to data/processed/missing_value_summary.csv")


# ---------------------------------------------------
# Step 7: Visualize Missing Value Pattern
# ---------------------------------------------------

plt.figure(figsize=(12,6))

sns.heatmap(df.isnull(), cbar=False)

plt.title("Missing Value Heatmap")

plt.xlabel("Columns")

plt.ylabel("Records")

plt.show()


# ---------------------------------------------------
# Step 8: Categorize Missing Values
# ---------------------------------------------------

print("\nCategorizing Missing Values...\n")

missing_percent = (df.isnull().sum() / len(df)) * 100

# Category 1: Completely Missing Columns
complete_missing = missing_percent[missing_percent == 100].index.tolist()

# Category 2: High Missing (20% - 100%)
high_missing = missing_percent[(missing_percent > 20) & (missing_percent < 100)].index.tolist()

# Category 3: Moderate Missing (5% - 20%)
moderate_missing = missing_percent[(missing_percent > 5) & (missing_percent <= 20)].index.tolist()

# Category 4: Low Missing (0% - 5%)
low_missing = missing_percent[(missing_percent > 0) & (missing_percent <= 5)].index.tolist()


print("Completely Missing Columns:")
print(complete_missing)

print("\nHigh Missing Columns:")
print(high_missing)

print("\nModerate Missing Columns:")
print(moderate_missing)

print("\nLow Missing Columns:")
print(low_missing)


# ---------------------------------------------------
# Step 9: Save Categorized Columns
# ---------------------------------------------------

category_summary = pd.DataFrame({
    "Category": ["Completely Missing", "High Missing", "Moderate Missing", "Low Missing"],
    "Columns": [complete_missing, high_missing, moderate_missing, low_missing]
})

category_summary.to_csv("data/processed/missing_value_categories.csv", index=False)

print("\nMissing value categories saved to data/processed/missing_value_categories.csv")


# ---------------------------------------------------
# Step 10: Final Message
# ---------------------------------------------------

print("\nMissing Value Investigation Completed")
print("Dataset is now ready for Missing Value Treatment stage.")