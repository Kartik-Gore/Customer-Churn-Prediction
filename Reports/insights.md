# Customer Churn Prediction – Project Insights

## 1. Dataset Overview
- **Source:** [Your dataset source here]
- **Number of rows:** 7,000 (example)
- **Number of features:** 20 (excluding target)
- **Target column:** `Churn` (1 = churned, 0 = retained)
- **Missing values handled:** Yes, filled with 0 or mean

## 2. Exploratory Data Analysis (EDA)

### Churn Distribution
- Total churned customers: 2,500 (≈36%)
- Total retained customers: 4,500 (≈64%)

### Key Observations from EDA
- Customers with **high monthly charges** tend to churn more.
- Long tenure is associated with **lower churn probability**.
- Services like **InternetService = DSL** are slightly less likely to churn than **Fiber optic** users.
- **Contract type** has a strong effect: month-to-month contracts churn more than one- or two-year contracts.

### Correlation Highlights
- `tenure` negatively correlates with churn.
- `MonthlyCharges` positively correlates with churn.
- Features like `OnlineSecurity` and `TechSupport` show protective effects.

*(Tip: Include a heatmap or bar charts from 01_EDA.ipynb here if desired.)*

## 3. Feature Engineering
- **Categorical encoding:** Label Encoding for all categorical variables.
- **Numeric scaling:** StandardScaler applied to continuous features.
- **New features:** None in this version, but you can add derived features like `TotalCharges_per_Tenure`.

## 4. Model Training & Evaluation

### Models Trained
| Model                  | Accuracy (Test) |
|------------------------|----------------|
| Logistic Regression    | 79%            |
| Random Forest Classifier | 86% (Best)    |

### Random Forest Evaluation
- **Accuracy:** 86%
- **Confusion Matrix:**
```
[[2600  400]
 [ 350  650]]
```
- **Classification Report:**
```
              precision    recall  f1-score   support

           0       0.88      0.87      0.87      3000
           1       0.62      0.65      0.63      1000

    accuracy                           0.86      4000
   macro avg       0.75      0.76      0.75      4000
weighted avg       0.83      0.86      0.84      4000
```

- **Feature Importance (Top 5):**
  1. `Contract`
  2. `tenure`
  3. `MonthlyCharges`
  4. `InternetService`
  5. `PaymentMethod`

*(Tip: Save `feature_importances_` plot from modeling notebook and reference here.)*

## 5. Key Insights
- Customers on **month-to-month contracts** are at highest risk of churn.
- High `MonthlyCharges` combined with **short tenure** increases churn probability.
- Offering additional services like **Tech Support** or **Online Security** may reduce churn.
- Random Forest is effective due to handling **non-linear relationships** and capturing feature importance.

## 6. Recommendations
- Focus retention strategies on high-risk segments (month-to-month contracts, high monthly charges, short tenure).
- Monitor high-value customers frequently to prevent churn.
- Use the **Streamlit dashboard** to predict churn for new customers and take proactive action.

## 7. Next Steps
- Experiment with **XGBoost** or **Gradient Boosting** for improved accuracy.
- Include **customer engagement metrics** or interaction history as new features.
- Deploy the model in production for **real-time churn prediction**.
- Automate reports generation for periodic analysis.

---

**Note:** All metrics and plots can be updated based on your actual dataset. Save this file as `reports/insights.md` and reference it in your README for documentation.
