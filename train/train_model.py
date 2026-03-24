import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC

df=pd.read_csv('Grocery_Customer_Churn_Data.csv')
df = df.drop(columns=['customer_id','education_level','transaction_id','transaction_date','promotion_type','last_purchase_date','gender','days_since_last_purchase','number_of_children','quantity','loyalty_program','unit_price','total_sales'])

y = df['churn']
X = df.drop('churn',axis=1)

# Identify column types
categorical_cols = X.select_dtypes(include=["object"]).columns
numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns

# Numerical pipeline
numeric_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="median")),
    ("scaler", StandardScaler())
])

# Categorical pipeline
categorical_pipeline = Pipeline([
    ("imputer", SimpleImputer(strategy="most_frequent")),
    ("encoder", OneHotEncoder(handle_unknown="ignore"))
])

# Combine both
preprocessor = ColumnTransformer([
    ("num", numeric_pipeline, numerical_cols),
    ("cat", categorical_pipeline, categorical_cols)
])

# Final pipeline with tuned SVM
model = Pipeline([
    ("preprocessor", preprocessor),
    ("svm", SVC(
        C=0.1,          # Replace with your tuned values
        kernel="rbf",
        gamma=0.1,
        probability=True
    ))
])

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train
model.fit(X_train, y_train)

# Save
joblib.dump(model, "churn_model.pkl")

print("Model trained and saved successfully.")
