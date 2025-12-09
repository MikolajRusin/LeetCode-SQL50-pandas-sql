def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    n_users = users['user_id'].nunique()
    percentage_user_contest = ((register.groupby('contest_id')['user_id'].count() / n_users) * 100).round(2)
    percentage_user_contest = percentage_user_contest.reset_index()
    percentage_user_contest.rename(columns={'user_id': 'percentage'}, inplace=True)
    percentage_user_contest.sort_values(['percentage', 'contest_id'], ascending=[False, True], inplace=True)
    return percentage_user_contest

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    results = (
        register
        .groupby('contest_id', as_index=False)['user_id'].count()
        .assign(percentage=lambda df: (df['user_id'] / users['user_id'].nunique()) * 100)
        .round({'percentage': 2})
        .loc[:, ['contest_id', 'percentage']]
        .sort_values(['percentage', 'contest_id'], ascending=[False, True])
    )
    return results