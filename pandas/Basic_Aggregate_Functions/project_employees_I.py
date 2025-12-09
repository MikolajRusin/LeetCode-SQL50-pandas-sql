def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    merged_df = project.merge(employee, on='employee_id', how='left')
    avg_year = merged_df.groupby('project_id', as_index=False)['experience_years'].mean().round(2)
    avg_year.rename(columns={'experience_years': 'average_years'}, inplace=True)
    return avg_year

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    results = (
        project
        .merge(employee, on='employee_id', how='left')
        .groupby('project_id', as_index=False)['experience_years'].mean().round(2)
        .rename(columns={'experience_years': 'average_years'})
    )
    return results