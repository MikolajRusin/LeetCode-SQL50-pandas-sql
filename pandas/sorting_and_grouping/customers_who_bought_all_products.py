def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    total_products = product['product_key'].nunique()

    counts = (
        customer
        .groupby('customer_id')['product_key'].nunique()
        .reset_index(name='n_products')
    )
    return counts.loc[counts['n_products'] == total_products, ['customer_id']]