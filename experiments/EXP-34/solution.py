"""EXP 34: small neural network image classification on sklearn digits.
Requires scikit-learn. Converts 8x8 grayscale digit images to labeled classes.
"""
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
d=load_digits(); Xtr,Xte,ytr,yte=train_test_split(d.data,d.target,test_size=.25,random_state=7,stratify=d.target)
m=make_pipeline(StandardScaler(),MLPClassifier(hidden_layer_sizes=(32,),max_iter=500,random_state=7))
m.fit(Xtr,ytr)
print('Test accuracy:',round(m.score(Xte,yte),3)); print('First test image prediction:',m.predict(Xte[:1])[0])
