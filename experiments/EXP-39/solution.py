"""EXP 39: PCA reduces four correlated features to two components."""
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
d=load_iris(); X=StandardScaler().fit_transform(d.data); p=PCA(n_components=2).fit_transform(X)
print('Original dimensions:',d.data.shape[1]); print('Reduced dimensions:',p.shape[1]); print('First projected sample:',[round(v,3) for v in p[0]])
