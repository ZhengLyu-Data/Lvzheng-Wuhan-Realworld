# clean_data.py

import pandas as pd

# Load the raw dataset
df = pd.read_csv("iot_sensor_fault_raw.csv")

# Standardize column names
df.columns = [
    "timestamp", "vibration", "temperature", "pressure",
    "rms_vibration", "mean_temp", "fault_label"
]

# Convert timestamp to datetime
df["timestamp"] = pd.to_datetime(df["timestamp"])

# Drop missing values if any
df.dropna(inplace=True)

# Save cleaned data
df.to_csv("iot_sensor_fault_cleaned.csv", index=False)

# Export the cleaned DataFrame as a CSV file
df.to_csv("iot_sensor_fault_cleaned.csv", index=False)