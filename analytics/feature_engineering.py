import pandas as pd

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_cleaned_dataset.csv"

print("Loading dataset...\n")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)


# ---------------------------------------------------
# Convert Timestamp
# ---------------------------------------------------

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')


# ---------------------------------------------------
# Time Difference Feature (in seconds)
# ---------------------------------------------------

df['time_diff'] = df['timestamp'].diff().dt.total_seconds()
df['time_diff'] = df['time_diff'].fillna(0)


# ---------------------------------------------------
# Speed Change Feature
# ---------------------------------------------------

df['speed_diff'] = df['gps_speed_kmh'].diff()
df['speed_diff'] = df['speed_diff'].fillna(0)


# ---------------------------------------------------
# Acceleration Change Feature
# ---------------------------------------------------

df['acceleration_change'] = df['imu_accel_magnitude'].diff()
df['acceleration_change'] = df['acceleration_change'].fillna(0)


# ---------------------------------------------------
# Overspeed Detection
# ---------------------------------------------------

SPEED_LIMIT = 60
df['overspeed'] = df['gps_speed_kmh'] > SPEED_LIMIT


# ---------------------------------------------------
# Sudden Acceleration & Braking
# ---------------------------------------------------

ACC_THRESHOLD = 10     # realistic threshold for km/h diff
BRAKE_THRESHOLD = -10

df['sudden_acceleration'] = df['speed_diff'] > ACC_THRESHOLD
df['sudden_braking'] = df['speed_diff'] < BRAKE_THRESHOLD


# ---------------------------------------------------
# High Acceleration Event (IMU based)
# ---------------------------------------------------

imu_threshold = df['imu_accel_magnitude'].mean() + df['imu_accel_magnitude'].std()

df['high_acceleration'] = df['imu_accel_magnitude'] > imu_threshold


# ---------------------------------------------------
# Object Detection Indicator (Corrected)
# ---------------------------------------------------

df['object_detected'] = df['class'] != "no_object"


# ---------------------------------------------------
# Close Object Risk
# ---------------------------------------------------

DIST_THRESHOLD = 5
df['close_object_risk'] = df['distance_m'] < DIST_THRESHOLD


# ---------------------------------------------------
# Trip Distance Approximation
# ---------------------------------------------------

df['trip_distance'] = df['distance_m'].diff().abs()
df['trip_distance'] = df['trip_distance'].fillna(0)


# ---------------------------------------------------
# Time-Based Feature
# ---------------------------------------------------

df['hour_of_day'] = df['timestamp'].dt.hour


# ---------------------------------------------------
# Additional PAYD Features (Important)
# ---------------------------------------------------

# Driving at night (risk factor)
df['night_driving'] = (df['hour_of_day'] < 6) | (df['hour_of_day'] > 22)

# Combined risk flag
df['high_risk_event'] = (
    df['overspeed'] |
    df['sudden_acceleration'] |
    df['sudden_braking'] |
    df['close_object_risk']
)


# ---------------------------------------------------
# Save Feature Dataset
# ---------------------------------------------------

OUTPUT_PATH = "data/processed/pivitel_feature_dataset.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nFeature dataset saved successfully at:", OUTPUT_PATH)