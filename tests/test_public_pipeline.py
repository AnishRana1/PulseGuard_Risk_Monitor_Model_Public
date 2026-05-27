from src.data_loader import load_demo_market_data
from src.feature_engineering import build_public_features
from src.model_pipeline import train_public_risk_model, score_risk_model
from src.overlay_backtest import run_public_overlay_backtest

def test_public_pipeline_runs_end_to_end():
    prices = load_demo_market_data("AAPL", rows=400)
    features, target, names = build_public_features(prices)
    model, holdout = train_public_risk_model(features, target, names)
    scored = score_risk_model(model, holdout)
    backtest, metrics = run_public_overlay_backtest(prices.loc[scored.index], scored)
    assert not features.empty
    assert set(["probability", "prediction"]).issubset(scored.columns)
    assert "overlay_return_pct" in metrics
    assert not backtest.empty
