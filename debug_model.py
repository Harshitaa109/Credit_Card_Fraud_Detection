import shap
import joblib
import pandas as pd

from src.config import BEST_MODEL_PATH, DATA_PATH


# -----------------------------
# Load trained model
# -----------------------------

print("Loading model...")

model = joblib.load(BEST_MODEL_PATH)


# -----------------------------
# Load dataset
# -----------------------------

print("Loading dataset...")

df = pd.read_csv(DATA_PATH)


# Remove target column

X = df.drop("Class", axis=1)


# Take sample for SHAP calculation
# (Full dataset can be slow)

X_sample = X.sample(
    5000,
    random_state=42
)


# -----------------------------
# Create SHAP Explainer
# -----------------------------

print("Creating SHAP explainer...")

explainer = shap.TreeExplainer(model)


# Calculate SHAP values

print("Calculating SHAP values...")

shap_values = explainer.shap_values(X_sample)



# -----------------------------
# Handle binary classification
# -----------------------------

if isinstance(shap_values, list):

    # Fraud class
    shap_values = shap_values[1]



# -----------------------------
# Create feature importance
# -----------------------------

importance = pd.DataFrame({

    "Feature": X.columns,

    "Importance":
        abs(shap_values).mean(axis=0)

})


importance = importance.sort_values(
    by="Importance",
    ascending=False
)



# -----------------------------
# Save CSV
# -----------------------------

output_path = "reports/shap_importance.csv"


importance.to_csv(
    output_path,
    index=False
)


print("\nSHAP importance created successfully!")
print(f"Saved at: {output_path}")

print("\nTop 10 Fraud Influencing Features:")
print(importance.head(10))