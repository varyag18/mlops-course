import pandas as pd
# Нужно сделать отстут не на 1, а на 2 строки. Это правило используется перед декларироваинем функции или класса.

def load_data(path):
    return pd.read_csv(path)
# Нужно сделать отстут не на 1, а на 2 строки. Это правило используется перед декларироваинем функции или класса.
def split_data(data):
    from sklearn.model_selection import train_test_split
    features = data.drop('fare_amount', axis=1)
    target = data['fare_amount']
    return train_test_split(features, target, test_size=0.2)
