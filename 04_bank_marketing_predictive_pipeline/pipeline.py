def analyze_marketing_data(df):
    results = {}

    # Response by Occupation
    results['response_by_occupation'] = (
        df.groupby('occupation')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    #  Response by Housing Loan
    results['response_by_housing'] = (
        df.groupby('has_housing_loan')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    #  Response by Education Level
    results['response_by_education'] = (
        df.groupby('education_level')['response']
        .value_counts(normalize=True)
        .unstack()
        .fillna(0)
        .round(2)
    )

    return results