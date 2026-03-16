## Tasks:

Load all CSV files from:
data/raw/

Merge the datasets into a single consolidated dataset

Ensure consistent column names across files

Sort records using timestamp

Remove duplicate records if present

Verify data types (timestamp, numeric values, categorical fields)

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
# Shruti Sarmah – Contribution Log
## Task 2: CSV Dataset Merging

Description:
Merged multiple PiViTeL telemetry CSV files collected from different driving sessions into a single dataset.

Output:
data/processed/pivitel_merged_dataset.csv
