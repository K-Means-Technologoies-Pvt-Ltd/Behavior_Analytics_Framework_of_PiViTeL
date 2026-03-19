import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_feature_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded:", df.shape)

os.makedirs("outputs/analytics/bivariate", exist_ok=True)


# ===================================================
# 1. SPEED vs DISTANCE (CORE RELATIONSHIP)
# ===================================================

plt.figure()
plt.scatter(df["gps_speed_kmh"], df["distance_m"], s=10)
plt.title("Speed vs Distance")
plt.xlabel("Speed (km/h)")
plt.ylabel("Distance (m)")
plt.savefig("outputs/analytics/bivariate/speed_vs_distance.png")
plt.close()


# ===================================================
# 2. SPEED vs ACCELERATION
# ===================================================

plt.figure()
plt.scatter(df["gps_speed_kmh"], df["imu_accel_magnitude"], s=10)
plt.title("Speed vs Acceleration")
plt.xlabel("Speed (km/h)")
plt.ylabel("Acceleration")
plt.savefig("outputs/analytics/bivariate/speed_vs_acceleration.png")
plt.close()


# ===================================================
# 3. SPEED vs CLOSE OBJECT RISK
# ===================================================

plt.figure()
sns.boxplot(x=df["close_object_risk"], y=df["gps_speed_kmh"])
plt.title("Speed vs Close Object Risk")
plt.savefig("outputs/analytics/bivariate/speed_vs_close_risk.png")
plt.close()


# ===================================================
# 4. SPEED vs SUDDEN BRAKING
# ===================================================

plt.figure()
sns.boxplot(x=df["sudden_braking"], y=df["gps_speed_kmh"])
plt.title("Speed vs Sudden Braking")
plt.savefig("outputs/analytics/bivariate/speed_vs_braking.png")
plt.close()


# ===================================================
# 5. SPEED vs SUDDEN ACCELERATION
# ===================================================

plt.figure()
sns.boxplot(x=df["sudden_acceleration"], y=df["gps_speed_kmh"])
plt.title("Speed vs Sudden Acceleration")
plt.savefig("outputs/analytics/bivariate/speed_vs_acc_event.png")
plt.close()


# ===================================================
# 6. DISTANCE vs SUDDEN BRAKING (IMPORTANT)
# ===================================================

plt.figure()
sns.boxplot(x=df["sudden_braking"], y=df["distance_m"])
plt.title("Distance vs Sudden Braking")
plt.savefig("outputs/analytics/bivariate/braking_vs_distance.png")
plt.close()


# ===================================================
# 7. ACCELERATION vs CLOSE OBJECT RISK
# ===================================================

plt.figure()
sns.boxplot(x=df["close_object_risk"], y=df["imu_accel_magnitude"])
plt.title("Acceleration vs Close Object Risk")
plt.savefig("outputs/analytics/bivariate/acceleration_vs_risk.png")
plt.close()


# ===================================================
# 8. SPEED vs OBJECT CLASS
# ===================================================

plt.figure(figsize=(10,6))
sns.boxplot(x=df["class"], y=df["gps_speed_kmh"])
plt.xticks(rotation=45)
plt.title("Speed vs Object Class")
plt.savefig("outputs/analytics/bivariate/speed_vs_class.png")
plt.close()


# ===================================================
# 9. SPEED vs HOUR OF DAY
# ===================================================

plt.figure(figsize=(12,5))
sns.boxplot(x=df["hour_of_day"], y=df["gps_speed_kmh"])
plt.title("Speed vs Hour of Day")
plt.savefig("outputs/analytics/bivariate/speed_vs_hour.png")
plt.close()


# ===================================================
# 10. CLOSE OBJECT RISK vs HOUR
# ===================================================

risk_hour = df.groupby("hour_of_day")["close_object_risk"].sum()

plt.figure()
risk_hour.plot(kind="bar")
plt.title("Close Object Risk by Hour")
plt.savefig("outputs/analytics/bivariate/close_risk_hour.png")
plt.close()


# ===================================================
# 11. RISK PROBABILITY vs SPEED (ADVANCED)
# ===================================================

speed_bins = pd.cut(df["gps_speed_kmh"], bins=10)

risk_prob = df.groupby(speed_bins)["close_object_risk"].mean()

plt.figure()
risk_prob.plot(kind="bar")
plt.title("Risk Probability vs Speed")
plt.xticks(rotation=45)
plt.savefig("outputs/analytics/bivariate/risk_probability_speed.png")
plt.close()


# ===================================================
# 12. DENSITY PLOT (ADVANCED)
# ===================================================

plt.figure()
sns.kdeplot(x=df["gps_speed_kmh"], y=df["distance_m"], fill=True)
plt.title("Speed vs Distance Density")
plt.savefig("outputs/analytics/bivariate/density_speed_distance.png")
plt.close()


# ===================================================
# 13. EVENT CORRELATION HEATMAP (VERY IMPORTANT)
# ===================================================

event_corr = df[[
    "overspeed",
    "sudden_braking",
    "sudden_acceleration",
    "close_object_risk"
]].corr()

plt.figure()
sns.heatmap(event_corr, annot=True)
plt.title("Risk Event Correlation")
plt.savefig("outputs/analytics/bivariate/event_correlation.png")
plt.close()


# ===================================================
# 14. PAIRPLOT (ADVANCED OVERVIEW)
# ===================================================

sns.pairplot(df[[
    "gps_speed_kmh",
    "distance_m",
    "imu_accel_magnitude",
    "speed_diff"
]])
plt.savefig("outputs/analytics/bivariate/pairplot.png")
plt.close()


print("\nBivariate Analysis Completed Successfully")