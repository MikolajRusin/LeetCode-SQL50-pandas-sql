def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    students_subject = students.merge(subjects, how='cross')
    n_times_attended = examinations.groupby(['student_id', 'subject_name'], as_index=False)['subject_name'].size()
    n_times_attended.rename(columns={'size': 'attended_exams'}, inplace=True)
    merged_df = students_subject.merge(n_times_attended, on=['student_id', 'subject_name'], how='left')
    merged_df['attended_exams'] = merged_df['attended_exams'].fillna(0)
    merged_df.sort_values(['student_id', 'subject_name'], inplace=True)
    return merged_df

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    n_times_attended = (
        examinations
        .groupby(['student_id', 'subject_name'], as_index=False)['subject_name'].size()
        .rename(columns={'size': 'attended_exams'})
    )

    result = (
        students
        .merge(subjects, how='cross')
        .merge(n_times_attended, on=['student_id', 'subject_name'], how='left')
        .fillna({'attended_exams': 0})
        .sort_values(['student_id', 'subject_name'])
    )
    return result