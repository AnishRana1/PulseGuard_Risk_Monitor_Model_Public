import streamlit as st

from src.data_loader import load_demo_market_data
from src.feature_engineering import build_public_features
from src.model_pipeline import train_public_risk_model, score_risk_model
from src.risk_metrics import classification_summary
from src.visualisation import plot_probability_trace, plot_feature_importance


def render_model_page() -> None:
    st.title("Model Pipeline Demonstration")
    ticker = st.selectbox("Demo ticker", ["AAPL", "MSFT", "NVDA", "SPY"])
    rows = st.slider("Demo observations", min_value=250, max_value=900, value=500, step=50)

    prices = load_demo_market_data(ticker=ticker, rows=rows)
    features, target, feature_names = build_public_features(prices)
    model, holdout = train_public_risk_model(features, target, feature_names)
    scored = score_risk_model(model, holdout)
    summary = classification_summary(scored["y_true"], scored["prediction"], scored["probability"])

    st.subheader("Simplified classification metrics")
    st.dataframe(summary, use_container_width=True)

    left, right = st.columns(2)
    with left:
        st.plotly_chart(plot_probability_trace(scored), use_container_width=True)
    with right:
        st.plotly_chart(plot_feature_importance(model, feature_names), use_container_width=True)

    st.caption(
        "The deployed/private implementation uses fuller model selection, "
        "threshold calibration and cached optimisation results."
    )
