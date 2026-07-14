# src/data_preprocessing.py

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from imblearn.over_sampling import SMOTE

from src.config import (
    DATA_PATH,
    TEST_SIZE,
    RANDOM_STATE
)


def load_dataset():

    df = pd.read_csv(DATA_PATH)

    return df


def preprocess_data():

    df = load_dataset()

    X = df.drop("Class", axis=1)

    y = df["Class"]

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE,
        stratify=y,
    )

    scaler = StandardScaler()

    X_train[["Time", "Amount"]] = scaler.fit_transform(
        X_train[["Time", "Amount"]]
    )

    X_test[["Time", "Amount"]] = scaler.transform(
        X_test[["Time", "Amount"]]
    )

    smote = SMOTE(random_state=RANDOM_STATE)

    X_train_smote, y_train_smote = smote.fit_resample(
        X_train,
        y_train,
    )

    return (
        X_train_smote,
        X_test,
        y_train_smote,
        y_test,
        scaler,
    )