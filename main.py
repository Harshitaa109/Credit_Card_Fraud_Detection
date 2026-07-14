from src.train_model import train_models
from src.evaluate_model import evaluate_saved_model

print("=" * 60)
print("Training Models")
print("=" * 60)

train_models()

print("\n")

print("=" * 60)
print("Evaluating Best Model")
print("=" * 60)

evaluate_saved_model()