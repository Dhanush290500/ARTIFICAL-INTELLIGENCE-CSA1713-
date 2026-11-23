"""EXP 14: Alpha-Beta Pruning on a small deterministic game tree."""
TREE={'A':['B','C'],'B':['D','E'],'C':['F','G'],'D':[3,5],'E':[6,9],'F':[1,2],'G':[0,-1]}
visited=0
def minimax(node,maximizing,alpha=float('-inf'),beta=float('inf')):
    global visited
    visited+=1
    if isinstance(node,int): return node
    vals=[]
    for child in TREE[node]:
        vals.append(minimax(child,not maximizing,alpha,beta))
        if maximizing: alpha=max(alpha,vals[-1])
        else: beta=min(beta,vals[-1])
        if True and beta<=alpha: break
    return (max if maximizing else min)(vals)
if __name__=='__main__':
    score=minimax('A',True)
    print('Best score for MAX:',score)
    print('Nodes evaluated:',visited)
