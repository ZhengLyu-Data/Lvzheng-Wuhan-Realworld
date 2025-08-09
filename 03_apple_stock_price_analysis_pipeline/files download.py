import shutil
from zipfile import ZipFile

# Files to include
files_to_zip = [
    "clean_apple_stock.csv",
    "price_with_ma.png",
    "daily_return_hist.png",
    "volatility_trend.png"
]

# Zip file name
zip_filename = "apple_stock_outputs.zip"

# Create zip
with ZipFile(zip_filename, 'w') as zipf:
    for file in files_to_zip:
        try:
            zipf.write(file)
        except FileNotFoundError:
            print(f"File not found: {file}")

print(f"Created: {zip_filename}")

# For Google Colab download
try:
    from google.colab import files
    files.download(zip_filename)
except ImportError:
    print("Not running in Colab. Please download manually.")