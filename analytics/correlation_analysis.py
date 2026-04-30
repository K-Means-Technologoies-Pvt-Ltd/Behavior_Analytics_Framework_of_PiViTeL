# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import seaborn as sns
# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_feature_dataset.csv"

print("Loading dataset...\n")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)

# Create output folder
os.makedirs("outputs/analytics/correlation", exist_ok=True)


# ---------------------------------------------------
# STEP 1: HANDLE BOOLEAN VALUES (IMPORTANT FOR YOUR DATASET)
# ---------------------------------------------------

# Convert TRUE/FALSE to 1/0
df = df.replace({True: 1, False: 0})




# ---------------------------------------------------
# STEP 1.5: FIX TIME FEATURES (IMPORTANT)
# ---------------------------------------------------

# Clean column names (prevents hidden bugs)
df.columns = df.columns.str.strip().str.lower()

# Convert time column properly
if "wall_time_iso" in df.columns:
    df["wall_time_iso"] = pd.to_datetime(df["wall_time_iso"], errors="coerce")
    df["hour_of_day"] = df["wall_time_iso"].dt.hour

elif "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    df["hour_of_day"] = df["timestamp"].dt.hour

# Create night_driving safely
if "hour_of_day" in df.columns:
    df["night_driving"] = df["hour_of_day"].apply(
        lambda x: 1 if pd.notnull(x) and (x < 6 or x >= 18) else 0
    )

# ---------------------------------------------------
# STEP 2: SELECT ONLY RELEVANT NUMERIC FEATURES
# ---------------------------------------------------

features = [
    "gps_speed_kmh",
    "distance_m",
    "imu_accel_magnitude",
    "speed_diff",
    "acceleration_change",
    "trip_distance",
    "overspeed",
    "sudden_acceleration",
    "sudden_braking",
    "high_acceleration",
    "close_object_risk",
    "hour_of_day",
    "night_driving"
]

# Keep only available columns (safe check)
features = [col for col in features if col in df.columns]

df_corr = df[features]

# ---------------------------------------------------
# STEP 3: COMPUTE CORRELATION MATRIX
# ---------------------------------------------------

corr_matrix = df_corr.corr()

print("\nCorrelation Matrix:\n")
print(corr_matrix)

# Save correlation table
corr_matrix.to_csv("outputs/analytics/correlation/correlation_matrix.csv")

# ---------------------------------------------------
# STEP 4: HEATMAP (MAIN OUTPUT)
# ---------------------------------------------------

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Matrix of Driving Variables")

plt.savefig("outputs/analytics/correlation/correlation_heatmap.png", dpi=150, bbox_inches='tight')
plt.close()

# ---------------------------------------------------
# STEP 5: CORRELATION WITH TARGET (IMPORTANT)
# ---------------------------------------------------

if "high_risk_event" in df.columns:
    
    target_corr = df_corr.join(df["high_risk_event"]).corr()["high_risk_event"].sort_values(ascending=False)
    
    print("\nCorrelation with High Risk Event:\n")
    print(target_corr)
    
    target_corr.to_csv("outputs/analytics/correlation/target_correlation.csv")

# ---------------------------------------------------
# STEP 6: TOP STRONG RELATIONSHIPS
# ---------------------------------------------------

strong_corr = corr_matrix.abs().unstack()

# remove self-correlation
strong_corr = strong_corr[strong_corr < 1]

strong_corr = strong_corr.sort_values(ascending=False)

print("\nTop Strong Correlations:\n")
print(strong_corr.head(10))

strong_corr.head(20).to_csv("outputs/analytics/correlation/top_correlations.csv")

print("\nCorrelation analysis completed!")