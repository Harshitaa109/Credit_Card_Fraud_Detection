import pandas as pd
from src.utils import load_object
from src.config import BEST_MODEL_PATH, SCALER_PATH

class FraudPredictor:
    def __init__(self):
        self.model = load_object(BEST_MODEL_PATH)
        self.scaler = load_object(SCALER_PATH)
        self.expected_columns = list(self.model.feature_names_in_)

    def preprocess(self, df):
        df = df.copy()
        df.columns = df.columns.str.strip()
        df.drop(columns=["Class"], errors="ignore", inplace=True)
        print("\nColumns AFTER dropping Class:")
        print(df.columns.tolist())
        df = df.reindex(columns=self.expected_columns)
        df["Time"] = pd.to_numeric(df["Time"])
        df["Amount"] = pd.to_numeric(df["Amount"])
        scaled = self.scaler.transform(df[["Time", "Amount"]])
        df["Time"] = scaled[:, 0]
        df["Amount"] = scaled[:, 1]
        return df

    def predict(self, df):
        processed_df = self.preprocess(df)
        print("\nColumns sent to model:")
        print(processed_df.columns.tolist())
        prediction = self.model.predict(processed_df)
        probability = self.model.predict_proba(processed_df)[:, 1]
        result = df.copy()
        result.drop(columns=["Class"], errors="ignore", inplace=True)
        result["Prediction"] = prediction
        result["Fraud Probability"] = probability.round(4)
        def risk(p):
            if p < 0.30:
                return "🟢 Low"
            elif p < 0.70:
                return "🟡 Medium"
            else:
                return "🔴 High"
        result["Risk Level"] = [risk(p) for p in probability]
        return result
