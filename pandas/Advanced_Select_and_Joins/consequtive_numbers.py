def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    cons_nums = (
        logs
        .sort_values('id')
        .assign(
            variance=lambda df: df['num'].rolling(window=3).var()
        )
        .loc[lambda df: df['variance'] == 0, ['num']]
        .drop_duplicates()
        .rename(columns={'num': 'ConsecutiveNums'})
    )

    return cons_nums

#OR
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    cons_mask = ( (logs['num'] == logs['num'].shift(-1)) & (logs['num'] == logs['num'].shift(-2)) )
    cons_nums = (
        logs
        .loc[cons_mask, ['num']]
        .drop_duplicates()
        .rename(columns={'num': 'ConsecutiveNums'})
    )
    return cons_nums

#OR
def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['variance'] = logs['num'].rolling(window=3).var()
    cons_nums = logs.query('variance == 0')['num']
    
    return pd.DataFrame({'ConsecutiveNums': cons_nums.unique()})