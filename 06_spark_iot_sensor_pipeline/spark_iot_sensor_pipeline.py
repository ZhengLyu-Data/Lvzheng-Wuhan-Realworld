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

# run_pipeline.py

# Step 1: Run data cleaning
print("Running data cleaning script...")
!python3 clean_data.py

# Step 2: Run data analysis pipeline
print("Running data analysis pipeline script...")
!python3 pipeline.py

print("All steps completed successfully.")

# Step 3: Visualization - Generate and Save Charts
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the cleaned dataset
df_cleaned = pd.read_csv('iot_sensor_fault_cleaned.csv')

# Chart 1: Fault Type Distribution
plt.figure(figsize=(6, 4))
sns.countplot(data=df_cleaned, x='fault_label')
plt.title('Fault Type Distribution')
plt.tight_layout()
plt.savefig('fault_type_distribution.png')
plt.close()

# Chart 2: Vibration Level by Fault Type
plt.figure(figsize=(6, 4))
sns.boxplot(data=df_cleaned, x='fault_label', y='vibration')
plt.title('Vibration by Fault Type')
plt.tight_layout()
plt.savefig('vibration_fault_boxplot.png')
plt.close()

# Chart 3: Temperature by Fault Type
plt.figure(figsize=(6, 4))
sns.violinplot(data=df_cleaned, x='fault_label', y='temperature')
plt.title('Temperature by Fault Type')
plt.tight_layout()
plt.savefig('temperature_fault_violinplot.png')
plt.close()

# Chart 4: Pressure Distribution by Fault Type
plt.figure(figsize=(6, 4))
sns.boxplot(data=df_cleaned, x='fault_label', y='pressure')
plt.title('Pressure by Fault Type')
plt.tight_layout()
plt.savefig('pressure_fault_boxplot.png')
plt.close()

# Optional download for Colab environment
try:
    import google.colab
    IN_COLAB = True
except ImportError:
    IN_COLAB = False

if IN_COLAB:
    from google.colab import files
    files.download("fault_type_distribution.png")
    files.download("vibration_fault_boxplot.png")
    files.download("temperature_fault_violinplot.png")
    files.download("pressure_fault_boxplot.png")
else:
    print("All charts saved locally. You can find them in the current directory.")
