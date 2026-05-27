# Detailed pseudocode walkthrough

This document gives recruiters enough technical detail to understand the private implementation approach without exposing the full implementation.

## Coarse-to-fine optimisation

```text
INPUT: ticker universe, selected display ticker, date cutoff, model search space,
       threshold search space, overlay search space, scoring constraints

1. Force the selected display ticker into the optimisation universe.
2. Freeze the market data window to the reproducibility cutoff.
3. Generate coarse candidates across broad hyperparameter ranges.
4. For each candidate:
   a. Build features using only information available at each time step.
   b. Train on past-only windows.
   c. Predict future validation segments.
   d. Compute classification metrics.
   e. Simulate overlay returns and drawdown.
   f. Store diagnostics in an optimisation table.
5. Rank candidates using a constrained objective:
   - reward AUC, recall, F2 and drawdown reduction;
   - penalise unstable ticker-level performance;
   - penalise excessive false positives;
   - reject candidates that only improve return through overfitting.
6. Build a narrower fine-search region around the best coarse candidates.
7. Rerun evaluation with higher resolution.
8. Export best parameters and full results table.
9. Update UI defaults and cache the selected model bundle.
```

## Walk-forward threshold calibration

```text
for fold in chronological_validation_folds:
    train model on observations before fold.start
    predict probabilities inside fold
    for threshold in threshold_grid:
        labels = probabilities >= threshold
        compute precision, recall, F2, AUC, event count
        run overlay using those labels
        compute return, drawdown and turnover diagnostics
    select threshold that maximises recall/F2 under precision and return constraints
combine fold-level thresholds robustly
return final threshold and diagnostics
```

## Cache invalidation

```text
if modelling inputs change:
    invalidate model cache
elif only graph controls change:
    reuse cached predictions
elif only portfolio display changes:
    reuse cached model output and recompute lightweight tables
elif user explicitly clicks retrain:
    overwrite current cache bundle
elif user runs optimisation:
    write new optimisation table and update optimised defaults
```
