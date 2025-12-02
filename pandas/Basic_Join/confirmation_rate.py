def confirmation_rate(signups: pd.DataFrame, confirmations: pd.DataFrame) -> pd.DataFrame:
    counts = (
        confirmations
        .pivot_table(
            values='time_stamp', 
            index=['user_id'], 
            columns=['action'], 
            aggfunc='count', 
            fill_value=0
        )
        .reset_index()
    )

    for col in ['confirmed', 'timeout']:
        if col not in counts.columns:
            counts[col] = 0

    rates = counts.assign(
        confirmation_rate=lambda df: (df['confirmed'] / (df['confirmed'] + df['timeout'])).round(2)
    )

    result = (
            signups
            .loc[:, ['user_id']]
            .merge(
                rates[['user_id', 'confirmation_rate']], 
                on='user_id', 
                how='left'
            )
            .fillna({'confirmation_rate': 0})
        )
    return result