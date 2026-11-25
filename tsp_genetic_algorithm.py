"""Solve a small Travelling Salesperson Problem with a genetic algorithm."""
import random

CITIES = ("A", "B", "C", "D", "E")
DISTANCE = {
    "A": {"A": 0, "B": 12, "C": 10, "D": 19, "E": 8},
    "B": {"A": 12, "B": 0, "C": 3, "D": 7, "E": 6},
    "C": {"A": 10, "B": 3, "C": 0, "D": 6, "E": 20},
    "D": {"A": 19, "B": 7, "C": 6, "D": 0, "E": 4},
    "E": {"A": 8, "B": 6, "C": 20, "D": 4, "E": 0},
}


def route_length(route):
    """Length of a round trip, including the return to the starting city."""
    return sum(DISTANCE[route[i]][route[(i + 1) % len(route)]]
               for i in range(len(route)))


def order_crossover(parent1, parent2, rng):
    """Order crossover (OX), preserving a valid permutation of cities."""
    left, right = sorted(rng.sample(range(len(parent1)), 2))
    child = [None] * len(parent1)
    child[left:right + 1] = parent1[left:right + 1]
    remaining = [city for city in parent2 if city not in child]
    slots = list(range(right + 1, len(child))) + list(range(0, left))
    for slot, city in zip(slots, remaining):
        child[slot] = city
    return child


def genetic_tsp(cities=CITIES, population_size=80, generations=300,
                mutation_rate=0.15, seed=7):
    rng = random.Random(seed)
    cities = list(cities)
    population = [rng.sample(cities, len(cities)) for _ in range(population_size)]

    def select():
        contenders = rng.sample(population, min(4, len(population)))
        return min(contenders, key=route_length)

    for _ in range(generations):
        population.sort(key=route_length)
        next_population = [route[:] for route in population[:2]]  # elitism
        while len(next_population) < population_size:
            child = order_crossover(select(), select(), rng)
            if rng.random() < mutation_rate:
                i, j = rng.sample(range(len(child)), 2)
                child[i], child[j] = child[j], child[i]
            next_population.append(child)
        population = next_population

    best = min(population, key=route_length)
    return best, route_length(best)


if __name__ == "__main__":
    route, distance = genetic_tsp()
    print("Shortest route found:", " -> ".join(route + [route[0]]))
    print("Total distance:", distance)
