def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = (
        employees
        .set_index('id')
        .join(employee_uni.set_index('id'), on='id', how='left')
        .loc[:, ['unique_id', 'name']]
    )
    return result

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    result = (
        employees
        .merge(employee_uni, on='id', how='left')
        .loc[:, ['unique_id', 'name']]
    )
    return result