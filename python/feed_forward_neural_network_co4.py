"""CO4: Feed-forward neural network classification on the Iris dataset.
Install dependency: python -m pip install scikit-learn
Run: python feed_forward_neural_network_co4.py
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)
model = make_pipeline(StandardScaler(), MLPClassifier(
    hidden_layer_sizes=(8,), activation="relu", solver="lbfgs",
    max_iter=1000, random_state=42))
model.fit(X_train, y_train)
print("Feed-forward neural network accuracy:", round(model.score(X_test, y_test), 2))
print("Prediction:", iris.target_names[model.predict(X_test[:1])[0]])