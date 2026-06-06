---
aliases: [Machine Learning, Supervised Learning, Unsupervised Learning, Deep Learning, Overfitting, Bias Error, Variance Error, Cross Validation, LASSO, Penalized Regression, SVM, KNN, CART, Random Forest, PCA, K-Means Clustering, Hierarchical Clustering, Neural Networks, Reinforcement Learning]
tags: [CFA-L2, quant, concept, machine-learning]
date: 2026-06-04
status: evergreen
source: Schweser Book 1, Reading 3 (Modules 3.1–3.3), LOS 3.a–3.d
---

# Machine Learning

## Overview (LOS 3.a)

ML uses algorithms to find patterns in data **without distributional assumptions**. It beats classical stats when there are **many variables (high dimension)** and **nonlinear** relationships.

| Term | Meaning |
|---|---|
| **Target variable** | the dependent (Y) variable — can be continuous, categorical, or ordinal |
| **Features** | the independent (X) variables |
| **Training dataset** | sample used to fit the model |
| **Hyperparameter** | model input **set by the researcher** (not learned) |

**Three learning types:**
- **Supervised** — uses **labeled** data (target defined). Tasks: **regression** (continuous target) and **classification** (categorical/ordinal — binary or multi-category). Multiple regression is supervised.
- **Unsupervised** — **no labeled** data / no target; the algorithm finds structure. Clustering, PCA.
- **Deep learning / reinforcement** — neural-network-based, for highly nonlinear tasks (image recognition, NLP). **Reinforcement learning** learns from its own output and prediction errors.

## Overfitting & Generalization (LOS 3.b)

**Overfitting**: too many features → the model mistakes **noise for signal** → high **in-sample R²** but poor **out-of-sample R²** (it doesn't *generalize*).

**Three data partitions:** (1) **training** (fit), (2) **validation** (tune), (3) **test** (evaluate on new data). Errors in training/validation are in-sample; test error is **out-of-sample**.

**Error decomposition:**

| Error | What it is | Driven by |
|---|---|---|
| **Bias error** | in-sample error from a **poor fit** (too simple) | high in **linear** models |
| **Variance error** | out-of-sample error from **overfitting** (too complex) | high in **nonlinear** models |
| **Base error** | residual error from random noise | irreducible |

As complexity rises, **bias error falls but variance error rises** → choose complexity that **minimizes total error**. A **learning curve** plots accuracy (1 − error) vs. training-sample size; a robust model's in- and out-of-sample error rates **converge** to the desired level.

**Fixing overfitting — two tools:**
1. **Complexity reduction** — impose a **penalty** that grows with the number of features, excluding features that don't improve out-of-sample accuracy.
2. **Cross validation** — estimate out-of-sample error from the validation sample. In **k-fold CV**, split the sample into k equal parts; train on k−1, validate on 1; repeat k times and average the error rates.

## Supervised Algorithms (LOS 3.c)

- **Penalized regression / LASSO** (regression): minimize SSE **+ penalty**; LASSO adds Σ\|slopes\|; λ (lambda) is the hyperparameter; auto-drops weak features → parsimonious.
  - Best for: high-dimension regression, parsimonious models.
- **Support vector machine (SVM)** (classification): linear; finds the **hyperplane farthest from all observations**; margins set by **support vectors**; **soft-margin** handles misclassified points.
  - Best for: binary classification such as default/not or text sentiment.
- **K-nearest neighbor (KNN)** (mostly classification): classify by **nearness** to k closest training points; k is a hyperparameter (too small → high error, too large → over-averaged, even → ties); needs a distance metric.
  - Best for: bankruptcy, ratings class, custom indices.
- **CART (classification & regression tree)** (both): binary split at each **node** on the most important feature at cutoff c; stops at **terminal node**; prune / cap depth to avoid overfit; **visual, not black-box**.
  - Best for: binary classification with nonlinearities; fraud detection.
- **Ensemble learning** (both): combine **multiple models** → noise cancels → lower error. Heterogeneous (voting classifier) or homogeneous (**bagging** = bootstrap aggregating).
  - Best for: general accuracy boost.
- **Random forest** (classification): many CART trees, each on **bagged data** + a random **subset of features** → mitigates overfit, raises signal-to-noise; but **black-box**.
  - Best for: IPO success, factor-based allocation.

- **CART vs. logit**: both handle binary targets, but CART copes with **significant nonlinearities** where logit struggles. CART regression tree → continuous target.

## Unsupervised Algorithms (LOS 3.d)

- **Principal components analysis (PCA)** — **dimension reduction**: collapses many correlated features into fewer **uncorrelated** factors (**eigenvectors**). Each eigenvector's **eigenvalue** = share of total variance it explains; keep the smallest set capturing **85%–95%** of variance (**scree plot**). Black-box (components can't be cleanly labeled).
- **Clustering** — group observations by attribute similarity (**cohesion**); often via **Euclidean distance**.
  - **K-means**: partition into **k non-overlapping** clusters (k = hyperparameter); each has a **centroid**; observations reassigned until centroids stabilize.
  - **Hierarchical**: builds a hierarchy with **no preset k** — **agglomerative** (bottom-up) or **divisive** (top-down).

