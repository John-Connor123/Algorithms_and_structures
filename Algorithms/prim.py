from random import randint, uniform
from numba import jit
import math


def prim(adjacency_matrix):
    """Algorithm for constructing a minimum spanning tree for an undirected graph.
    Complexity: T(n) = O(V^2), memory-complexity: O(V^2), where V - number of vertexes.
    Returns set of tuple(vertex_i, vertex_j, edge_length)."""
    edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] != -1:
                edges.append((i, j, adjacency_matrix[i][j]))
    edges.sort(key=lambda x: x[2])
    
    minimum_egdes = set()
    visited_vertexes = {0}
    for _ in range(len(adjacency_matrix)):  # while
        for i, j, edge_length in edges:
            if i in visited_vertexes and j not in visited_vertexes: 
                minimum_egdes.add((i, j, edge_length))
                visited_vertexes.add(j)
                break
            elif j in visited_vertexes and i not in visited_vertexes: 
                minimum_egdes.add((i, j, edge_length))
                visited_vertexes.add(i)
                break

    return minimum_egdes
             

def test(adjacency_matrix):
    # Алгоритм Прима поиска минимального остова графа
    def get_min(R, U):
            rm = (math.inf, -1, -1)
            for v in U:
                rr = min(R, key=lambda x: x[0] if (x[1] == v or x[2] == v) and (x[1] not in U or x[2] not in U) else math.inf)
                if rm[0] > rr[0]:
                    rm = rr
            return rm

    R = []
    for i in range(len(adjacency_matrix)):
        for j in range(i+1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] != -1:
                R.append((adjacency_matrix[i][j], i, j))
    R.sort(key=lambda x: x[0])
    R = [(math.inf, -1, -1)] + R

    N = len(adjacency_matrix)    # число вершин в графе
    U = {0}   # множество соединенных вершин
    T = []    # список ребер остова
    while len(U) < N:
        r = get_min(R, U)       # ребро с минимальным весом
        if r[0] == math.inf:    # если ребер нет, то остов построен
            break

        T.append(r)             # добавляем ребро в остов
        U.add(r[1])             # добавляем вершины в множество U
        U.add(r[2])

    T = set([(i, j, edge_length) for edge_length, i, j in T])
    return T


def print_matrix(matrix):
    """Help function for matrix visualisation"""
    print('[' + ',\n'.join(['[' + ', \t'.join([str(matrix[i][j]) for j in range(dimension)]) + ']' for i in range(dimension)]) + ']')


@jit(nopython=True)
def get_random_matrix(dimension, max_distance, edge_probability, is_directed=False):
    matrix = [[randint(1, max_distance) if edge_probability > uniform(0, 1) else 0
              for _ in range(dimension)] for _ in range(dimension)]
    for i in range(dimension):
        for j in range(i if not is_directed else 0, dimension):
            if matrix[i][j] == 0:
                matrix[i][j] = -1
            if not is_directed:
                matrix[j][i] = matrix[i][j]
            matrix[i][i] = 0
    return matrix


def has_cycle(adjacency_matrix, edge, visited, parent=-1):
    visited[edge] = True
    for j in range(len(adjacency_matrix)): # i + 1
        if j not in (i, parent) and adjacency_matrix[edge][j] != -1:
            if visited[j]:
                raise 
            has_cycle(adjacency_matrix, j, visited, edge)


if __name__ == '__main__':
    print("WARNING:")
    print("""The test function is an order of magnitude slower than the prim function. 
    In reality, the prim function produces results in a fraction of a second when dimension=1000.""")
    print("\nDescription of function prim: ", prim.__doc__, end='\n\n')
    iterations_count = 100
    dimension = 20
    max_distance = 200
    edge_probability = 0.5

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")

        # generate matrix
        matrix = get_random_matrix(
                                dimension=dimension, 
                                max_distance=max_distance, 
                                edge_probability=edge_probability, 
                                is_directed=False)

        # algorithm test
        res1 = prim(matrix)
        res2 = test(matrix)
        try:
            assert res1 == res2
        except AssertionError:
            # If algorithm constructed other spanning tree
            if sum([edge[2] for edge in res1]) != sum([edge[2] for edge in res2]):
                raise AssertionError

            span_tree = [[-1 for _ in range(dimension)] for _ in range(dimension)]
            for i, j, edge_length in res1:
                span_tree[j][i] = span_tree[i][j] = edge_length
            
            for i in range(dimension):
                visited = dict.fromkeys(range(dimension), False)
                if has_cycle(span_tree, i, visited):
                    raise AssertionError
            
    print("\nTests passed!")
