def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = employee.merge(bonus, on='empId', how='left')
    keep_mask = merged_df['bonus'].isna() | (merged_df['bonus'] < 1000)
    result = merged_df.loc[keep_mask, ['name', 'bonus']]
    return result

def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    result = (
        employee
        .merge(bonus, on='empId', how='left')
        .query('bonus.isna() | bonus < 1000')
        .loc[:, ['name', 'bonus']]
    )
    return result