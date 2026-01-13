def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = (
        followers
        .groupby('user_id')['follower_id'].count()
        .reset_index(name='followers_count')
    )

    return result