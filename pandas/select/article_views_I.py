def article_views(views: pd.DataFrame) -> pd.DataFrame:
    keep_mask = views['author_id'] == views['viewer_id']
    author_viewed_own = views[keep_mask]
    ids = author_viewed_own[['author_id']].rename(columns={'author_id': 'id'})
    u_ids = ids.drop_duplicates()
    u_ids = u_ids.sort_values('id')
    return u_ids

# Or
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = pd.DataFrame(
        views
        .loc[views['author_id'] == views['viewer_id'], 'author_id']
        .unique(),
        columns=['id']
    ).sort_values('id')
    return ids

# Or
def article_views(views: pd.DataFrame) -> pd.DataFrame:
    ids = (
        views
        .loc[views['author_id'] == views['viewer_id'], ['author_id']]
        .rename(columns={'author_id': 'id'})
        .drop_duplicates()
        .sort_values('id')
    )
    return ids