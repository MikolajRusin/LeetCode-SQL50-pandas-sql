def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products.loc[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y'), ['product_id']]

# Or more clearly
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    keep_mask = (products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')
    return products.loc[keep_mask, ['product_id']]

#Or pipeline way
def find_products(products: pd.DataFrame) -> pd.DataFrame:
    filtered_products = (
        products
        .query("low_fats == 'Y' & recyclable == 'Y'")
        .loc[:, ['product_id']]
    )
    return filtered_products