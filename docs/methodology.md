# Methodology

PulseGuard Crash Risk Monitor frames market-risk monitoring as a supervised risk-classification and overlay-evaluation problem.

## 1. Data layer

The private app uses real OHLCV data. This public version generates deterministic OHLCV-like data because shipping cached snapshots and generated artefacts would make the repository easier to copy.

## 2. Feature engineering

The public version includes a compact set of representative features:

- short- and medium-horizon returns;
- rolling annualised volatility;
- drawdown and drawdown speed;
- intraday range percentage;
- rolling volume anomaly;
- moving-average gap and momentum regime.

The private implementation contains a richer feature set and production checks.

## 3. Risk model

The public implementation trains a small Random Forest pipeline to demonstrate the classification workflow. The private version contains fuller ensemble logic, additional baseline comparison and threshold calibration.

## 4. Risk overlay

The public overlay reduces exposure as forecast risk probability rises. The private implementation uses more detailed risk tiers, transaction-cost handling and return-constrained optimisation.

## 5. Evaluation

The dashboard focuses on classification metrics and portfolio-style evaluation. Key metrics include AUC-ROC, precision, recall, F2-score, buy-and-hold return, overlay return and max drawdown reduction.
