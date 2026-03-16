import pandas as pd

# ---------------------------------------------------
# Load Dataset
# ---------------------------------------------------

DATA_PATH = "data/processed/pivitel_merged_dataset.csv"

df = pd.read_csv(DATA_PATH)

print("Dataset Loaded")
print("Shape:", df.shape)


# ---------------------------------------------------
# Remove Completely Missing Overlay Columns
# ---------------------------------------------------

overlay_columns = [
    "overlay_time",
    "overlay_date",
    "overlay_gps",
    "overlay_accel_g",
    "overlay_gyro_deg_s"
]

df = df.drop(columns=overlay_columns, errors="ignore")


# ---------------------------------------------------
# Handle Object Detection Missing Values
# ---------------------------------------------------

df["class"] = df["class"].fillna("no_object")

df["confidence"] = df["confidence"].fillna(0)

bbox_cols = ["bbox_x", "bbox_y", "bbox_w", "bbox_h"]

for col in bbox_cols:
    df[col] = df[col].fillna(0)

df["position"] = df["position"].fillna("unknown")

df["distance_m"] = df["distance_m"].fillna(-1)

df["detection_id"] = df["detection_id"].fillna(-1)

df["tracking_id"] = df["tracking_id"].fillna(-1)


# ---------------------------------------------------
# Handle GPS Missing Values
# ---------------------------------------------------

gps_cols = ["latitude", "longitude", "gps_altitude"]

for col in gps_cols:
    df[col] = df[col].interpolate()
    df[col] = df[col].ffill()
    df[col] = df[col].bfill()


# ---------------------------------------------------
# Handle GPS Precision Values
# ---------------------------------------------------

df["gps_hdop"] = df["gps_hdop"].interpolate().ffill().bfill()

df["gps_data_age_seconds"] = df["gps_data_age_seconds"].interpolate().ffill().bfill()


# ---------------------------------------------------
# Handle Speed Missing Values
# ---------------------------------------------------

df["gps_speed_kmh"] = df["gps_speed_kmh"].ffill().bfill()

df["gps_course_degrees"] = df["gps_course_degrees"].ffill().bfill()


# ---------------------------------------------------
# Convert Timestamp Columns
# ---------------------------------------------------

df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")

df["system_time"] = pd.to_datetime(df["system_time"], errors="coerce")


# ---------------------------------------------------
# Drop system_time (invalid format column)
# ---------------------------------------------------

df = df.drop(columns=["system_time"], errors="ignore")


# ---------------------------------------------------
# Reconstruct Vehicle Trip Timeline
# ---------------------------------------------------

df = df.sort_values(by="timestamp")

df.reset_index(drop=True, inplace=True)


# ---------------------------------------------------
# Detect Sensor Time Gaps
# ---------------------------------------------------

df["time_gap"] = df["timestamp"].diff()

df["time_gap"] = df["time_gap"].fillna(pd.Timedelta(seconds=0))


print("\nTime Gap Statistics")

print(df["time_gap"].describe())


# ---------------------------------------------------
# Verify Missing Values
# ---------------------------------------------------

print("\nMissing Values After Cleaning")

print(df.isnull().sum())


# ---------------------------------------------------
# Save Clean Dataset
# ---------------------------------------------------

OUTPUT_PATH = "data/processed/pivitel_cleaned_dataset.csv"

df.to_csv(OUTPUT_PATH, index=False)

print("\nClean dataset saved successfully at:", OUTPUT_PATH)