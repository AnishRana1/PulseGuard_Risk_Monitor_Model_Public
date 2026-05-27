from __future__ import annotations
import pandas as pd
from src.risk_metrics import max_drawdown

def exposure_from_probability(probability: pd.Series) -> pd.Series:
    """Simplified exposure policy for public demonstration.

    Private version uses more nuanced risk tiers and return constraints.
    """
    exposure = pd.Series(1.0, index=probability.index)
    exposure[probability >= 0.50] = 0.55
    exposure[probability >= 0.70] = 0.25
    return exposure

def run_public_overlay_backtest(prices: pd.DataFrame, scored: pd.DataFrame) -> tuple[pd.DataFrame, dict]:
    returns = prices["Close"].pct_change().fillna(0.0).clip(-0.95, 0.95)
    exposure = exposure_from_probability(scored["probability"])
    overlay_returns = returns * exposure.shift(1).fillna(1.0)
    output = pd.DataFrame(index=scored.index)
    output["buy_hold_equity"] = (1 + returns).cumprod()
    output["overlay_equity"] = (1 + overlay_returns).cumprod()
    output["exposure"] = exposure
    output["risk_probability"] = scored["probability"]
    bh_return = (output["buy_hold_equity"].iloc[-1] - 1) * 100
    ov_return = (output["overlay_equity"].iloc[-1] - 1) * 100
    bh_dd = max_drawdown(output["buy_hold_equity"])
    ov_dd = max_drawdown(output["overlay_equity"])
    dd_reduction = (abs(bh_dd) - abs(ov_dd)) / max(abs(bh_dd), 1e-9) * 100
    return output, {"buy_hold_return_pct": float(bh_return), "overlay_return_pct": float(ov_return), "max_drawdown_reduction_pct": float(dd_reduction)}
