def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    results = (
        transactions
        .assign(month=lambda df: df['trans_date'].dt.strftime('%Y-%m'))
        .groupby(['month', 'country'], as_index=False, dropna=False)
        .agg(
            trans_count=('state', 'count'),
            approved_count=('state', lambda x: sum(x == 'approved')),
            trans_total_amount=('amount', 'sum'),
            approved_total_amount=('amount', lambda x: x[transactions['state'] == 'approved'].sum())
        )
    )
    return results

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = (
        transactions
        .assign(
            month=lambda df: df['trans_date'].dt.strftime('%Y-%m'),
            approved_amount=lambda df: df['amount'].where(df['state'] == 'approved', 0)
        )
    )
    
    results = (
        transactions
        .groupby(['month', 'country'], as_index=False, dropna=False)
        .agg(
            trans_count=('state', 'count'),
            approved_count=('approved_amount', lambda x: sum(x > 0)),
            trans_total_amount=('amount', 'sum'),
            approved_total_amount=('approved_amount', lambda x: x[transactions['state'] == 'approved'].sum())
        )
    )
    return results