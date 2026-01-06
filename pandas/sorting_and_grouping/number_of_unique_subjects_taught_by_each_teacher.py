def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    results = (
        teacher
        .groupby('teacher_id', as_index=False)['subject_id'].nunique()
        .rename(columns={'subject_id': 'cnt'})
    )
    return results