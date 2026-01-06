def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    end_date = pd.to_datetime('2019-7-29')
    start_date = end_date - pd.Timedelta(days=31)
    results = (
        activity
        .loc[(activity['activity_date'] >= start_date) & (activity['activity_date'] <= end_date)]
        .groupby('activity_date', as_index=False)['user_id'].nunique()
        .rename(columns={'activity_date': 'day', 'user_id': 'active_users'})
    )
    return results