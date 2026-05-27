from __future__ import annotations
import numpy as np
import pandas as pd

PUBLIC_FEATURES = [
    "return_1d", "return_5d", "return_20d",
    "volatility_10d", "volatility_20d",
    "drawdown", "drawdown_speed",
    "range_pct", "volume_zscore",
    "ma_gap_20d", "momentum_regime",
]

def build_public_features(prices: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series, list[str]]:
    """Build a compact public subset of the private feature pipeline.

    The private implementation contains a fuller 14-feature risk set and additional
    production checks. This version preserves the modelling shape while avoiding a
    complete code clone of the deployed pipeline.
    """
    df = prices.copy()
    close = df["Close"]
    returns = close.pct_change()
    df["return_1d"] = returns
    df["return_5d"] = close.pct_change(5)
    df["return_20d"] = close.pct_change(20)
    df["volatility_10d"] = returns.rolling(10).std() * np.sqrt(252)
    df["volatility_20d"] = returns.rolling(20).std() * np.sqrt(252)
    running_peak = close.cummax()
    df["drawdown"] = close / running_peak - 1.0
    df["drawdown_speed"] = df["drawdown"].diff(5)
    df["range_pct"] = (df["High"] - df["Low"]) / df["Close"]
    volume_mean = df["Volume"].rolling(20).mean()
    volume_std = df["Volume"].rolling(20).std().replace(0, np.nan)
    df["volume_zscore"] = (df["Volume"] - volume_mean) / volume_std
    ma20 = close.rolling(20).mean()
    ma60 = close.rolling(60).mean()
    df["ma_gap_20d"] = close / ma20 - 1.0
    df["momentum_regime"] = ma20 / ma60 - 1.0
    downside_cutoff = returns.rolling(80).quantile(0.20)
    target = (returns.shift(-1) < downside_cutoff).astype(int)
    features = df[PUBLIC_FEATURES].replace([np.inf, -np.inf], np.nan).dropna()
    target = target.loc[features.index]
    return features.iloc[:-1], target.iloc[:-1], PUBLIC_FEATURES.copy()
