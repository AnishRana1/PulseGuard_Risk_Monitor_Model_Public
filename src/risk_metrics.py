from __future__ import annotations
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, fbeta_score, roc_auc_score

def classification_summary(y_true, y_pred, y_prob) -> pd.DataFrame:
    try:
        auc = roc_auc_score(y_true, y_prob)
    except ValueError:
        auc = np.nan
    rows = {
        "Accuracy": accuracy_score(y_true, y_pred),
        "Precision": precision_score(y_true, y_pred, zero_division=0),
        "Recall": recall_score(y_true, y_pred, zero_division=0),
        "F2-score": fbeta_score(y_true, y_pred, beta=2, zero_division=0),
        "AUC-ROC": auc,
    }
    return pd.DataFrame({"metric": rows.keys(), "value": rows.values()})

def max_drawdown(equity_curve: pd.Series) -> float:
    peak = equity_curve.cummax()
    drawdown = equity_curve / peak - 1.0
    return float(drawdown.min())
