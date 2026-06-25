# 🏦 Loan Default Prediction System

## 📌 Project Overview

This is an end-to-end Machine Learning project that predicts whether a customer is likely to default on a loan using customer financial and personal information.

The project covers the complete workflow from data understanding and preprocessing to model training and building an interactive Streamlit web application.

---

## 🎯 Problem Statement

Financial institutions face significant risks when customers fail to repay loans. Identifying high-risk customers early can reduce financial losses and improve lending decisions.

The objective of this project is to classify customers into:

* Likely Default
* Likely Non-default

---

## 📂 Dataset Information

The dataset contains customer financial and personal information.

### Numerical Features

* Age
* Income
* Loan Amount
* Credit Score
* Months Employed
* Number of Credit Lines
* Interest Rate
* Loan Term
* DTI Ratio

### Categorical Features

* Education
* Employment Type
* Marital Status
* Has Mortgage
* Has Dependents
* Loan Purpose
* Has Co-Signer

Removed feature:

* LoanID

---

## 🔄 Project Workflow

### Step 1: Data Understanding

* Loaded dataset
* Explored dataset structure
* Removed unnecessary feature (LoanID)

### Step 2: Exploratory Data Analysis (EDA)

Performed EDA to identify patterns and customer behavior.

Key insights:

* Lower credit scores increased default risk
* Higher DTI ratio showed stronger default tendencies
* Employment type influenced customer risk
* Loan purpose affected loan behavior

### Step 3: Data Preprocessing

Created a preprocessing pipeline using:

* ColumnTransformer
* Categorical encoding
* Pipeline approach for reproducibility

### Step 4: Model Training

Performed:

* Train-test split
* Logistic Regression training
* Cross-validation
* Performance evaluation
* Model experimentation

### Step 5: Model Improvement

Instead of focusing only on accuracy, multiple evaluation metrics were analyzed:

* Precision
* Recall
* F1 Score
* ROC-AUC

Special focus was given to Recall because in loan default prediction missing risky customers can create larger financial losses than incorrectly flagging safe customers.

Improvements included:

* Better preprocessing pipeline
* Cross-validation
* Performance analysis
* Model experimentation

---

## 📊 Final Model Performance

Final Model:

**Logistic Regression**

Performance Metrics:

* Accuracy: **67.65%**
* Recall: **69.97%**
* F1 Score: **33.44%**
* ROC-AUC Score: **68.66%**

Confusion Matrix:

| Actual / Predicted | Non-default | Default |
| ------------------ | ----------- | ------- |
| Non-default        | 30400       | 14739   |
| Default            | 1781        | 4150    |

Observation:

The model achieved a relatively high Recall (~70%), meaning it successfully identified a large proportion of risky customers. Since the business objective prioritizes identifying potential defaulters, recall was considered an important evaluation metric rather than relying only on overall accuracy.

---

## 💻 Web Application Features

✅ Interactive Streamlit UI

✅ Real-time prediction

✅ Professional risk visualization

✅ User-friendly design

✅ Customer risk prediction system

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## ▶️ Run Project Locally

Install requirements:

```bash
pip install -r requirements.txt
```

Run application:

```bash
streamlit run app.py
```


## 👤 Author

Tanvi Ukani
