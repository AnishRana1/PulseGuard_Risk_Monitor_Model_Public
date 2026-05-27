"""
Public Streamlit application structure for PulseGuard Crash Risk Monitor.

This file is intentionally a readable scaffold rather than the production
application. The deployed version at https://crash-monitor.streamlit.app uses a
larger private app with production caching, full optimisation controls,
walk-forward calibration, result downloads and deployment-specific state logic.

Recruiters can use this file to understand how the original long app is
organised conceptually without receiving the exact implementation.
"""

import streamlit as st

from app.page_overview import render_overview_page
from app.page_model import render_model_page
from app.page_backtest import render_backtest_page


def configure_page() -> None:
    """Apply high-level Streamlit configuration used by the public scaffold."""
    st.set_page_config(page_title="PulseGuard Crash Risk Monitor Codebase Scaffold", layout="wide")


def render_sidebar() -> str:
    """Render public navigation controls and return the selected page name."""
    pages = ["Overview", "Model pipeline", "Simulation/backtest"]
    st.sidebar.title("PulseGuard Crash Risk Monitor")
    st.sidebar.caption("Public code-reading scaffold")
    selected_page = st.sidebar.radio("Section", pages)
    st.sidebar.divider()
    st.sidebar.info(
        "This repository is designed for recruiter code review. It explains the "
        "simulation architecture but withholds cloneable production internals."
    )
    return selected_page


def main() -> None:
    """Entry point for the public scaffold."""
    configure_page()
    selected_page = render_sidebar()

    page_renderers = {
        "Overview": render_overview_page,
        "Model pipeline": render_model_page,
        "Simulation/backtest": render_backtest_page,
    }
    page_renderers[selected_page]()


if __name__ == "__main__":
    main()
