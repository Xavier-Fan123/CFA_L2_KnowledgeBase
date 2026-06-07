---
aliases: [Big Data Projects, Data Wrangling, Data Cleansing, Normalization, Standardization, Text Processing, Bag-of-Words, BOW, Document Term Matrix, N-grams, Tokenization, Stemming, Lemmatization, Confusion Matrix, Precision, Recall, F1 Score, ROC, AUC, Fitting Curve, Grid Search, Ceiling Analysis, Class Imbalance]
tags: [CFA-L2, quant, concept, big-data, machine-learning]
date: 2026-06-04
status: evergreen
source: Schweser Book 1, Reading 4 (Modules 4.1–4.3), LOS 4.a–4.g
---

# Big Data Projects

> Sister note to [[Machine_Learning]]. The "three Vs" of big data: **Volume, Variety, Velocity** (+ **Veracity** when used for inference). **Structured** data = rows/columns; **unstructured** = text, images, audio.

## Five Steps of a Data Analysis Project (LOS 4.a)

1. **Conceptualization** — define the problem, the output, who uses it, how it embeds in the business.
2. **Data collection** — gather (usually structured, numeric) data from internal/external sources.
3. **Data preparation & wrangling** — clean and preprocess.
4. **Data exploration** — feature selection, feature engineering, exploratory analysis.
5. **Model training** — select algorithm, train, tune.

Steps are **iterative**. For **text/unstructured** data the first four become: text **problem formulation → curation (collection) → text preparation & wrangling → text exploration**.

## Data Preparation & Wrangling (LOS 4.b)

**Data cleansing** fixes raw-data errors: **missing, invalid (out-of-range), inaccurate, non-uniform (format/unit), duplicate** values. (Note: "common values" are NOT a cleansing target — exam trap.)

**Data wrangling = transformation + scaling:**
- **Transformation types**: **Extraction, Aggregation, Filtration** (drop irrelevant observations/rows), **Selection** (drop unneeded features/columns), **Conversion** (data types).
- **Outliers**: **trimming** removes the highest/lowest x% of observations; **winsorization** replaces extremes with the maximum/minimum allowable value.
- **Scaling** (put features on a common range — required by NN, SVM):

| Method | Range | Note |
|---|---|---|
| **Normalization** | scales to **[0, 1]** | sensitive to outliers |
| **Standardization** | mean **0**, SD **1** (z-scores) | **not** outlier-sensitive, but **assumes normality** |

## Text Preparation, Wrangling & Exploration (LOS 4.g, 4.e)

**Text cleansing** — remove: (1) **HTML tags** (via regex), (2) **punctuation** (keep %, $, ? as annotations if meaningful), (3) **numbers** (replace with annotation), (4) **white space**.

**Text wrangling (normalization):** (1) **lowercasing**, (2) remove **stop words** (the, is…), (3) **stemming** (rules-based root: integrate/integration → "integrat"), (4) **lemmatization** (maps to the morphological **lemma** — more advanced/resource-intensive than stemming).

- **Token** = a word; **tokenization** = splitting text into tokens.
- **Bag-of-words (BOW)** = collection of tokens, **ignoring sequence**.
- **Document term matrix (DTM)** = structured output: **rows = documents, columns = tokens, cell = count** of token in that document.
- **N-grams** keep word sequences when order matters (bigram, trigram). N-grams change BOW normalization because **stop words are not removed**.

