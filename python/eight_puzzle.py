"""EXP 01: 8-puzzle solver using breadth-first search."""
from collections import deque

START = (1, 2, 3, 4, 0, 6, 7, 5, 8)
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def solve(start, goal):
    queue=deque([(start, [start])]); seen={start}
    while queue:
        state,path=queue.popleft()
        if state==goal: return path
        z=state.index(0); r,c=divmod(z,3)
        for dr,dc,move in [(-1,0,'Up'),(1,0,'Down'),(0,-1,'Left'),(0,1,'Right')]:
            nr,nc=r+dr,c+dc
            if 0<=nr<3 and 0<=nc<3:
                j=nr*3+nc; nxt=list(state); nxt[z],nxt[j]=nxt[j],nxt[z]; nxt=tuple(nxt)
                if nxt not in seen: seen.add(nxt); queue.append((nxt,path+[nxt]))
    return None

def show(state):
    for i in range(0,9,3): print(' '.join('_' if x==0 else str(x) for x in state[i:i+3]))

if __name__=='__main__':
    solution=solve(START,GOAL)
    print(f'Solution found in {len(solution)-1} moves:')
    for step,state in enumerate(solution):
        print(f'Step {step}:'); show(state)
