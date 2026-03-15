import pandas as pd
import os

# Relative paths from project root
RAW_FOLDER = "data/raw"
OUTPUT_FILE = "data/processed/pivitel_merged_dataset.csv"

VIDEO_FILE = os.path.join(RAW_FOLDER, r"C:\Users\Lenovo\OneDrive\Desktop\Behavior_Analytics_Framework_of_PiViTeL\data\raw\driving_video.csv")
SENSOR_FILE = os.path.join(RAW_FOLDER, r"C:\Users\Lenovo\OneDrive\Desktop\Behavior_Analytics_Framework_of_PiViTeL\data\raw\sesor_data.csv")


def standardize_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def merge_datasets():

    print("Loading datasets...")

    video_df = pd.read_csv(VIDEO_FILE)
    sensor_df = pd.read_csv(SENSOR_FILE)

    video_df = standardize_columns(video_df)
    sensor_df = standardize_columns(sensor_df)

    print("Merging datasets on frame_number...")

    merged_df = pd.merge(
        video_df,
        sensor_df,
        on="frame_number",
        how="inner"
    )

    # Convert timestamp
    if "timestamp" in merged_df.columns:
        merged_df["timestamp"] = pd.to_datetime(merged_df["timestamp"], errors="coerce")

    # Remove duplicates
    merged_df = merged_df.drop_duplicates()

    # Sort by timestamp
    if "timestamp" in merged_df.columns:
        merged_df = merged_df.sort_values("timestamp")

    # Ensure processed folder exists
    os.makedirs("data/processed", exist_ok=True)

    # Save merged dataset
    merged_df.to_csv(OUTPUT_FILE, index=False)

    print("Merged dataset saved to:", OUTPUT_FILE)
    print("Total rows:", len(merged_df))


if __name__ == "__main__":
    merge_datasets()