**Text feature selection** (trim the BOW; drop very high- and very low-frequency words):
- **Document frequency (DF)** = (# documents containing the token) / (total documents).
- **Chi-square** — ranks tokens by association with a class.
- **Mutual information (MI)** — token in **all** classes → **MI ≈ 0** (useless discriminator); token in one/few classes → **MI ≈ 1**.

**Text feature engineering**: **numbers** (→ /numberX/, 4-digit → /number4/), **N-grams**, **name entity recognition (NER)** (Microsoft → ORG), **parts of speech (POS)** (Microsoft → NNP, 1969 → CD).

## Data Exploration for Structured Data (LOS 4.d)

- **Exploratory data analysis (EDA)**: summary stats, heat maps, word clouds; single-feature visuals (histogram, density plot, bar chart, box plot) and multi-feature (correlation matrix, scatterplot).
- **Feature selection**: keep only features that add out-of-sample power → more **parsimonious** model, less noise.
- **Feature engineering (FE)**: create/transform features (log, decompose, combine); **one-hot encoding (OHE)** converts a categorical feature into binary dummies.
- For unstructured text: **word cloud** (bigger font = higher frequency); summary stats = **term frequency** and **co-occurrence**.

### Commodity Hedge Fund Extension (Beyond Curriculum)
This section is a professional hedge-fund application, not CFA curriculum text.

- For a top commodity fund, the data project is an alpha-production system, not a dashboard. Useful sources can include exchange data, broker flows, customs data, vessel AIS, satellite storage estimates, pipeline nominations, refinery runs, weather models, crop conditions, power load, credit data, and text/news.
- **Veracity** is the dominant issue. Every observation needs timestamp, source, revision history, unit, location, product specification, delivery period, and point-in-time availability. A signal received after the market close cannot be used as if it was known before the trade.
- Data wrangling must solve commodity-specific mapping: barrels vs. tonnes, grades, sulfur/API quality, delivery hubs, contract rolls, holiday calendars, time zones, daylight saving changes, and benchmark changes. Unit errors can look like alpha in backtests.
- Alternative data is valuable only after conversion into a tradable feature: inventory surprise, congestion, implied run rate, export pace, weather deviation, vessel delay, or balance revision. Raw novelty is not edge.
- Feature engineering should encode lags and publication timing. Many fundamental series are revised, delayed, sampled irregularly, or released during illiquid trading hours; ignoring this creates look-ahead bias.
- Production-grade data work includes lineage, anomaly flags, vendor-change monitoring, stale-data detection, and a fallback rule for missing feeds. A fragile data feed can become a hidden position risk.

## Model Training (LOS 4.f)

**Method selection** depends on:
- **Supervised** (target/ground truth present) → regression, ensemble trees, SVM, NN. **Unsupervised** (no target) → clustering, dimension reduction, anomaly detection.
- **Data type**: numerical → CART; text → GLM/SVM; image → NN/deep learning.
- **Data size**: large (many obs & features) → SVM; NN better with many observations but few features.

**Data split (supervised only):** ~**60% training / 20% validation / 20% test**. Unsupervised needs no split (no labels).

**Class imbalance**: one class dominates (e.g. mostly high-grade bonds) → model biased toward the majority. Fix by **undersampling the overrepresented** class and **oversampling the underrepresented**.

## Model Evaluation — Confusion Matrix & Metrics (LOS 4.c)

Errors: **false positive = Type I**, **false negative = Type II**.

| Metric | Formula | Use |
|---|---|---|
| **Precision (P)** | `TP / (TP + FP)` | value when **Type I (FP)** cost is high |
| **Recall (R)** = TPR | `TP / (TP + FN)` | value when **Type II (FN)** cost is high (e.g. lender avoiding defaulters) |
| **Accuracy** | `(TP + TN) / (TP+TN+FP+FN)` | overall correct rate |
| **F1 score** | `2PR / (P + R)` | **harmonic mean** of P and R (use when classes imbalanced) |
| **FPR** | `FP / (FP + TN)` | x-axis of ROC |

- **ROC curve** plots **TPR (y) vs. FPR (x)**; **AUC** ∈ [0,1], closer to 1 = better; **AUC = 0.5** = random guessing. More convex curve → higher AUC.
- **RMSE** is used for **continuous** (regression) targets, not classification.

## Model Tuning (LOS 4.c)

- **Bias error** = training error from **underfitting** (too simple); **variance error** = validation error from **overfitting** (too complex). Find the bias-variance optimum.
- **Fitting curve**: training error vs. cross-validation error across complexity; as complexity rises, bias error falls but variance error rises.
- **Regularization** penalizes non-contributing features to cut complexity.
- **Parameters** (e.g. regression slopes) are **learned** from data; **hyperparameters** (NN hidden layers, logit p-threshold) are **set by engineers**. **Tuning** adjusts hyperparameters.
- **Grid search** = automated search for the best hyperparameter combination. **Ceiling analysis** evaluates each pipeline component to find the weak link.

## Worked Example — confusion matrix metrics

Dividend-cut model, 78 test obs: TP = 18 (correctly flagged cuts), TN = 46, FN = 3 (missed cuts), so FP = 78 − 18 − 46 − 3 = 11.
- **Precision** = 18/(18+11) = **0.621**; **Recall** = 18/(18+3) = **0.857**;
- **Accuracy** = (18+46)/78 = **0.821**; **F1** = 2(0.621)(0.857)/(0.621+0.857) = **0.720**;
- **FPR** = 11/(11+46) = **0.193**.

## Exam Traps
- **Normalization → [0,1]** (outlier-sensitive); **standardization → mean 0, SD 1** (assumes normality, not outlier-sensitive). Don't swap them.
- **Recall** ↔ Type II/FN cost; **Precision** ↔ Type I/FP cost. F1 = **harmonic** mean (not arithmetic).
- **AUC = 0.5 means random**; higher (toward 1) is better.
- **Parameters are learned; hyperparameters are set by the researcher** and adjusted in tuning.
- **Stemming** is rules-based and crude; **lemmatization** is more advanced/resource-heavy.
- "Common values" are not a data-cleansing item; structured cleansing targets missing/invalid/inaccurate/ non-uniform/duplicate.

## Q&A

### 2026-06-04 — Precision, recall, accuracy, F1 from a confusion matrix
**Q:** How are precision, recall, accuracy, and the F1 score computed, and when does each matter?
**A:** From a confusion matrix: **Precision = TP/(TP+FP)**, **Recall = TP/(TP+FN)**, **Accuracy = (TP+TN)/total**, **F1 = 2·P·R/(P+R)** (harmonic mean). A **false positive is Type I**, a **false negative is Type II**. **High precision** matters when a **Type I error (FP)** is costly; **high recall** matters when a **Type II error (FN)** is costly (e.g. a lender wanting to catch all potential defaulters maximizes recall). F1 is the preferred single metric under class imbalance. For continuous targets use **RMSE**, and for classification trade-offs use the **ROC curve / AUC** (AUC = 0.5 is random, near 1 is strong).
Related: [[Machine_Learning]]

### 2026-06-04 — How is unstructured text turned into model-ready data?
**Q:** Walk through preparing text data for a forecasting model.
**A:** **Cleanse**: remove HTML tags (regex), punctuation, numbers, and white space. **Wrangle/normalize**: lowercase, remove stop words, **stem** (rules-based root) or **lemmatize** (map to morphological lemma), then **tokenize**. Build a **bag-of-words (BOW)** (order ignored) — or **N-grams** if sequence matters — and convert to a **document term matrix** (rows = documents, columns = tokens, cells = counts). **Explore** with term frequency, co-occurrence, and word clouds; **select features** via document frequency, chi-square, and mutual information (MI≈0 useless, MI≈1 discriminating); **engineer** with number tags, NER, and POS.
Related: [[Big_Data_Projects]]
