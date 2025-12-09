def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    ROUND_CORRECTION = 1e-9

    results = (
        queries
        .assign(
            poor=lambda df: df['rating'] < 3,
            ratio=lambda df: df['rating'] / df['position']
        )
        .groupby('query_name', as_index=False)
        .agg(
            quality=('ratio', lambda x: x.mean() + ROUND_CORRECTION),
            poor_query_percentage=('poor', lambda x: (sum(x) / x.shape[0]) * 100)
        )
        .round({'quality': 2, 'poor_query_percentage': 2})
    )
    return results

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    ROUND_CORRECTION = 1e-9

    results = (
        queries
        .assign(
            quality=lambda df: df['rating'] / df['position'],
            poor_query_percentage=lambda df: (df['rating'] < 3).astype(int) * 100
        )
        .groupby('query_name')[['quality', 'poor_query_percentage']].mean()
        .apply(lambda x: round(x + ROUND_CORRECTION, 2))
        .reset_index()
    )
    return results