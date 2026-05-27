from __future__ import annotations
import hashlib
import numpy as np
import pandas as pd

def _seed_from_ticker(ticker: str) -> int:
    digest = hashlib.sha256(ticker.upper().encode()).hexdigest()
    return int(digest[:8], 16)

def load_demo_market_data(ticker: str = "AAPL", rows: int = 500) -> pd.DataFrame:
    """Create deterministic OHLCV-like demo data.

    The private deployment uses real market data and optional frozen snapshots.
    Public showcase data is synthetic to avoid shipping cached source data.
    """
    rng = np.random.default_rng(_seed_from_ticker(ticker))
    index = pd.bdate_range(end=pd.Timestamp.today().normalize(), periods=rows)
    drift = 0.00045
    shock = rng.normal(loc=drift, scale=0.018, size=rows)
    regime = np.sin(np.linspace(0, 8 * np.pi, rows)) * 0.006
    returns = shock + regime
    close = 100 * np.exp(np.cumsum(returns))
    open_ = close * (1 + rng.normal(0, 0.003, rows))
    high = np.maximum(open_, close) * (1 + rng.uniform(0.001, 0.018, rows))
    low = np.minimum(open_, close) * (1 - rng.uniform(0.001, 0.018, rows))
    volume = rng.integers(1_000_000, 8_000_000, rows)
    return pd.DataFrame({"Open": open_, "High": high, "Low": low, "Close": close, "Volume": volume}, index=index)
