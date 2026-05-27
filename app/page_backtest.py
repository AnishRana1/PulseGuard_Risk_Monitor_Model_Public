import streamlit as st

from src.data_loader import load_demo_market_data
from src.feature_engineering import build_public_features
from src.model_pipeline import train_public_risk_model, score_risk_model
from src.overlay_backtest import run_public_overlay_backtest
from src.visualisation import plot_equity_curves, plot_exposure_trace


def render_backtest_page() -> None:
    st.title("Overlay Backtest Demonstration")
    ticker = st.selectbox("Demo ticker", ["AAPL", "MSFT", "NVDA", "SPY"], key="bt_ticker")
    threshold = st.slider("Risk probability threshold", 0.10, 0.90, 0.50, 0.05)

    prices = load_demo_market_data(ticker=ticker, rows=650)
    features, target, feature_names = build_public_features(prices)
    model, holdout = train_public_risk_model(features, target, feature_names)
    scored = score_risk_model(model, holdout, threshold=threshold)
    backtest, metrics = run_public_overlay_backtest(prices.loc[scored.index], scored)

    c1, c2, c3 = st.columns(3)
    c1.metric("Buy-and-hold return", f"{metrics['buy_hold_return_pct']:.1f}%")
    c2.metric("Overlay return", f"{metrics['overlay_return_pct']:.1f}%")
    c3.metric("Max drawdown reduction", f"{metrics['max_drawdown_reduction_pct']:.1f}%")

    st.plotly_chart(plot_equity_curves(backtest), use_container_width=True)
    st.plotly_chart(plot_exposure_trace(backtest), use_container_width=True)

    st.caption(
        "This is a simplified demonstration. The private app contains the fuller "
        "return-constrained overlay and optimisation workflow."
    )
