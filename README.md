# 🚀 Customer Churn Prediction & Retention Analysis

<p align="center">
  <b>An End-to-End Machine Learning Project for Predicting Customer Churn</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine-Learning-orange" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Streamlit-Application-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Status-Completed-success" />
</p>

## 📌 Project Overview

Customer Churn Prediction and Retention Analysis is an end-to-end Data Science project that uses Machine Learning to predict whether a customer is likely to leave a telecom service.

The project combines Exploratory Data Analysis, data preprocessing, model development, model evaluation, explainable AI and customer risk segmentation to generate actionable business insights.

## 📊 Project Dashboard

| Project Metric | Result |
|---|---:|
| Total Customer Records | 7,043 |
| Churned Customers | 1,869 |
| Non-Churned Customers | 5,174 |
| Churn Rate | 26.54% |
| Machine Learning Models | 4 |
| Selected Model | Logistic Regression |

## 🏆 Final Model Performance

| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| Logistic Regression | 80.70% | 65.84% | 56.68% | 60.92% | 84.16% |
| Decision Tree | 79.42% | 62.96% | 54.55% | 58.45% | 82.84% |
| Random Forest | 80.41% | 66.67% | 52.41% | 58.68% | 84.32% |
| Tuned Logistic Regression | 80.34% | 65.20% | 55.62% | 60.03% | 84.10% |

**Selected Model:** Logistic Regression based on its highest accuracy and F1-score among the evaluated models.

## 🧠 Key Project Features

- Customer churn exploratory data analysis
- Missing value handling and data preprocessing
- Categorical encoding and feature scaling
- Multiple machine learning model comparison
- Hyperparameter tuning using GridSearchCV
- Confusion matrix and ROC curve evaluation
- SHAP-based model explainability
- Permutation feature importance
- Customer churn probability prediction
- Low, Medium and High Risk customer segmentation
- Interactive Streamlit prediction application

## 📈 Visualizations

The project includes:

- Churn Distribution Analysis
- Contract Type vs Churn
- Monthly Charges vs Churn
- Tenure vs Churn
- Payment Method Analysis
- Correlation Heatmap
- Confusion Matrix
- ROC Curve
- SHAP Summary Plot
- Customer Risk Analysis Dashboard

## 🛠️ Technologies Used

| Category | Tools |
|---|---|
| Programming | Python |
| Data Analysis | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Machine Learning | Scikit-learn |
| Explainable AI | SHAP |
| Application | Streamlit |
| Development | Google Colab, Jupyter Notebook |

## 📂 Project Structure

```text
Customer_Churn_Prediction_Project/
│
├── App/
│   └── app.py
├── Dataset/
│   ├── cleaned_customer_churn.csv
│   └── encoded_customer_churn.csv
├── Documentation/
├── Models/
├── Notebooks/
├── Reports/
│   ├── Customer_Churn_Prediction_Final_Report.docx<img width="1536" height="1024" alt="Neon Customer Churn Analytics Dashboard" src="https://github.com/user-attachments/assets/3aae189f-1f8a-477b-a648-c99b7978016c" />

├── Visualizations/
├── README.md
└── requirements.txt
```

## ▶️ Run the Application

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application from the project root:

```bash
streamlit run App/app.py
```

## 💡 Business Recommendations

- Identify customers with high churn probability.
- Offer retention incentives to high-risk customers.
- Review month-to-month contract customers.
- Improve customer experience and service quality.
- Monitor customer satisfaction and payment patterns.

## ⚠️ Model Limitation

The selected Logistic Regression model achieves 80.70% accuracy and 56.68% recall. Some actual churners may not be identified, so model predictions should support, not replace, business decisions.

## 👩‍💻 Author

**Ankita Sahu**

B.Tech | Data Science & Machine Learning

---

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>
