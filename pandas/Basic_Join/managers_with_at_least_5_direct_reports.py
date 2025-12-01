def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    managers_reports = employee.groupby('managerId', as_index=False)['id'].size()
    managers_ge_5_reports = managers_reports.loc[managers_reports['size'] >= 5]

    merged_df = managers_ge_5_reports.merge(employee, left_on='managerId', right_on='id', how='inner')
    managers_name = merged_df[['name']]
    return managers_name

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    results = (
        employee
        .groupby('managerId', as_index=False)['id'].size()
        .merge(employee, left_on='managerId', right_on='id', how='inner')
        .loc[lambda df: df['size'] >= 5, ['name']]
    )
    return results