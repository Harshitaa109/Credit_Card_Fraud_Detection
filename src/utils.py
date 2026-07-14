# src/utils.py

import joblib


def save_object(obj, filepath):
    """
    Save Python object
    """
    joblib.dump(obj, filepath)


def load_object(filepath):
    """
    Load Python object
    """
    return joblib.load(filepath)