
---

# 🧪 Growth Rate Calculator (Python, SciPy, Matplotlib)

This is a **modular Python project** for calculating and analyzing the **specific growth rate ($k$)** of biological populations (e.g., bacteria, cells) using time-concentration data.

---

## ✨ Features

* **Single-Point Growth Rate ($k$)**: Basic calculation using initial ($N_0$) and final ($N_t$) concentrations.
* **Multi-Point Fit**: Uses **linear regression** (`scipy.stats.linregress`) for accurate growth curve analysis.
* **Graphical Interface (GUI)**: Load data, plot graphs (`matplotlib`), and display results in a user-friendly window.
* **File Loading**: Direct import from `.csv` or `.txt` files.

---

## 📈 Linear Regression Principle

Growth of cells is **exponential**, but linear regression requires a linear relationship. We transform the concentration to logarithm base 2:

[
\log_2(N) = \log_2(N_0) + k \cdot t
]

* $t$: time
* $\log_2(N)$: vertical axis

The **slope** of the fitted line gives the specific growth rate $k$, and $R^2$ indicates goodness-of-fit:

[
\text{Slope} = k, \quad R^2 \in [0,1]
]

> ⚠️ **Important:** Only use data from the **exponential growth phase** for accurate $k$. $R^2$ can help identify the correct points.

---

## 🏗️ Project Structure

| File                       | Role                                                                        | Libraries               |
| -------------------------- | --------------------------------------------------------------------------- | ----------------------- |
| `calculator_logic.py`      | Business logic, growth rate calculations (`growth_rate`, `growth_rate_fit`) | `numpy`, `scipy.stats`  |
| `growth_rateGUI.py`        | Main GUI application                                                        | `tkinter`, `matplotlib` |
| `test_calculator_logic.py` | Unit tests for all calculation functions                                    | `pytest`, `numpy`       |

---

## 🛠️ Installation & Running

### 📥 Requirements

* Python 3.x
* Install dependencies:

```bash
pip install scipy matplotlib pytest numpy
```

### 🚀 Running the GUI

```bash
python growth_rateGUI.py
```

* Input multiple time & concentration points manually **or** load a CSV/TXT file.
* Click **"Calculate & Plot Growth Rate (k)"** to get results and plot.

---

## 📁 File Format for Data Loading

* **Format:** `.txt` or `.csv`
* **Structure:** 2 columns:

  1. Time ($t$) ≥ 0
  2. Concentration ($N$) > 0
* **Delimiter:** comma `,`, tab `\t`, or space
* Lines starting with `#` or empty lines are ignored

**Example:**

```
# Time (Hours), Concentration (OD)
0, 0.1
1.5, 0.25
3.0, 0.5
4.5, 1.05
6.0, 2.0
```

---

## ✅ Running Tests

Ensure calculation logic works correctly:

```bash
pytest test_calculator_logic.py
```

---

## 🧪 Development Notes

### Multi-Point Fit

* New function `growth_rate_fit(times, concentrations)` uses `scipy.stats.linregress` on **log2-transformed data**.
* Returns: `(k, R^2)`
* Input validation checks for:

  * Non-empty lists
  * Equal length
  * Positive concentrations

### Edge Case Fix

* **Stagnant data** (no growth, zero variance) can produce `NaN` in `R^2`.
* **Solution:** If variance is zero, return `k=0.0` and `R^2=1.0`.

---

## 📚 Linear Regression & Exponential Growth

1. Growth is exponential; direct regression fails on raw concentrations.
2. Apply $\log_2$ transformation to linearize.
3. Fit a straight line and extract slope as $k$.
4. $R^2$ quantifies how well the exponential phase fits a line.

> Only exponential growth phase data should be used for accuracy.

---

## 📝 Summary

* Modular Python project for **biological growth rate calculation**.
* GUI with **manual or file input**, plotting, and multi-point linear regression.
* Well-tested with `pytest`.
* Clear separation of **business logic** and **interface**.

---


---


