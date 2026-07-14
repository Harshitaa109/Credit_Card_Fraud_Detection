# src/evaluate_model.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.metrics import (
    confusion_matrix,
    ConfusionMatrixDisplay,
    classification_report,
    roc_curve,
    auc,
    precision_recall_curve,
)

from src.data_preprocessing import preprocess_data
from src.utils import load_object
from src.config import (
    BEST_MODEL_PATH,
    IMAGE_DIR,
    REPORT_DIR,
)


def evaluate_saved_model():

    # Load processed data
    X_train, X_test, y_train, y_test, scaler = preprocess_data()

    # Load best model
    model = load_object(BEST_MODEL_PATH)

    # Predictions
    y_pred = model.predict(X_test)

    y_prob = model.predict_proba(X_test)[:, 1]

    # -----------------------------
    # Classification Report
    # -----------------------------
    report = classification_report(
        y_test,
        y_pred,
        output_dict=True,
    )

    report_df = pd.DataFrame(report).transpose()

    report_df.to_csv(
        REPORT_DIR / "classification_report.csv"
    )

    print(classification_report(y_test, y_pred))

    # -----------------------------
    # Confusion Matrix
    # -----------------------------
    cm = confusion_matrix(y_test, y_pred)

    plt.figure(figsize=(6, 5))

    sns.heatmap(
        cm,
        annot=True,
        fmt="d",
        cmap="Blues"
    )

    plt.title("Confusion Matrix")

    plt.xlabel("Predicted")

    plt.ylabel("Actual")

    plt.savefig(
        IMAGE_DIR / "confusion_matrix.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # -----------------------------
    # ROC Curve
    # -----------------------------
    fpr, tpr, _ = roc_curve(
        y_test,
        y_prob
    )

    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=(7, 6))

    plt.plot(
        fpr,
        tpr,
        label=f"AUC = {roc_auc:.4f}"
    )

    plt.plot([0, 1], [0, 1], "--")

    plt.xlabel("False Positive Rate")

    plt.ylabel("True Positive Rate")

    plt.title("ROC Curve")

    plt.legend()

    plt.savefig(
        IMAGE_DIR / "roc_curve.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # -----------------------------
    # Precision Recall Curve
    # -----------------------------
    precision, recall, _ = precision_recall_curve(
        y_test,
        y_prob
    )

    plt.figure(figsize=(7, 6))

    plt.plot(
        recall,
        precision
    )

    plt.xlabel("Recall")

    plt.ylabel("Precision")

    plt.title("Precision-Recall Curve")

    plt.savefig(
        IMAGE_DIR / "pr_curve.png",
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    # -----------------------------
    # Feature Importance
    # -----------------------------
    if hasattr(model, "feature_importances_"):

        importance = pd.Series(
            model.feature_importances_,
            index=X_test.columns
        )

        importance = importance.sort_values(
            ascending=False
        )

        plt.figure(figsize=(10, 8))

        importance.head(15).plot.barh()

        plt.title("Top 15 Feature Importance")

        plt.savefig(
            IMAGE_DIR / "feature_importance.png",
            dpi=300,
            bbox_inches="tight"
        )

        plt.close()

    print("\nEvaluation completed successfully.")


if __name__ == "__main__":

    evaluate_saved_model()