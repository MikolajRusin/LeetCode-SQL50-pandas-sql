def gameplay_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    first_login = (
        activity
        .groupby('player_id', as_index=False)['event_date'].min()
        .assign(next_day_expected=lambda df: df['event_date'] + pd.DateOffset(1))
    )

    retained_players = (
        first_login
        .merge(activity, how='inner', left_on=['player_id', 'next_day_expected'], right_on=['player_id', 'event_date'])
    )

    fraction = round(retained_players['player_id'].nunique() / activity['player_id'].nunique(), 2)
    return pd.DataFrame({'fraction': [fraction]})