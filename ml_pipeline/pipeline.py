from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

print("Step 1: Data Preprocessing")

# Load dataset
data = load_iris()
X = data.data
y = data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

print("Step 2: Model Training")

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

print("Step 3: Model Evaluation")

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy}")

print("Step 4: Model Packaging")

# Save model
joblib.dump(model, "model.pkl")

print("Pipeline completed successfully!")