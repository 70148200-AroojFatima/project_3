from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Component A: Load and preprocess data
data = load_iris()

X = data.data
y = data.target

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Data preprocessing completed")

# Component B: Train model
model = RandomForestClassifier()

model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")

print("Model training completed")

# Component C: Evaluate model
predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy}")
