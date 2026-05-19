import mlflow
import mlflow.sklearn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_iris()

X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2
)

# Start MLflow run
with mlflow.start_run():

    # Train model
    model = RandomForestClassifier()

    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    accuracy = accuracy_score(y_test, predictions)

    # Log parameter
    mlflow.log_param("model_type", "RandomForest")

    # Log metric
    mlflow.log_metric("accuracy", accuracy)

    # Log and register model
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="IrisClassifier"
    )

    print(f"Model Accuracy: {accuracy}")
