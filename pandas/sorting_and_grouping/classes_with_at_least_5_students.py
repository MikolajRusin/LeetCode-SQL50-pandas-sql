def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    result = (
        courses
        .groupby('class', as_index=False)['student'].nunique()
        .loc[lambda x: x['student'] >= 5, ['class']]
    )
    return result