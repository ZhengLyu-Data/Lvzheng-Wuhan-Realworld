# pipeline.py

import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("iot_sensor_fault_cleaned.csv")

# Extract date from timestamp
df["date"] = pd.to_datetime(df["timestamp"]).dt.date

# Count of faults per day
faults_by_date = df[df["fault_label"] == 1].groupby("date").size().reset_index(name="fault_count")

# Daily average values for all sensors
daily_avg = df.groupby("date")[["vibration", "temperature", "pressure"]].mean().reset_index()

# Comparison of sensor values: normal vs. fault
summary_by_fault = df.groupby("fault_label")[["vibration", "temperature", "pressure"]].mean().reset_index()

# Save the output analysis files
faults_by_date.to_csv("faults_by_date.csv", index=False)
daily_avg.to_csv("daily_avg.csv", index=False)
summary_by_fault.to_csv("summary_by_fault.csv", index=False)