import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import RidgeClassifier
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score
import numpy as np

def train_model():
    data = pd.read_csv('C:/Users/Arjun S V/Desktop/MENTAL WELLBEING BASED ON DIGITAL ACTIVITY/mentalhealth.csv')

    X = data.drop('anxiety_level', axis=1)
    y = data['anxiety_level']

    X.fillna(X.mean(), inplace=True)

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42)

    # First, get actual number of bins (might be less than 3 if duplicates dropped)
    temp_bins = pd.qcut(y_train, q=3, duplicates='drop')
    n_bins = temp_bins.cat.categories.size
    labels = list(range(n_bins))

    y_train_binned = pd.qcut(y_train, q=n_bins, labels=labels, duplicates='drop')
    y_test_binned = pd.qcut(y_test, q=n_bins, labels=labels, duplicates='drop')

    models = {
        "Ridge": RidgeClassifier(),
        "RandomForest": RandomForestClassifier(n_estimators=100, random_state=42),
        "XGBoost": XGBClassifier(eval_metric='logloss', random_state=42)
    }

    accuracies = {}
    for name, model in models.items():
        model.fit(X_train, y_train_binned)
        y_pred = model.predict(X_test)
        acc = accuracy_score(y_test_binned, y_pred)
        accuracies[name] = acc
        print(f"{name} Accuracy: {acc:.4f}")

    best_model_name = max(accuracies, key=accuracies.get)
    best_model = models[best_model_name]
    print(f"\n✅ Best Model: {best_model_name} with accuracy {accuracies[best_model_name]:.4f}")

    feature_names = data.drop('anxiety_level', axis=1).columns.tolist()
    label_levels = {0: "Low Anxiety", 1: "Moderate Anxiety", 2: "High Anxiety"}

    return best_model, scaler, feature_names, label_levels

def predict_anxiety(model, scaler, input_data):
    input_array = np.array(input_data).reshape(1, -1)
    input_scaled = scaler.transform(input_array)
    prediction = model.predict(input_scaled)[0]
    return prediction
