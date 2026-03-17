## Tasks:

Load all CSV files from:
data/raw/

Merge the datasets into a single consolidated dataset

Ensure consistent column names across files

Sort records using timestamp

Remove duplicate records if present

Verify data types (timestamp, numeric values, categorical fields)

===========

## Task 2: CSV Dataset Merging

Description:
Merged multiple PiViTeL telemetry CSV files collected from different driving sessions into a single dataset.

Output:
data/processed/pivitel_merged_dataset.csv
==============

## Task 4.1 : Missing Value Investigation and Categorization

### Objective
The objective of this task was to analyze the merged PiViTeL telemetry dataset and identify missing values across different attributes. This analysis helps determine the appropriate data cleaning strategies before performing further analytics.

### Dataset
File analyzed:
data/processed/pivitel_merged_dataset.csv

Dataset size:
- Rows: 4398
- Columns: 47

### Work Performed

The following steps were performed during the missing value investigation phase:

1. Loaded the merged telemetry dataset and inspected its structure.
2. Identified columns containing missing values using pandas functions.
3. Calculated the number of missing values for each attribute.
4. Computed the percentage of missing values relative to the total dataset size.
5. Created a summary table describing missing value distribution.
6. Visualized missing value patterns using a heatmap to detect structural patterns.
7. Categorized columns based on the nature of missing values.

### Missing Value Categories Identified

#### 1. Completely Missing Metadata Columns
These columns contain missing values for all observations.

Examples:
- overlay_time
- overlay_date
- overlay_gps
- overlay_accel_g
- overlay_gyro_deg_s

These attributes likely represent optional overlay information that was not recorded during telemetry capture.

#### 2. Object Detection Related Missing Values
Missing values in detection attributes occur when no object is detected in a frame.

Examples:
- detection_id
- tracking_id
- class
- confidence
- bbox_x
- bbox_y
- bbox_w
- bbox_h
- position
- distance_m

These missing values represent valid frames without object detection.

#### 3. GPS Signal Missing Values
A small number of missing values occur in GPS attributes due to temporary signal interruptions.

Examples:
- latitude
- longitude
- gps_altitude
- gps_hdop

#### 4. Telemetry Measurement Missing Values
Moderate missing values occur in speed and direction attributes.

Examples:
- gps_speed_kmh
- gps_course_degrees

These gaps may occur due to intermittent sensor measurement delays.

### Outcome

The missing value investigation provided a structured understanding of incomplete data within the dataset. This categorization enables the next phase of the project, where appropriate missing value handling techniques will be applied to clean the dataset while preserving the chronological sequence of the vehicle trip.

### Next Step

The next stage involves implementing missing value treatment strategies, including:

- Removing completely empty metadata columns
- Logical imputation for object detection attributes
- Interpolation for GPS coordinates
- Forward filling for speed-related attributes

These steps will prepare the dataset for exploratory data analysis and behavioural modelling.
=====================

## Task 5.0: Feature Engineering for Driving Behaviour Analytics

### Objective
The objective of this task was to transform the cleaned PiViTeL telemetry dataset into a feature-rich dataset by deriving meaningful variables that represent driving behaviour. These features are essential for performing analytical tasks such as risk detection, pattern analysis, and driving score computation in a Pay-As-You-Drive (PAYD) framework.

### Dataset
Input dataset:
data/processed/pivitel_cleaned_dataset.csv

Dataset characteristics:
- Cleaned and validated telemetry data
- No missing values
- Chronologically ordered vehicle trip data

### Work Performed

The following feature engineering steps were implemented to convert raw telemetry data into behaviour-oriented features:

### 1. Speed Change Feature
Computed the difference between consecutive speed values to detect rapid acceleration and deceleration patterns.

- Feature: `speed_change`

### 2. Acceleration Change Feature
Calculated variation in IMU acceleration magnitude to identify abrupt motion patterns.

- Feature: `accel_change`

### 3. Overspeed Event Detection
Identified instances where vehicle speed exceeds a predefined threshold (80 km/h), indicating risky driving behaviour.

- Feature: `overspeed_event`

### 4. Sudden Acceleration Detection
Detected rapid increases in speed based on speed change threshold.

- Feature: `sudden_acceleration`

### 5. Sudden Braking Detection
Identified sharp decreases in speed, indicating abrupt braking events.

- Feature: `sudden_braking`

### 6. Close Object Proximity Detection
Detected situations where objects are very close to the vehicle, indicating potential collision risk.

- Feature: `close_object_event`

### 7. Object Detection Indicator
Created a binary indicator to represent whether an object was detected in a frame.

- Feature: `object_detected`

### 8. Time-Based Feature Extraction
Extracted the hour from timestamp to analyze driving patterns based on time of day.

- Feature: `hour_of_day`

### 9. High Acceleration Event Detection
Identified instances of unusually high acceleration based on dataset mean values.

- Feature: `high_accel_event`

### 10. Distance Change Approximation
Calculated changes in object distance between frames to understand movement dynamics.

- Feature: `distance_change`

### Outcome

The feature engineering process resulted in the creation of a structured dataset containing both raw telemetry data and derived behavioural features.

Output dataset generated:

data/processed/pivitel_feature_dataset.csv

This dataset enables advanced analytics such as:

- Driving behaviour analysis
- Risk event detection
- Feature-based visualization
- Driving score computation

### Importance

The feature dataset transforms raw sensor data into interpretable behavioural indicators, which are essential for building explainable models in the Pay-As-You-Drive framework. These features allow meaningful insights into driver performance and safety patterns.

### Next Phase

The next stage involves performing exploratory data analysis (EDA) using the feature dataset to visualize driving patterns and identify key behavioural trends.
=============