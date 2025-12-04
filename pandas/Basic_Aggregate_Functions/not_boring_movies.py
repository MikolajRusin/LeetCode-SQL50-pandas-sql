def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    keep_mask = (cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')
    results = cinema.loc[keep_mask, :]
    results.sort_values('rating', ascending=False, inplace=True)
    return results

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    results = (
        cinema
        .loc[(cinema['id'] % 2 == 1) & (cinema['description'] != 'boring')]
        .sort_values('rating', ascending=False)
    )
    return results