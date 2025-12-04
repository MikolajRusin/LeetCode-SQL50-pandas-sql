def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    results = (
        prices
        .merge(units_sold, on='product_id', how='left')
        .assign(
            valid_date=lambda df: (df['start_date'] <= df['purchase_date']) & (df['purchase_date'] <= df['end_date']),
            price=lambda df: df['price'].where(df['valid_date'], 0),
            units=lambda df: df['units'].where(df['valid_date'], 0),
            total_price=lambda df: df['units'] * df['price']
        )
        .groupby('product_id', as_index=False)[['units', 'total_price']].sum()
        .assign(average_price=lambda df: round(df['total_price'] / df['units'].replace(0, 1), 2))
        .loc[:, ['product_id', 'average_price']]
    )

    return results