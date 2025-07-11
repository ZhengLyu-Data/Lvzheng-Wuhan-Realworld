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