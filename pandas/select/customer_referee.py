def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    return customer.loc[(customer['referee_id'].isna()) | (customer['referee_id'] != 2), ['name']]

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    keep_mask = (customer['referee_id'].isna()) | (customer['referee_id'] != 2)
    return customer.loc[keep_mask, ['name']]

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    filtered_customer = (
        customer
        .query('referee_id.isna() | referee_id != 2')
        .loc[:, ['name']]
    )
    return filtered_customer