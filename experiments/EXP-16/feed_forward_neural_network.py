"""Feed-forward neural network classification example using scikit-learn."""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.25, random_state=42, stratify=iris.target
)
model = make_pipeline(
    StandardScaler(),
    MLPClassifier(hidden_layer_sizes=(8,), activation="relu", solver="lbfgs",
                  max_iter=1000, random_state=42),
)
model.fit(X_train, y_train)
print("Accuracy:", round(model.score(X_test, y_test), 3))
print("Prediction for first test sample:", iris.target_names[model.predict(X_test[:1])[0]])
