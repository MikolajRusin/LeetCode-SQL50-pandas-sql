def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    reports_count = (
        employees
        .groupby('reports_to', as_index=False).agg(
            reports_count=('reports_to', 'count'),
            average_age=('age', 'mean')
        )
        .rename(columns={'reports_to': 'employee_id'})
    )

    result = (
        reports_count
        .merge(employees, how='left', on='employee_id')
        .assign(average_age=lambda df: (df['average_age'] + 1e-8).round(0))
        .sort_values(by='employee_id')
    )
    return result[['employee_id', 'name', 'reports_count', 'average_age']]