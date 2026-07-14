import shap
import joblib
import pandas as pd

from src.config import BEST_MODEL_PATH


class ExplainPrediction:

    def __init__(self):

        # Load trained model
        self.model = joblib.load(BEST_MODEL_PATH)

        # SHAP Tree Explainer
        self.explainer = shap.TreeExplainer(self.model)


    # ----------------------------------
    # Individual prediction explanation
    # ----------------------------------

    def explain(self, sample):

        shap_values = self.explainer.shap_values(sample)

        # Binary classification:
        # Select fraud class explanation
        if isinstance(shap_values, list):
            shap_values = shap_values[1]

        explanation = pd.DataFrame({

            "Feature": sample.columns,

            "Impact": shap_values[0]

        })


        explanation["Abs_Impact"] = (
            explanation["Impact"]
            .abs()
        )


        explanation = explanation.sort_values(
            by="Abs_Impact",
            ascending=False
        )


        return explanation



    # ----------------------------------
    # Model feature importance
    # ----------------------------------

    def feature_importance(self):

        importance = pd.DataFrame({

            "Feature":
            self.model.feature_names_in_,


            "Importance":
            self.model.feature_importances_

        })


        importance = importance.sort_values(

            by="Importance",

            ascending=False

        )


        return importance



    # ----------------------------------
    # SHAP Global Importance
    # ----------------------------------

    def shap_feature_importance(self, X):

        """
        Calculates global feature importance
        using SHAP values
        """


        shap_values = self.explainer.shap_values(X)


        # Binary classifier handling

        if isinstance(shap_values, list):

            shap_values = shap_values[1]


        importance = pd.DataFrame({

            "Feature":
            X.columns,


            "Importance":
            abs(shap_values).mean(axis=0)

        })


        importance = importance.sort_values(

            by="Importance",

            ascending=False

        )


        return importance