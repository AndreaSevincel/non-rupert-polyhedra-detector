import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
from src.dataset.polyhedra_loader import load_polyhedra_data

def train_model():
    # Load the dataset
    data = load_polyhedra_data()
    
    # Prepare features and labels
    X = data.drop('is_non_rupert', axis=1)  # Assuming 'is_non_rupert' is the label column
    y = data['is_non_rupert']
    
    # Split the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the model
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    print(classification_report(y_test, y_pred))
    
    # Save the trained model
    joblib.dump(model, 'non_rupert_model.pkl')

if __name__ == "__main__":
    train_model()