"""Pseudocode for private cache strategy.

The deployed app uses caching so UI controls do not retrain models unnecessarily.
This public module explains the pattern without exposing exact cache internals.
"""

CACHE_POLICY_PSEUDOCODE = r'''
construct cache_key from:
    ticker
    data_end_date
    lookback_period
    feature_config
    model_hyperparameters
    threshold_config
    optimisation_version

if user changes only chart controls:
    reuse cached predictions and backtest tables

if user edits portfolio/exposure display controls only:
    reuse cached model output
    recompute lightweight display tables only

if user changes modelling inputs:
    invalidate only affected model cache entry

if user clicks Retrain model:
    overwrite current cache_key artefact

if user clicks Run full optimisation:
    run coarse-to-fine search
    write optimisation table
    update optimised defaults
    write new cache bundle

persist cache metadata:
    creation timestamp
    code version
    data cutoff
    model configuration
    deterministic environment notes
'''
