import pandas as pd
from src.predict import FraudPredictor

print("Loading model...")

predictor = FraudPredictor()

print("Loading dataset...")

df = pd.read_csv("data/creditcard.csv")

print("Dataset Shape:")
print(df.shape)

print("Starting prediction...")

result = predictor.predict(df)

print("\nPrediction completed successfully!")

print("\nResult Shape:")
print(result.shape)

print("\nFirst 5 Rows:")
print(result.head())

print("\nLast 5 Rows:")
print(result.tail())