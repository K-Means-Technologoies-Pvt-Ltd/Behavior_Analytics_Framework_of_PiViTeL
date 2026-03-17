import pandas as pd
import numpy as np

DATA_PATH = "data/processed/pivitel_cleaned_dataset.csv"

print("Loading dataset...\n")

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded Successfully")
print("Dataset Shape:", df.shape)

# convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

#driving time feature
df['time_diff'] = df['timestamp'].diff().dt.total_seconds()

#speed change feature
df['speed_diff'] = df['gps_speed_kmh'].diff()

#acceleration change feature
df['acceleration_change'] = df['imu_accel_magnitude'].diff()

#overspeed detection
SPEED_LIMIT = 60
df['overspeed'] = df['gps_speed_kmh'] > SPEED_LIMIT

#sudden acceleration event
ACC_THRESHOLD = 2.5  # tune this
df['sudden_acceleration'] = df['speed_diff'] > ACC_THRESHOLD

#sudden braking event
BRAKE_THRESHOLD = -2.5
df['sudden_braking'] = df['speed_diff'] < BRAKE_THRESHOLD

#high acceleration event
df['high_acceleration'] = df['imu_accel_magnitude'] > df['imu_accel_magnitude'].mean()

#object detection indicator
df['object_detected'] = df['class'].notnull()

#close object risk
DIST_THRESHOLD = 5
df['close_object_risk'] = df['distance_m'] < DIST_THRESHOLD

#trip distance approximation
df['trip_distance'] = df['distance_m'].diff().abs()

OUTPUT_PATH = "data/processed/pivitel_feature_dataset.csv"
df.to_csv(OUTPUT_PATH, index = False)