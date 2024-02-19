from random import randint, uniform
from Dijkstra import dijkstra  # for testing Floyd-Warshall algorithm


def floyd_warshall(adjacency_matrix, return_history_matrix=False):
    """Floyd-Warshall’s algorithm. Complexity: T(n) = O(V^3), memory-complexity: O(V^2), where V - number of vertexes.
    If return_history_matrix=True, function returns tuple(adjacency_matrix, history), where:
       adjacency_matrix - matrix of shortest distances
         (i-th j-th element is the length of the shortest distance from the i-th vertex to the j-th vertex)
       history - is a matrix, the i-j-th element of which contains the number of the vertex
         to which one must go from vertex i in order to get to vertex j in the shortest way.
    else returns only adjacency_matrix.
    P.s. Doesn't work for the case of loops at the starting vertex (but loops in other vertexes is allowed)
    P.s.s. Also works with directed graphs"""
    adjacency_matrix = [x.copy() for x in adjacency_matrix]
    n = len(adjacency_matrix)
    history = [[j for j in range(n)] for _ in range(n)]

    for C in range(n):
        for A in range(n):
            for B in range(n):
                if adjacency_matrix[A][B] > adjacency_matrix[A][C] + adjacency_matrix[C][B]:
                    adjacency_matrix[A][B] = adjacency_matrix[A][C] + adjacency_matrix[C][B]
                    history[A][B] = history[A][C]
    return (adjacency_matrix, history) if return_history_matrix else adjacency_matrix


def get_path_by_history_matrix(history, start_vertex, end_vertex):
    """Help function for floyd_warshall. Helps find the path from start_vertex to end_vertex using the history matrix.
    Can work infinity because of negative cycles in graph"""
    path = [start_vertex]
    next_vertex = start_vertex
    while next_vertex != end_vertex:
        next_vertex = history[next_vertex][end_vertex]
        path.append(next_vertex)
    return path


def print_matrix(matrix):
    """Help function for matrix visualisation"""
    print('[' + ',\n'.join(['[' + ', '.join([str(matrix[i][j]) for j in range(dimension)]) + ']' for i in range(dimension)]) + ']')


if __name__ == '__main__':
    print("Description of function floyd_warshall: ", floyd_warshall.__doc__, end='\n\n')
    iterations_count = 100
    dimension = 20
    max_distance = 100
    edge_probability = 0.5

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")

        # generate matrix
        matrix = [[randint(1, max_distance) if edge_probability > uniform(0, 1) else 0
                   for _ in range(dimension)] for _ in range(dimension)]
        for i in range(dimension):
            for j in range(dimension):  # range(i, dimension):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')
                matrix[i][i] = 0

        # algorithm test
        adjacency_matrix, history = floyd_warshall(matrix, return_history_matrix=True)
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                path = get_path_by_history_matrix(history, i, j)
                assert adjacency_matrix[i] == dijkstra(matrix, i, j, full_info=True)[0]

    print("\nTests passed!")
