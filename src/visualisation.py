from __future__ import annotations
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def plot_probability_trace(scored: pd.DataFrame):
    fig = px.line(scored, y="probability", title="Risk probability trace")
    fig.add_hline(y=0.5, line_dash="dash", annotation_text="demo threshold")
    return fig

def plot_feature_importance(model, feature_names: list[str]):
    classifier = model.named_steps["classifier"]
    frame = pd.DataFrame({"feature": feature_names, "importance": classifier.feature_importances_})
    frame = frame.sort_values("importance", ascending=True)
    return px.bar(frame, x="importance", y="feature", orientation="h", title="Demo feature importance")

def plot_equity_curves(backtest: pd.DataFrame):
    fig = go.Figure()
    fig.add_scatter(x=backtest.index, y=backtest["buy_hold_equity"], mode="lines", name="Buy-and-hold")
    fig.add_scatter(x=backtest.index, y=backtest["overlay_equity"], mode="lines", name="Risk overlay")
    fig.update_layout(title="Equity curve comparison", yaxis_title="Growth of £1")
    return fig

def plot_exposure_trace(backtest: pd.DataFrame):
    fig = px.line(backtest, y="exposure", title="Risk-managed exposure")
    fig.update_yaxes(range=[0, 1.05])
    return fig
