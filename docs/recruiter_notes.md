# Recruiter notes

This repository is designed to be reviewed alongside the live deployed app.

## Why the code is intentionally incomplete

The full project contains original optimisation, caching, calibration and deployment logic. Making all of that public would make the project easy to clone or submit elsewhere. This repository therefore demonstrates engineering ability while keeping the production implementation private.

## What to look at first

1. `README.md` for project positioning.
2. `app/app_demo.py` for the cleaned Streamlit entry point.
3. `src/feature_engineering.py` for representative feature construction.
4. `src/model_pipeline.py` for the simplified modelling pipeline.
5. `src/optimisation_pseudocode.py` and `docs/pseudocode_walkthrough.md` for the withheld optimisation logic.

## Suggested interview walkthrough

- Explain the original long-app problem and why the public version was modularised.
- Walk through data loading, feature generation, model fitting and overlay simulation.
- Discuss how private walk-forward threshold optimisation avoids look-ahead bias.
- Show the deployed Streamlit app to demonstrate the fuller implementation.
