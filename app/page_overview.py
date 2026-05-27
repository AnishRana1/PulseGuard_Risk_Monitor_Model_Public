import streamlit as st


def render_overview_page() -> None:
    st.title("PulseGuard Crash Risk Monitor: Market Risk Monitoring Showcase")
    st.warning(
        "This is a public-facing showcase version. The full production app, "
        "optimisation logic, model cache and deployment code are intentionally withheld."
    )

    st.markdown(
        """
        PulseGuard Crash Risk Monitor is a deployed Streamlit dashboard for market-risk forecasting and
        overlay simulation. The private app uses real OHLCV market data, engineered
        risk features, supervised ML classifiers and anomaly baselines.

        This showcase repository focuses on code organisation and methodology rather
        than exposing the full implementation.
        """
    )

    c1, c2, c3 = st.columns(3)
    c1.metric("Feature families", "Volatility / Momentum / Drawdown")
    c2.metric("Baseline comparison", "Z-Score + Isolation Forest")
    c3.metric("Deployment", "Streamlit")

    st.subheader("Public architecture")
    st.image("docs/diagrams/architecture_flow.png", use_container_width=True)

    st.subheader("What recruiters can inspect")
    st.markdown(
        """
        - modular data, feature, model, risk and visualisation components;
        - simplified but runnable demonstration pipeline;
        - detailed pseudocode for sensitive optimisation and caching routines;
        - documentation explaining which parts are private and why.
        """
    )
