from __future__ import annotations
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

def train_public_risk_model(features: pd.DataFrame, target: pd.Series, feature_names: list[str]):
    """Train a compact public demonstration classifier.

    The private app uses a fuller ensemble, walk-forward logic and optional
    optimisation. This public implementation is intentionally small and readable.
    """
    split = int(len(features) * 0.72)
    X_train, X_test = features.iloc[:split], features.iloc[split:]
    y_train, y_test = target.iloc[:split], target.iloc[split:]
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("classifier", RandomForestClassifier(n_estimators=80, max_depth=5, random_state=42, class_weight="balanced")),
    ])
    model.fit(X_train[feature_names], y_train)
    return model, {"X": X_test[feature_names], "y": y_test}

def score_risk_model(model, holdout: dict, threshold: float = 0.50) -> pd.DataFrame:
    probabilities = model.predict_proba(holdout["X"])[:, 1]
    prediction = (probabilities >= threshold).astype(int)
    return pd.DataFrame({"y_true": holdout["y"], "probability": probabilities, "prediction": prediction}, index=holdout["X"].index)
