def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather.sort_values('recordDate', inplace=True)
    weather['higher'] = weather['temperature'] > weather['temperature'].shift(1)
    weather['ddiff'] = (weather['recordDate'] - weather['recordDate'].shift(1)).dt.days
    keep_mask = weather['higher'] & (weather['ddiff'] == 1)
    result = weather.loc[keep_mask, ['id']]
    return result

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    result = (
        weather
        .sort_values('recordDate')
        .assign(
            higher = lambda df: df['temperature'] > df['temperature'].shift(1),
            ddiff = lambda df: (df['recordDate'] - df['recordDate'].shift(1)).dt.days
        )
        .loc[lambda df: df['higher'] & (df['ddiff'] == 1), ['id']]
    )
    return result