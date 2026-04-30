import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_feature_dataset.csv"
df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

# Create output folder
os.makedirs("outputs/analytics/correlation", exist_ok=True)

# ---------------------------------------------------
# STEP 1: FIX BOOLEAN VALUES (VERY IMPORTANT)
# ---------------------------------------------------

# Convert all True/False → 1/0
df = df.replace({True: 1, False: 0})

# ---------------------------------------------------
# STEP 2: CREATE TARGET VARIABLE (CORRECTLY)
# ---------------------------------------------------

# Safety check (ensure columns exist)
required_cols = ["overspeed", "sudden_braking", "sudden_acceleration", "close_object_risk"]

for col in required_cols:
    if col not in df.columns:
        raise ValueError(f"Missing column: {col}")

# Create risk score
df["risk_score"] = (
    0.3 * df["overspeed"] +
    0.3 * df["sudden_braking"] +
    0.2 * df["sudden_acceleration"] +
    0.2 * df["close_object_risk"]
)

# Create target (0/1, NOT True/False)
df["high_risk_event"] = (df["risk_score"] > 0.5).astype(int)

print("\nTarget Distribution:\n", df["high_risk_event"].value_counts())

# ---------------------------------------------------
# STEP 3: FIX TIME FEATURES (IF MISSING)
# ---------------------------------------------------

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

    if "hour_of_day" not in df.columns:
        df["hour_of_day"] = df["timestamp"].dt.hour

    if "night_driving" not in df.columns:
        df["night_driving"] = (
            (df["hour_of_day"] >= 20) | (df["hour_of_day"] <= 6)
        ).astype(int)

# ---------------------------------------------------
# STEP 4: SELECT NUMERIC FEATURES ONLY
# ---------------------------------------------------

df_numeric = df.select_dtypes(include=["number"])

# Drop columns with all NaN
df_numeric = df_numeric.dropna(axis=1, how="all")

# Fill remaining NaN
df_numeric = df_numeric.fillna(0)

# ---------------------------------------------------
# STEP 5: CORRELATION MATRIX
# ---------------------------------------------------

corr_matrix = df_numeric.corr()

print("\nCorrelation Matrix Created")

# Save full matrix
corr_matrix.to_csv("outputs/analytics/correlation/correlation_matrix.csv")

# ---------------------------------------------------
# STEP 6: HEATMAP
# ---------------------------------------------------

plt.figure(figsize=(14, 10))
sns.heatmap(corr_matrix, cmap="coolwarm")

plt.title("Correlation Matrix of Driving Variables")

plt.savefig(
    "outputs/analytics/correlation/correlation_heatmap.png",
    dpi=150,
    bbox_inches="tight"
)
plt.close()

# ---------------------------------------------------
# STEP 7: TARGET CORRELATION (IMPORTANT OUTPUT)
# ---------------------------------------------------

target_corr = corr_matrix["high_risk_event"].sort_values(ascending=False)

print("\nCorrelation with High Risk Event:\n")
print(target_corr)

target_corr.to_csv("outputs/analytics/correlation/target_correlation.csv")

# ---------------------------------------------------
# STEP 8: TOP FEATURE RELATIONSHIPS
# ---------------------------------------------------

corr_pairs = corr_matrix.abs().unstack()

# Remove self correlation
corr_pairs = corr_pairs[corr_pairs < 1]

# Sort
corr_pairs = corr_pairs.sort_values(ascending=False)

top_corr = corr_pairs.head(20)

print("\nTop Correlations:\n")
print(top_corr)

top_corr.to_csv("outputs/analytics/correlation/top_correlations.csv")

# ---------------------------------------------------
# DONE
# ---------------------------------------------------

print("\nCorrelation analysis completed successfully!")