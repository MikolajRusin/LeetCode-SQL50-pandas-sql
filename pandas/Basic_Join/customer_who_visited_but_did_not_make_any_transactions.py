def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    merged_df = visits.merge(transactions, on='visit_id', how='left')
    no_transactions = merged_df.loc[merged_df['transaction_id'].isna()]
    result = no_transactions.groupby('customer_id')[['visit_id']].count()
    result = result.reset_index()
    result = result.rename(columns={'visit_id': 'count_no_trans'})
    return result

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    result = (
        visits
        .merge(transactions, on='visit_id', how='left')
        .loc[lambda df: df['transaction_id'].isna()]
        .groupby('customer_id')[['visit_id']].count()
        .reset_index()
        .rename(columns={'visit_id': 'count_no_trans'})
    )
    return result