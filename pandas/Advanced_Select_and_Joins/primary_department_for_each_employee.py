def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    emp_Y_dep = employee.loc[employee['primary_flag'] == 'Y']
    emp_1_dep = employee.loc[employee.groupby('employee_id')['department_id'].transform('nunique') == 1]

    return pd.concat((emp_Y_dep, emp_1_dep), axis=0)[['employee_id', 'department_id']]

#OR
def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee['n_dep'] = employee.groupby('employee_id')['department_id'].transform('count')
    return employee.loc[
        (employee['n_dep'] == 1) | (employee['primary_flag'] == 'Y'), 
        ['employee_id', 'department_id']
        ]