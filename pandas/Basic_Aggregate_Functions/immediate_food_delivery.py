def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    first_order_date = delivery.groupby('customer_id')['order_date'].transform('min')

    is_first_order = delivery['order_date'] == first_order_date
    is_immediate_order = delivery['order_date'] == delivery['customer_pref_delivery_date']

    n_customers = delivery.loc[is_first_order, 'customer_id'].nunique()
    n_immediate_first_orders = delivery.loc[is_first_order & is_immediate_order, 'customer_id'].nunique()
    percentage = round((n_immediate_first_orders / n_customers) * 100, 2)
    return pd.DataFrame({'immediate_percentage': [percentage]})