import json
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import pickle

def load_config():
    with open("config.json") as f:
        return json.load(f)

def load_data(path):
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        return None

def preprocess(data, config):
    if data is None:
        return None, None
    data = data.dropna()
    X = data[config['features']]
    y = data[config['target_column']]
    return X, y

def train(X, y, params):
    if X is None or y is None:
        return None
    model = RandomForestRegressor(**params)
    model.fit(X, y)
    return model

def save_model(model, path):
    if model is not None:
        with open(path, "wb") as f:
            pickle.dump(model, f)

def main():
    config = load_config()
    data = load_data(config["data_path"])
    X, y = preprocess(data, config)
    
    if X is not None and y is not None:
        X_train, _, y_train, _ = train_test_split(X, y, random_state=config['model_params']['random_state'])
        model = train(X_train, y_train, config["model_params"])
        save_model(model, config["output_path"])
        print("Model saved successfully")

if __name__ == "__main__":
    main()
