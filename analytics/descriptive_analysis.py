import pandas as pd

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_feature_dataset.csv"

print("Loading dataset...\n")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Shape:", df.shape)


# ---------------------------------------------------
# 1. BASIC STATISTICAL SUMMARY
# ---------------------------------------------------

print("\n==============================")
print("BASIC STATISTICS")
print("==============================\n")

stats = df.describe()

print(stats)


# ---------------------------------------------------
# 2. CENTRAL TENDENCY ANALYSIS
# ---------------------------------------------------

print("\n==============================")
print("CENTRAL TENDENCY")
print("==============================\n")

print("Average Speed:", df["gps_speed_kmh"].mean())
print("Median Speed:", df["gps_speed_kmh"].median())

print("\nAverage Acceleration:", df["imu_accel_magnitude"].mean())

print("\nAverage Distance to Object:", df["distance_m"].mean())


# ---------------------------------------------------
# 3. VARIABILITY ANALYSIS
# ---------------------------------------------------

print("\n==============================")
print("VARIABILITY ANALYSIS")
print("==============================\n")

print("Speed Std Dev:", df["gps_speed_kmh"].std())
print("Acceleration Std Dev:", df["imu_accel_magnitude"].std())
print("Distance Std Dev:", df["distance_m"].std())


# ---------------------------------------------------
# 4. EXTREME VALUES ANALYSIS
# ---------------------------------------------------

print("\n==============================")
print("EXTREME VALUES")
print("==============================\n")

print("Max Speed:", df["gps_speed_kmh"].max())
print("Min Speed:", df["gps_speed_kmh"].min())

print("\nMax Acceleration:", df["imu_accel_magnitude"].max())
print("Min Acceleration:", df["imu_accel_magnitude"].min())


# ---------------------------------------------------
# 5. DRIVING EVENT COUNTS
# ---------------------------------------------------

print("\n==============================")
print("DRIVING EVENT COUNTS")
print("==============================\n")

overspeed_count = df["overspeed"].sum()
acc_count = df["sudden_acceleration"].sum()
brake_count = df["sudden_braking"].sum()
close_risk_count = df["close_object_risk"].sum()
night_count = df["night_driving"].sum()

print("Overspeed Events:", overspeed_count)
print("Sudden Acceleration Events:", acc_count)
print("Sudden Braking Events:", brake_count)
print("Close Object Risk Events:", close_risk_count)
print("Night Driving Instances:", night_count)


# ---------------------------------------------------
# 6. EVENT PERCENTAGE ANALYSIS (VERY IMPORTANT)
# ---------------------------------------------------

print("\n==============================")
print("EVENT PERCENTAGES")
print("==============================\n")

total = len(df)

print("Overspeed %:", (overspeed_count / total) * 100)
print("Sudden Acceleration %:", (acc_count / total) * 100)
print("Sudden Braking %:", (brake_count / total) * 100)
print("Close Object Risk %:", (close_risk_count / total) * 100)


# ---------------------------------------------------
# 7. SAVE RESULTS
# ---------------------------------------------------

stats.to_csv("outputs/analytics/descriptive_statistics.csv")

print("\nDescriptive statistics saved successfully.")


# ---------------------------------------------------
# SAVE OUTPUT TO TEXT FILE
# ---------------------------------------------------

with open("outputs/descriptive_analysis.txt", "w") as f:
    
    f.write("CENTRAL TENDENCY\n")
    f.write(f"Average Speed: {df['gps_speed_kmh'].mean()}\n")
    f.write(f"Median Speed: {df['gps_speed_kmh'].median()}\n")
    f.write(f"Average Acceleration: {df['imu_accel_magnitude'].mean()}\n")
    f.write(f"Average Distance: {df['distance_m'].mean()}\n\n")

    f.write("VARIABILITY ANALYSIS\n")
    f.write(f"Speed Std Dev: {df['gps_speed_kmh'].std()}\n")
    f.write(f"Acceleration Std Dev: {df['imu_accel_magnitude'].std()}\n")
    f.write(f"Distance Std Dev: {df['distance_m'].std()}\n\n")

    f.write("EXTREME VALUES\n")
    f.write(f"Max Speed: {df['gps_speed_kmh'].max()}\n")
    f.write(f"Min Speed: {df['gps_speed_kmh'].min()}\n\n")

    f.write("EVENT COUNTS\n")
    f.write(f"Overspeed: {df['overspeed'].sum()}\n")
    f.write(f"Sudden Acceleration: {df['sudden_acceleration'].sum()}\n")
    f.write(f"Sudden Braking: {df['sudden_braking'].sum()}\n")
    f.write(f"Close Risk: {df['close_object_risk'].sum()}\n\n")

    total = len(df)

    f.write("EVENT PERCENTAGES\n")
    f.write(f"Overspeed %: {(df['overspeed'].sum()/total)*100}\n")
    f.write(f"Acceleration %: {(df['sudden_acceleration'].sum()/total)*100}\n")
    f.write(f"Braking %: {(df['sudden_braking'].sum()/total)*100}\n")
    f.write(f"Close Risk %: {(df['close_object_risk'].sum()/total)*100}\n")

print("Descriptive analysis saved as text file.")