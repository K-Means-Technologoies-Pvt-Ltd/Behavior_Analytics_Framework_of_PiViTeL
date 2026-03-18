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
os.makedirs("outputs/analytics/univariate", exist_ok=True)

# ===================================================
# 1. VEHICLE SPEED DISTRIBUTION (HISTOGRAM)
# ===================================================

plt.figure()
plt.hist(df["gps_speed_kmh"], bins=30)
plt.title("Vehicle Speed Distribution")
plt.xlabel("Speed (km/h)")
plt.ylabel("Frequency")
plt.savefig("outputs/analytics/univariate/speed_histogram.png")
plt.close()


# ===================================================
# 2. VEHICLE SPEED BOXPLOT
# ===================================================

plt.figure()
plt.boxplot(df["gps_speed_kmh"])
plt.title("Vehicle Speed Boxplot")
plt.ylabel("Speed (km/h)")
plt.savefig("outputs/analytics/univariate/speed_boxplot.png")
plt.close()

# ===================================================
# 3. ACCELERATION DISTRIBUTION
# ===================================================

plt.figure()
plt.hist(df["imu_accel_magnitude"], bins=30)
plt.title("Acceleration Distribution")
plt.xlabel("Acceleration")
plt.ylabel("Frequency")
plt.savefig("outputs/analytics/univariate/acceleration_distribution.png")
plt.close()

# ===================================================
# 3. OVERSPEED - Distribution
# ===================================================
plt.figure(figsize=(10, 6))
df["overspeed"].value_counts().plot(kind='bar', color=['lightblue', 'salmon'])
plt.title("Overspeed Events Distribution")
plt.xlabel("Overspeed")
plt.ylabel("Count")
plt.xticks(rotation=0)
for i, v in enumerate(df["overspeed"].value_counts()):
    plt.text(i, v + len(df)*0.002, str(int(v)), ha='center', fontweight='bold')
plt.grid(True, alpha=0.3)
plt.savefig("outputs/analytics/univariate/overspeed_distribution.png", dpi=150, bbox_inches='tight')
plt.close()

# ===================================================
# 4. SUDDEN BRAKING - Distribution
# ===================================================
plt.figure()
df["sudden_braking"].value_counts().plot(kind='bar')
plt.title("Sudden Braking Events")
plt.xlabel("Sudden Braking")
plt.ylabel("Count")

plt.savefig("outputs/analytics/univariate/sudden_braking_distribution.png")
plt.close()

# ===================================================
# 4. SUDDEN ACCELERATION - Distribution
# ===================================================
plt.figure()
df["sudden_acceleration"].value_counts().plot(kind='bar')
plt.title("Sudden acceleration Events")
plt.xlabel("Sudden acceleration")
plt.ylabel("Count")

plt.savefig("outputs/analytics/univariate/sudden_braking_distribution.png")
plt.close()


# ===================================================
# 5. HIGH ACCELERATION - Distribution
# ===================================================
plt.figure()
df["high_acceleration"].value_counts().plot(kind='bar')
plt.title("High acceleration Events")
plt.xlabel("High acceleration")
plt.ylabel("Count")

plt.savefig("outputs/analytics/univariate/high_accleration_distribution.png")
plt.close()

# ===================================================
# 5. CLOSE OBJECT RISK - Distribution
# ===================================================
plt.figure()
df["close_object_risk"].value_counts().plot(kind='bar')
plt.title("Close Object Risk Events")
plt.xlabel("Close Object Risk")
plt.ylabel("Count")

plt.savefig("outputs/analytics/univariate/close_object_risk.png")
plt.close()

# ===================================================
# 6. GPS ROUTE - SIMPLE SCATTER MAP
# ===================================================
plt.figure()
plt.scatter(df["longitude"], df["latitude"], c=df["gps_speed_kmh"])
plt.colorbar(label="Speed (km/h)")
plt.title("GPS Route")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.savefig("outputs/analytics/univariate/gps_route.png")
plt.close()


# ===================================================
# 7. GPS COURSE DEGREES - Direction Analysis
# ===================================================
# Rose diagram (circular histogram)
angles = np.radians(df["gps_course_degrees"])

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})

# Fix orientation (VERY IMPORTANT)
ax.set_theta_zero_location('N')   # 0° at North (top)
ax.set_theta_direction(-1)        # Clockwise direction

# Plot histogram
ax.hist(angles, bins=30)
ax.set_title("GPS Course Rose Plot")
plt.savefig("outputs/analytics/univariate/gps_course_rose_plot.png")
plt.close()

# ===================================================
# 8. PIE CHART (RISK DISTRIBUTION)
# ===================================================

events = [
    df["overspeed"].sum(),
    df["sudden_braking"].sum(),
    df["sudden_acceleration"].sum(),
    df["close_object_risk"].sum()
]

labels = ["Overspeed", "Braking", "Acceleration", "Close Risk"]

plt.figure()
plt.pie(events, labels=labels, autopct='%1.1f%%')
plt.title("Risk Event Distribution")
plt.savefig("outputs/analytics/univariate/risk_pie.png")
plt.close()

# ===================================================
# 9. OBJECT CLASS DISTRIBUTION 
# ===================================================
value_counts = df["class"].value_counts().head(10)
plt.figure()
plt.pie(value_counts.values, labels=value_counts.index, autopct='%1.1f%%')
plt.title("Object Class Pie Chart")
plt.savefig("outputs/analytics/univariate/class_pie.png")
plt.close()

# ===================================================
# 10. CONFIDENCE DISTRIBUTION 
# ===================================================

plt.figure()
plt.hist(df["confidence"], bins=30)
plt.title("Confidence Distribution")
plt.xlabel("Confidence Score")
plt.ylabel("Frequency")
plt.savefig("outputs/analytics/univariate/confidence_histogram.png")
plt.close()

# ===================================================
# 11. HOUR OF DAY
# ===================================================
plt.figure()
df["hour_of_day"].value_counts().sort_index().plot(kind='bar')

plt.title("Driving by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")

plt.savefig("outputs/analytics/univariate/hour_of_day.png")
plt.close()

# ===================================================
# 12. NIGHT DRIVING
# ===================================================
plt.figure()
df["night_driving"].value_counts().plot(kind='bar')
plt.title("Night Driving")
plt.xlabel("0 = Day, 1 = Night")
plt.ylabel("Count")
plt.savefig("outputs/analytics/univariate/night_driving.png")
plt.close()

# ===================================================
# 13. TRIP DISTANCE
# ===================================================
plt.figure()
plt.hist(df["trip_distance"].dropna(), bins=30)
plt.title("Trip Distance Distribution")
plt.xlabel("Distance")
plt.ylabel("Frequency")
plt.savefig("outputs/analytics/univariate/trip_distance.png")
plt.close()


# ===================================================
# 14. RISK EVENTS BY HOUR
# ===================================================
plt.figure()
risk = df.groupby("hour_of_day")[['overspeed', 'sudden_braking', 'close_object_risk']].sum()
risk.plot(kind='bar', stacked=True)
plt.title("Risk Events by Hour")
plt.xlabel("Hour")
plt.ylabel("Count")
plt.savefig("outputs/analytics/univariate/risk_by_hour.png")
plt.close()