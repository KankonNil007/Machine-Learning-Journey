<div align="center">

# 🧠 Machine Learning Journey
### Hands-On Implementations, Mathematical Intuition & Practical ML Projects

[![Python Version](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebooks-orange?style=for-the-badge&logo=jupyter&logoColor=white)](https://jupyter.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-v1.3+-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-emerald?style=for-the-badge)](https://opensource.org/licenses/MIT)

<p align="center">
  A premium, high-fidelity log of my journey learning machine learning from scratch. It contains comprehensive data science workflows, model benchmarking, validation pipelines, and practical implementation notebooks.
</p>

[📂 Repository Structure](#-repository-structure) • [🗓️ Day-by-Day Milestones](#-day-by-day-milestones) • [🛠️ Tooling & Libraries](#-tooling--libraries) • [🚀 Getting Started](#-getting-started)

</div>

---

> [!NOTE]
> **Repository Purpose:** This codebase documents my progressive development in Machine Learning. From foundational exploratory data analysis to complex ensemble models, hyperparameter tuning, and model deployment serialization.

---

## 📂 Repository Structure

Below is an overview of the directory layout and the localized study structure:

```text
Machine-Learning-Journey/
│
├── 📁 Day-01_EDA_and_Feature_Selection/
│   ├── 📁 files/                                     # Raw datasets (heart.csv, insurance.csv)
│   ├── 📄 eda_preprocessing_and_feature_selection_classification.ipynb
│   └── 📄 eda_preprocessing_and_feature_selection_regression.ipynb
│
├── 📁 Day-02_Linear_Regression/
│   ├── 📁 files/                                     # Raw datasets (car data, housing data, insurance)
│   ├── 📄 linear_regression_ford_pricing.ipynb
│   ├── 📄 linear_regression_housing_prices.ipynb
│   └── 📄 linear_regression_insurance_charges.ipynb
│
├── 📁 Day-03_Classification_Algorithms/
│   ├── 📁 deployment/                                # Serialized production artifacts (.pkl)
│   ├── 📁 files/                                     # Raw classification datasets
│   ├── 📄 classification_algorithms_heart_disease.ipynb
│   └── 📄 classification_algorithms_titanic_survival.ipynb
│
├── 📁 Day-04_Advanced_ML_Concepts/
│   ├── 📄 cross_validation_titanic_survival.ipynb
│   ├── 📄 dimensionality_reduction_pca.ipynb
│   ├── 📄 ensemble_learning_classifiers.ipynb
│   ├── 📄 hyperparameter_tuning_grid_and_random_search.ipynb
│   └── 📄 unsupervised_clustering_kmeans_dbscan.ipynb
│
├── 📄 LICENSE
├── 📄 README.md                                      # Repository Homepage
└── 📄 SECURITY.md
```

---

## 🗓️ Day-by-Day Milestones

| Day | Core Focus | Notebooks & Datasets | Key Methods Learned |
| :--- | :--- | :--- | :--- |
| **Day 01** | **EDA & Feature Selection** | 📄 [classification_feature_selection.ipynb](Day-01_EDA_and_Feature_Selection/eda_preprocessing_and_feature_selection_classification.ipynb) (`heart.csv`) <br> 📄 [regression_feature_selection.ipynb](Day-01_EDA_and_Feature_Selection/eda_preprocessing_and_feature_selection_regression.ipynb) (`insurance.csv`) | - Pearson Correlation <br> - Chi-Squared Independence Test (`chi2_contingency`) <br> - StandardScaler scaling & One-Hot encoding |
| **Day 02** | **Supervised Learning - Regression** | 📄 [ford_pricing.ipynb](Day-02_Linear_Regression/linear_regression_ford_pricing.ipynb) (`ford.csv`) <br> 📄 [housing_prices.ipynb](Day-02_Linear_Regression/linear_regression_housing_prices.ipynb) (`housing.csv`) <br> 📄 [insurance_charges.ipynb](Day-02_Linear_Regression/linear_regression_insurance_charges.ipynb) (`insurance.csv`) | - Linear Regression <br> - Performance Metrics ($R^2$, MAE, MSE) <br> - Multi-modal data handling |
| **Day 03** | **Supervised Learning - Classification** | 📄 [heart_disease.ipynb](Day-03_Classification_Algorithms/classification_algorithms_heart_disease.ipynb) (`heart.csv`) <br> 📄 [titanic_survival.ipynb](Day-03_Classification_Algorithms/classification_algorithms_titanic_survival.ipynb) (`titanic.csv`) | - Benchmarking Classifiers (Logistic Reg, KNN, Naive Bayes, Decision Trees, SVM) <br> - Model Serialization (`pickle` deployment models in [deployment/](Day-03_Classification_Algorithms/deployment)) |
| **Day 04** | **Advanced Concepts & Clustering** | 📄 [cross_val_titanic.ipynb](Day-04_Advanced_ML_Concepts/cross_validation_titanic_survival.ipynb) (`titanic.csv`) <br> 📄 [dimensionality_reduction_pca.ipynb](Day-04_Advanced_ML_Concepts/dimensionality_reduction_pca.ipynb) <br> 📄 [ensemble_learning_classifiers.ipynb](Day-04_Advanced_ML_Concepts/ensemble_learning_classifiers.ipynb) <br> 📄 [hyperparameter_tuning.ipynb](Day-04_Advanced_ML_Concepts/hyperparameter_tuning_grid_and_random_search.ipynb) <br> 📄 [unsupervised_clustering.ipynb](Day-04_Advanced_ML_Concepts/unsupervised_clustering_kmeans_dbscan.ipynb) | - K-Fold Cross-Validation (`cross_val_score`) <br> - PCA Dimensionality Reduction <br> - Ensemble learning (Boosting, Stacking, Random Forest) <br> - Grid / Randomized Search CV <br> - K-Means & DBSCAN Clustering |

---

## 🛠️ Tooling & Libraries

This journey leverages the standard Python PyData ecosystem for scientific computing and machine learning modeling:

*   **Data Manipulation & Analysis:** `pandas` • `numpy`
*   **Data Visualization:** `matplotlib` • `seaborn`
*   **Machine Learning Modeling:** `scikit-learn`
*   **Statistical Evaluators:** `scipy`
*   **Model Serialization:** `pickle`

---

## 🚀 Getting Started

### 📋 Prerequisites
Ensure you have **Python 3.8+** installed.

### ⚙️ Installation & Setup

1.  **Clone this repository**:
    ```bash
    git clone https://github.com/KankonNil007/Machine-Learning-Journey.git
    cd Machine-Learning-Journey
    ```

2.  **Initialize Virtual Environment**:
    *   **Windows (PowerShell):**
        ```powershell
        python -m venv venv
        .\venv\Scripts\activate
        ```
    *   **macOS / Linux:**
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3.  **Install Required Dependencies**:
    ```bash
    pip install numpy pandas matplotlib seaborn scikit-learn scipy
    ```

4.  **Launch Jupyter Notebook**:
    ```bash
    jupyter notebook
    ```
    Navigate through any folder (e.g. [Day-02_Linear_Regression](Day-02_Linear_Regression)) and open the desired `.ipynb` notebook file to experiment.