## Other Models — Neural Nets, DLN, RL

- **Neural networks (NN/ANN)**: **input layer → hidden layer(s) → output layer**. Hidden-layer nodes (**neurons**) = **summation operator** (weighted average) + **nonlinear activation function**; **forward propagation** passes values forward, **backward propagation** revises weights from errors. Network structure (e.g. 3-4-1 nodes) is a **hyperparameter**.
- **Deep learning networks (DLN)**: NNs with **many hidden layers (≥2, often >20)**; image/pattern/speech recognition, fraud detection, NLP. (A DLN reproduced Black-Scholes option values at R² = 99.8%.)
- **Reinforcement learning (RL)**: an **agent** maximizes a reward under constraints, learning from millions of trials (e.g. AlphaGo); no labeled data, no instant feedback.

## Exam Traps
- **Hyperparameters are set by the researcher**; they are not learned from the data (λ in LASSO, k in KNN/k-means, NN node counts).
- **Bias error = in-sample/underfit (too simple); variance error = out-of-sample/overfit (too complex).** Linear → high bias; nonlinear → high variance.
- **# features = total independent variables** (12 fundamental + 2 technical = 14, not 70).
- **Black-box** algorithms: PCA, random forest, neural nets/DLN. **CART is the transparent/visual one.**
- Unlabeled data / "group these into k dissimilar sets" → **unsupervised (clustering)**, not CART/regression.
- **Fix overfitting** with complexity reduction + cross validation — a *smaller* sample does NOT fix it.

## Q&A

### 2026-06-04 — Bias error vs. variance error, and how to fix overfitting
**Q:** What is the difference between bias error and variance error, and how do you address overfitting?
**A:** **Bias error** is the **in-sample** error from an underfit (too-simple) model — high for linear models. **Variance error** is the **out-of-sample** error from an **overfit** (too-complex) model that doesn't generalize — high for nonlinear models. As complexity rises, bias falls while variance rises, so you pick the complexity that **minimizes total error**. Address overfitting with **(1) complexity reduction** (a penalty that grows with the number of features, dropping non-contributing ones) and **(2) cross validation** (e.g. **k-fold**: split into k parts, train on k−1, validate on 1, repeat and average). Using a *smaller* sample does NOT help.
Related: [[Multiple_Regression]], [[Logistic_Regression]]

### 2026-06-04 — Which ML algorithm fits which task?
**Q:** How do you choose among LASSO, SVM, KNN, CART, random forest, PCA, and clustering?
**A:** **Supervised (labeled data):** **LASSO/penalized regression** for parsimonious high-dimension regression (penalty λ drops weak features); **SVM** for binary classification via a separating hyperplane; **KNN** to classify by nearness to k neighbors; **CART** for binary/continuous targets with nonlinearities (transparent, visual); **random forest** = many bagged CART trees on random feature subsets (more accurate but black-box). **Unsupervised (no labels):** **PCA** for dimension reduction into uncorrelated eigenvectors (keep 85–95% of variance); **k-means / hierarchical clustering** to group similar observations. Deep learning networks handle image/speech recognition and NLP.
Related: [[Big_Data_Projects]]
