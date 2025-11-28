def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    mask = tweets['content'].str.len() > 15
    return tweets.loc[mask, ['tweet_id']]

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['content_len'] = tweets['content'].map(lambda x: len(x) > 15)
    return tweets.loc[tweets['content_len'], ['tweet_id']]

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    tweets['content_len'] = tweets['content'].str.len()
    invalid_tweets_ids = (
        tweets
        .query('content_len > 15')
        .loc[:, ['tweet_id']]
    )
    return invalid_tweets_ids