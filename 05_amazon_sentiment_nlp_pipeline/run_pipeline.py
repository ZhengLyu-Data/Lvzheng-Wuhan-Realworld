from pipeline import process_reviews

if __name__ == "__main__":
    input_csv = "/content/amazon_reviews_raw.csv"        
    output_csv = "/content/processed_reviews.csv"
    process_reviews(input_csv, output_csv)
    print(f"✅ Pipeline completed. Output saved to {output_csv}")