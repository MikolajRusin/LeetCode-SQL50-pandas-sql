def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_df = sales.merge(product, on='product_id', how='left')
    result = merged_df.loc[:, ['product_name', 'year', 'price']]
    return result

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    result = (
        sales
        .merge(product, on='product_id', how='left')
        .loc[:, ['product_name', 'year', 'price']]
    )
    return result