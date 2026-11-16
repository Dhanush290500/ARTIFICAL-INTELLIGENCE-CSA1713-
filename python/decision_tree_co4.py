"""CO4: Decision tree classification on the Iris dataset.
Install dependency: python -m pip install scikit-learn
Run: python decision_tree_co4.py
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    iris.data, iris.target, test_size=0.2, random_state=42, stratify=iris.target
)
model = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
model.fit(X_train, y_train)
print("Decision Tree accuracy:", round(model.score(X_test, y_test), 2))
print(export_text(model, feature_names=list(iris.feature_names)))