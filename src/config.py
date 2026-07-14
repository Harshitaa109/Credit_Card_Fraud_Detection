# src/config.py

from pathlib import Path

# Project Root
BASE_DIR = Path(__file__).resolve().parent.parent

# Paths
DATA_PATH = BASE_DIR / "data" / "creditcard.csv"

MODEL_DIR = BASE_DIR / "models"

IMAGE_DIR = BASE_DIR / "images"

REPORT_DIR = BASE_DIR / "reports"

# Model Files
# Output Files
METRICS_PATH = MODEL_DIR / "model_metrics.csv"

BEST_MODEL_PATH = MODEL_DIR / "best_model.pkl"
SCALER_PATH = MODEL_DIR / "scaler.pkl"
CLASSIFICATION_REPORT_PATH = REPORT_DIR/"classification_report.csv"
FEATURE_IMPORTANCE_PATH = REPORT_DIR / "feature_importance.csv"
# Random Seed
RANDOM_STATE = 42

# Test Size
TEST_SIZE = 0.20