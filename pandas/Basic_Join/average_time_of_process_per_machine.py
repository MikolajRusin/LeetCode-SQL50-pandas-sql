def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_machines = activity.loc[activity['activity_type'] == 'start', ['machine_id', 'process_id', 'timestamp']]
    start_machines.rename(columns={'timestamp': 'start'}, inplace=True)
    end_machines = activity.loc[activity['activity_type'] == 'end', ['machine_id', 'process_id', 'timestamp']]
    end_machines.rename(columns={'timestamp': 'end'}, inplace=True)
    merged_df = start_machines.merge(end_machines, how='left', on=['machine_id', 'process_id'])
    merged_df['run_time'] = merged_df['end'] - merged_df['start']
    processing_time = merged_df.groupby('machine_id', as_index=False)['run_time'].mean().round(3)
    processing_time.rename(columns={'run_time': 'processing_time'}, inplace=True)
    return processing_time

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    start_machines = (
        activity
        .loc[activity['activity_type'] == 'start']
        .rename(columns={'timestamp': 'start'})
    )
    end_machines = (
        activity
        .loc[activity['activity_type'] == 'end']
        .rename(columns={'timestamp': 'end'})
    )

    result = (
        start_machines
        .merge(end_machines, on=['machine_id', 'process_id'], how='left')
        .assign(run_time=lambda df: df['end'] - df['start'])
        .groupby('machine_id', as_index=False)['run_time'].mean().round(3)
        .rename(columns={'run_time': 'processing_time'})
    )
    return result
