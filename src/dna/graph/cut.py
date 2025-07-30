import random
from math import log

from .adjacency_list import AdjacencyListMapping, N, mutable_alm_copy


def karger_min(
    adjacency_list_mapping: AdjacencyListMapping[N], iterations: int = 0
) -> int:
    # would be neat to implement this with actual linked lists sometime
    malm = mutable_alm_copy(adjacency_list_mapping)
    n = len(malm)

    if iterations <= 0:
        iterations = int(n**2 * log(n))

    iterations *= 10
    # constant factor that gets supressed from asymptotic runtime,
    # but increases the probability of success

    def _karger_min(malm: dict[N, list[N]]) -> int:
        while len(malm) > 2:
            # Pick a random edge (v, w)
            v = random.choice(list(malm.keys()))
            w = random.choice(malm[v])

            # Merge w into v
            malm[v].extend(malm[w])

            # Replace all appearances of w with v
            for node in malm[w]:
                malm[node] = [v if i == w else i for i in malm[node]]

            # Remove self-loops
            malm[v] = [i for i in malm[v] if i != v]

            # Delete node w
            del malm[w]

        # Return the number of edges between the two remaining nodes
        return len(next(iter(malm.values())))

    return min(_karger_min(malm) for _ in range(iterations))
