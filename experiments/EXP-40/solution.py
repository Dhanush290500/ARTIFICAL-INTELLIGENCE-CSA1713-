"""EXP 40: user-user collaborative filtering with cosine similarity."""
import numpy as np
ratings=np.array([[5,3,0,1],[4,0,0,1],[1,1,0,5],[0,0,5,4]],dtype=float)
# Recommend highest-rated item from nearest user that target user has not rated.
target=0; similarities=[]
for u in range(len(ratings)):
    if u==target: continue
    a,b=ratings[target],ratings[u]; mask=(a>0)&(b>0)
    sim=(a[mask]@b[mask])/(np.linalg.norm(a[mask])*np.linalg.norm(b[mask])) if mask.any() else 0
    similarities.append((sim,u))
sim,u=max(similarities); candidates=[i for i,x in enumerate(ratings[target]) if x==0]
rec=max(candidates,key=lambda i:ratings[u,i])
print('Most similar user:',u); print('Recommended item:',rec+1); print('Similarity:',round(sim,3))
