# Customer Churn Prediction using Machine Learning

* Problem Statement

Customer churn is a critical challenge for businesses. The goal of this project is to build a machine learning model that can accurately identify customers who are likely to churn, with a focus on minimizing false negatives.

* Dataset

Customer transactional and behavioral data
Target variable: churn (1 = churn, 0 = non-churn)

* Approach

Performed data preprocessing and feature encoding
Handled class imbalance using SMOTE



Trained multiple classification models:

Logistic Regression
KNN
Decision Tree
Random Forest
SVM

Selected final model based on recall rather than accuracy
Tuned SVM hyperparameters using RandomizedSearchCV
Interpreted churn drivers using Random Forest feature importance



* Results

Achieved 90% recall for churn customers using tuned SVM
Demonstrated trade-off between recall and accuracy
Identified key churn drivers:
Average purchase value
Purchase frequency
Discount dependency



* Key Insights

Churn is primarily driven by changes in customer purchasing behavior
Behavioral features are more predictive than demographic attributes
Early decline in spending and frequency indicates churn risk



* Tech Stack

Python
Pandas, NumPy
Scikit-learn
Imbalanced-learn (SMOTE)
Matplotlib / Seaborn

* Conclusion

This project demonstrates an end-to-end machine learning workflow with business-driven evaluation, proper handling of class imbalance, and model explainability.
