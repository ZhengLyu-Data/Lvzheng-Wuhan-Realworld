# Add this at the bottom of run_pipeline.py after main() finishes
from google.colab import files

def download_outputs():
    files_to_download = [
        "walmart_weekly_clean.csv",
        "chart1_weekly_trend.png",
        "chart2_store_yoy_top10.png",
        "chart3_dept_lift_top20.png"
    ]
    for f in files_to_download:
        try:
            files.download(f)
            print(f"[download] {f} downloaded successfully.")
        except Exception as e:
            print(f"[download] Failed to download {f}: {e}")

if __name__ == "__main__":
    main()
    download_outputs()