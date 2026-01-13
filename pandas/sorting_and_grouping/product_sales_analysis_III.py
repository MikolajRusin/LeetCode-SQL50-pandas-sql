def sales_analysis(sales: pd.DataFrame) -> pd.DataFrame:
    product_first_year = (
        sales
        .groupby('product_id')['year']
        .transform('min')
    )

    results = (
        sales
        .loc[sales['year'] == product_first_year]
        .rename(columns={'year': 'first_year'})
        .drop('sale_id', axis=1)
    )
    return results