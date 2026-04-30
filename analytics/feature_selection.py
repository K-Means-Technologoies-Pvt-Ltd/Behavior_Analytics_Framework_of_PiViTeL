import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_feature_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

os.makedirs("outputs/analytics/feature_selection", exist_ok=True)

# ---------------------------------------------------
# STEP 1: FIX BOOLEAN VALUES
# ---------------------------------------------------

df = df.replace({True: 1, False: 0})

# ---------------------------------------------------
# STEP 2: CREATE TARGET VARIABLE
# ---------------------------------------------------

df["risk_score"] = (
    0.3 * df["overspeed"] +
    0.3 * df["sudden_braking"] +
    0.2 * df["sudden_acceleration"] +
    0.2 * df["close_object_risk"]
)

df["high_risk_event"] = (df["risk_score"] > 0.3).astype(int)

# ---------------------------------------------------
# STEP 3: SELECT NUMERIC FEATURES
# ---------------------------------------------------

df_numeric = df.select_dtypes(include=["number"]).fillna(0)

# ---------------------------------------------------
# STEP 4: CORRELATION MATRIX
# ---------------------------------------------------

corr_matrix = df_numeric.corr()

# ---------------------------------------------------
# STEP 5: CORRELATION WITH TARGET
# ---------------------------------------------------

target_corr = corr_matrix["high_risk_event"].drop("high_risk_event")

target_corr = target_corr.sort_values(ascending=False)

print("\nCorrelation with Target:\n", target_corr)

target_corr.to_csv("outputs/analytics/feature_selection/target_correlation.csv")

# ---------------------------------------------------
# STEP 6: SELECT IMPORTANT FEATURES (THRESHOLD BASED)
# ---------------------------------------------------

# Keep features with correlation > 0.1 (tunable)
selected_features = target_corr[abs(target_corr) > 0.1].index.tolist()

print("\nSelected Features (based on correlation):")
print(selected_features)

# ---------------------------------------------------
# STEP 7: REMOVE MULTICOLLINEAR FEATURES
# ---------------------------------------------------

# Remove features highly correlated with each other (>0.8)
corr_features = df_numeric[selected_features].corr().abs()

upper = corr_features.where(np.triu(np.ones(corr_features.shape), k=1).astype(bool))

to_drop = [column for column in upper.columns if any(upper[column] > 0.8)]

final_features = [f for f in selected_features if f not in to_drop]

print("\nRemoved (Highly Correlated Features):", to_drop)
print("\nFinal Selected Features:", final_features)

# ---------------------------------------------------
# STEP 8: SAVE FINAL FEATURE LIST
# ---------------------------------------------------

pd.DataFrame(final_features, columns=["Selected_Features"]) \
    .to_csv("outputs/analytics/feature_selection/final_features.csv", index=False)

# ---------------------------------------------------
# STEP 9: CREATE FINAL MODEL DATASET
# ---------------------------------------------------

X = df_numeric[final_features]
y = df_numeric["high_risk_event"]

final_df = pd.concat([X, y], axis=1)

final_df.to_csv("data/processed/pivitel_model_dataset.csv", index=False)

print("\nFinal model dataset saved!")

# ---------------------------------------------------
# DONE
# ---------------------------------------------------

print("\nFeature selection completed successfully!")