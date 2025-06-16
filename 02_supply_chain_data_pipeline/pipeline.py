def process_data(df):
    results = {}

    # 1. Average Product Cost by Shipping Mode
    avg_cost_by_mode = df.groupby("mode_of_shipment")["product_cost"].mean()
    results["avg_cost_by_mode"] = avg_cost_by_mode

    # 2. Average Discount by Product Importance
    avg_discount_by_importance = df.groupby("product_importance")["discount"].mean()
    results["avg_discount_by_importance"] = avg_discount_by_importance

    # 3. Correlation between Customer Rating and Product Cost
    correlation_rating_cost = df["customer_rating"].corr(df["product_cost"])
    results["correlation_rating_cost"] = correlation_rating_cost

    return results