import os
import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
)

from src.data_preprocessing import preprocess_data
from src.utils import save_object

from src.config import (
    RANDOM_STATE,
    METRICS_PATH,
    BEST_MODEL_PATH,
    SCALER_PATH,
)


# ---------------------------------------------------------
# Evaluate Model
# ---------------------------------------------------------

def evaluate(model, X_test, y_test):

    prediction = model.predict(X_test)
    probability = model.predict_proba(X_test)[:, 1]

    return {
        "Accuracy": accuracy_score(y_test, prediction),
        "Precision": precision_score(y_test, prediction),
        "Recall": recall_score(y_test, prediction),
        "F1": f1_score(y_test, prediction),
        "ROC_AUC": roc_auc_score(y_test, probability),
    }


# ---------------------------------------------------------
# Train Models
# ---------------------------------------------------------

def train_models():

    print("=" * 70)
    print("Loading Dataset...")
    print("=" * 70)

    X_train, X_test, y_train, y_test, scaler = preprocess_data()

    os.makedirs("models", exist_ok=True)
    os.makedirs("reports", exist_ok=True)

    models = {

        "Logistic Regression":
        LogisticRegression(
            max_iter=1000,
            random_state=RANDOM_STATE
        ),

        "Decision Tree":
        DecisionTreeClassifier(
            random_state=RANDOM_STATE
        ),

        "Random Forest":
        RandomForestClassifier(
            n_estimators=200,
            random_state=RANDOM_STATE,
            n_jobs=-1
        )

    }

    results = []

    best_model = None
    best_score = -1
    best_name = ""

    # -------------------------------------------------

    for name, model in models.items():

        print(f"\nTraining {name}...")

        model.fit(X_train, y_train)

        metrics = evaluate(
            model,
            X_test,
            y_test
        )

        metrics["Model"] = name

        results.append(metrics)

        # Save every trained model
        filename = name.lower().replace(" ", "_") + ".pkl"

        save_object(
            model,
            os.path.join("models", filename)
        )

        print(metrics)

        if metrics["F1"] > best_score:

            best_score = metrics["F1"]

            best_model = model

            best_name = name

    # -------------------------------------------------

    results_df = pd.DataFrame(results)

    results_df = results_df[
        [
            "Model",
            "Accuracy",
            "Precision",
            "Recall",
            "F1",
            "ROC_AUC",
        ]
    ]

    results_df = results_df.sort_values(
        by="ROC_AUC",
        ascending=False
    )

    results_df.to_csv(
        METRICS_PATH,
        index=False
    )

    # -------------------------------------------------
    # Save Best Model
    # -------------------------------------------------

    save_object(
        best_model,
        BEST_MODEL_PATH
    )

    save_object(
        scaler,
        SCALER_PATH
    )

    print("\n" + "=" * 70)
    print("MODEL LEADERBOARD")
    print("=" * 70)

    print(results_df.to_string(index=False))

    print("\nBest Model :", best_name)
    print("Best F1 Score :", round(best_score, 4))

    # -------------------------------------------------
    # Save Feature Importance (Random Forest)
    # -------------------------------------------------

    if hasattr(best_model, "feature_importances_"):

        importance = pd.DataFrame({

            "Feature": X_train.columns,

            "Importance": best_model.feature_importances_

        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False
        )

        importance.to_csv(
            "reports/feature_importance.csv",
            index=False
        )

        print("\nFeature importance saved.")

    print("\nBest model saved successfully.")
    print("Scaler saved successfully.")
    print("Metrics saved successfully.")

    return results_df


# ---------------------------------------------------------

if __name__ == "__main__":

    train_models()