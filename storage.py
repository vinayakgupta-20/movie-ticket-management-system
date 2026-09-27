import json
import os

DATA_FOLDER = "data"

def load_data(file_name):
    path = os.path.join(DATA_FOLDER, file_name)

    if not os.path.exists(path):
        return []

    try:
        with open(path, "r") as f:
            data = json.load(f)
            return data
    except (json.JSONDecodeError, ValueError):
        return []

def save_data(file_name, data):
    if not os.path.exists(DATA_FOLDER):
        os.makedirs(DATA_FOLDER)

    path = os.path.join(DATA_FOLDER, file_name)
    with open(path, "w") as f:
        json.dump(data, f, indent=4)