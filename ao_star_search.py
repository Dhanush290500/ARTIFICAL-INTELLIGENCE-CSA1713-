"""AO* search for a finite, acyclic AND-OR graph.

Each node maps to a list of alternatives (hyperarcs). The children within an
alternative are AND-connected; the alternatives are OR-connected. Costs are
non-negative edge costs. The solver propagates the least-cost solved choice
back to the start and prints the selected solution graph.
"""
from math import inf

# For each node, each tuple is one way to solve it. Children in a tuple must
# all be solved (AND); choosing between tuples is an OR decision.
GRAPH = {
    "start": [('a',), ('b', 'c')],
    "a": [('d',), ('e',)],
    "b": [('f',)],
    "c": [('g',)],
    "d": [], "e": [], "f": [], "g": [],
}
EDGE_COST = {
    ("start", "a"): 1, ("start", "b"): 1, ("start", "c"): 1,
    ("a", "d"): 2, ("a", "e"): 1,
    ("b", "f"): 2, ("c", "g"): 2,
}
TERMINALS = {"d", "e", "f", "g"}


def ao_star(start, graph=GRAPH, edge_cost=EDGE_COST, terminals=TERMINALS):
    """Return (minimum solution cost, selected AND-OR solution structure)."""
    memo = {}
    active = set()

    def solve(node):
        if node in terminals:
            return 0, node
        if node in memo:
            return memo[node]
        if node in active:
            raise ValueError(f"Cycle detected at {node!r}; this demo expects a DAG")
        if node not in graph or not graph[node]:
            return inf, None
        active.add(node)
        best_cost, best_choice = inf, None
        for alternative in graph[node]:
            total, children = 0, []
            for child in alternative:
                child_cost, child_solution = solve(child)
                total += edge_cost.get((node, child), 1) + child_cost
                children.append(child_solution)
            if total < best_cost:
                best_cost, best_choice = total, tuple(children)
        active.remove(node)
        memo[node] = (best_cost, (node, best_choice))
        return memo[node]

    cost, solution = solve(start)
    if solution is None:
        raise ValueError(f"No solution exists from {start!r}")
    return cost, solution


def show_solution(solution, indent=0):
    node, children = solution
    print("  " * indent + node)
    if children:
        for child in children:
            if isinstance(child, tuple):
                show_solution(child, indent + 1)
            else:
                print("  " * (indent + 1) + str(child))


if __name__ == "__main__":
    cost, solution = ao_star("start")
    print(f"Minimum solution cost: {cost}")
    print("Selected solution graph:")
    show_solution(solution)
