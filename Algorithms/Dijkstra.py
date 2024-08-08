from random import randint, uniform


class Node:
    """Class for comfortable working with vertexes"""

    def __init__(self, distance=None, prev=None):
        self.prev = prev
        self.distance = distance

    def __lt__(self, other):
        return self.distance < other.distance

    def __eq__(self, other):
        return other == self.distance


def dijkstra(adjacency_matrix, start_vertex: int, end_vertex: int, full_info: bool = False):
    """Dijkstra’s algorithm. Complexity: T(n) = O(m^2), memory-complexity: O(n).
    If param full_info is True, function returns tuple(T, P), where:
     T - array of distances for each vertex
     P - array of vertex paths from start_vertex to end_vertex.
    else returns only P."""
    n = len(adjacency_matrix)
    distances = {i: Node(distance=float("inf")) for i in range(n)}
    distances[start_vertex].distance = 0

    distances_temp = distances.copy()
    while len(distances_temp):
        curr_vertex_ind = min(distances_temp.items(), key=lambda x: x[1])[0]

        for neighbor_i, neighbor_vertex in enumerate(adjacency_matrix[curr_vertex_ind]):
            # Первое условие нужно для того,
            # чтобы не было ошибки KeyError для уже просмотренных (удаленных) вершин
            if neighbor_i in distances_temp:
                distance_to_neighbor = (
                    distances_temp[curr_vertex_ind].distance + neighbor_vertex
                )
                if distance_to_neighbor < distances_temp[neighbor_i].distance:
                    distances_temp[neighbor_i].distance = distance_to_neighbor
                    distances_temp[neighbor_i].prev = curr_vertex_ind
        distances_temp.pop(curr_vertex_ind)
        distances.update(distances_temp)

    path = [end_vertex]
    curr_vertex = end_vertex
    while curr_vertex != start_vertex:
        if distances[curr_vertex].prev is None:
            path = []
            break
        path.append(distances[curr_vertex].prev)
        curr_vertex = distances[curr_vertex].prev

    return [x.distance for x in distances.values()], (path[::-1] if full_info else path[::-1])


def print_matrix(matrix):
    """Help function for matrix visualisation"""
    for i in range(dimension):
        for j in range(dimension):
            print(matrix[i][j], end=", ")
        if i + 1 < dimension:
            print("\n", end="")
    print()


def test(matrix, start_vertex, end_vertex):
    """This is a test function from:
     1. https://www.youtube.com/watch?v=MCfjc_UIP1M&list=PLA0M1Bcd0w8yF0PO0eJ9v8VlsYEowmsnJ&index=3
     2. https://github.com/selfedu-rus/python-algorithms/blob/master/algorithm-dikstry.py
    :return: T, P, where
    - T is array of distances for each vertex,
    - P is array of vertex paths from start_vertex to end_vertex
    P.s. this function works only for start_vertex=0"""

    def arg_min(T, S):
        """Service method for test function"""
        amin = -1
        m = float("inf")  # максимальное значение
        for i, t in enumerate(T):
            if t < m and i not in S:
                m = t
                amin = i
        return amin

    N = len(matrix)  # число вершин в графе
    T = [float("inf")] * N  # последняя строка таблицы

    v = 0  # стартовая вершина (нумерация с нуля)
    S = {v}  # просмотренные вершины
    T[v] = 0  # нулевой вес для стартовой вершины
    M = [0] * N  # оптимальные связи между вершинами

    while v != -1:  # цикл, пока не просмотрим все вершины
        for j, dw in enumerate(matrix[v]):  # перебираем все связанные вершины с вершиной v
            if j not in S:  # если вершина еще не просмотрена
                w = T[v] + dw
                if w < T[j]:
                    T[j] = w
                    M[j] = v  # связываем вершину j с вершиной v

        v = arg_min(T, S)  # выбираем следующий узел с наименьшим весом
        if v >= 0:  # выбрана очередная вершина
            S.add(v)  # добавляем новую вершину в рассмотрение

    # формирование оптимального маршрута:
    start = start_vertex
    end = end_vertex
    P = [end]
    while end != start:
        end = M[P[-1]]
        P.append(end)
    return T, P[::-1] if T[end_vertex] != float("inf") else []


if __name__ == "__main__":
    print("Description of function dijkstra: ", dijkstra.__doc__, end="\n\n")
    iterations_count = 100
    dimension = 50
    max_distance = 100
    edge_probability = 0.45

    for i in range(1, iterations_count + 1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")

        # generate matrix
        matrix = [
            [
                randint(1, max_distance) if edge_probability > uniform(0, 1) else 0
                for _ in range(dimension)
            ]
            for _ in range(dimension)
        ]
        for i in range(dimension):
            for j in range(i, dimension):
                if i != j:
                    if matrix[i][j] == 0:
                        matrix[i][j] = float("inf")
                else:
                    matrix[i][i] = 0

        # algorithm test
        for i in range(len(matrix)):
            assert dijkstra(matrix, start_vertex=0, end_vertex=i, full_info=True) == test(
                matrix, start_vertex=0, end_vertex=i
            )

    print("\nTests passed!")
