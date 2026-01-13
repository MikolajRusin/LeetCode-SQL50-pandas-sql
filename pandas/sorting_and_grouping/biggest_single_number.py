def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    result = (
        my_numbers
        .drop_duplicates(keep=False)
        .max()
        .to_frame(name='num')
    )
    return result