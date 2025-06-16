from clean_data import clean_supply_chain_data
from pipeline import process_data

if __name__ == '__main__':
    # Load and clean data
    input_file = 'supply_chain_raw.csv'
    df_cleaned = clean_supply_chain_data(input_file)

    # Run analysis
    results = process_data(df_cleaned)

    # Output results
    print("\n📦 Average Product Cost by Shipping Mode:")
    print(results["avg_cost_by_mode"])

    print("\n💸 Average Discount by Product Importance:")
    print(results["avg_discount_by_importance"])

    print("\n📊 Correlation between Customer Rating and Product Cost:")
    print(round(results["correlation_rating_cost"], 4))
