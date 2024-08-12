from random import randint, uniform


def kruskal(adjacency_matrix):
    """Algorithm for constructing a minimum spanning tree for an undirected graph.
    Complexity: T(n) = O(V^2), memory-complexity: O(V^2), where V - number of vertexes.
    Returns list of tuple(vertex_i, vertex_j, edge_length).
    P.s. T(n) = O(V^2) instead of O(V*log_V) because of matrix transformation to the array of edges"""
    vertex_edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] != float('inf'):
                vertex_edges.append((i, j, adjacency_matrix[i][j]))
    vertex_edges.sort(key=lambda x: x[2])

    visited_vertexes = set()
    vertex_groups = {}
    for i, j, edge_len in vertex_edges:
        if i not in visited_vertexes and j not in visited_vertexes:
            visited_vertexes.add(i)
            visited_vertexes.add(j)
            vertex_groups[i] = vertex_groups[j] = {}
            vertex_groups[i]['vertexes_list'] = vertex_groups[j]['vertexes_list'] = [i, j]
            vertex_groups[i]['vertex_edges'] = vertex_groups[j]['vertex_edges'] = [(i, j, edge_len)]
            
        elif i in visited_vertexes and j not in visited_vertexes\
                or i not in visited_vertexes and j in visited_vertexes:
            current_vertex_group = i if i in visited_vertexes else j
            vertex_to_add = j if i in visited_vertexes else i
            vertex_groups[vertex_to_add] = {}            
            visited_vertexes.add(vertex_to_add)

            vertex_groups[current_vertex_group]['vertexes_list'].append(vertex_to_add)
            vertex_groups[vertex_to_add]['vertexes_list'] = vertex_groups[current_vertex_group]['vertexes_list']

            vertex_groups[current_vertex_group]['vertex_edges'].append((i, j, edge_len))
            vertex_groups[vertex_to_add]['vertex_edges'] = vertex_groups[current_vertex_group]['vertex_edges'] # теперь ссылается на другой список и подтягивает все изменения

    to_return = set()
    for i, j, edge_len in vertex_edges:
            if vertex_groups[i]['vertexes_list'] != vertex_groups[j]['vertexes_list']:
                vertex_groups[i]['vertexes_list'] += vertex_groups[j]['vertexes_list']
                vertex_groups[i]['vertex_edges'] += vertex_groups[j]['vertex_edges'] + [(i, j, edge_len)]  # !!
                vertex_groups[i]['vertex_edges'] = list(set(vertex_groups[i]['vertex_edges']))
 
                for vertex in vertex_groups[i]['vertexes_list'] + vertex_groups[i]['vertexes_list']:
                    vertex_groups[vertex]['vertexes_list'] = vertex_groups[i]['vertexes_list']
                    vertex_groups[vertex]['vertex_edges'] = vertex_groups[i]['vertex_edges']

                               
 
    to_return = set(vertex_groups[list(vertex_groups.keys())[0]]['vertex_edges'])
    return to_return


def test(adjacency_matrix):
    # Алгоритм Краскала поиска минимального остова графа
    import queue  
    class Graph:  
        def __init__(self, vertices):  
            self.vertices = vertices  
            self.edges = []  
            self.parent = {}  
            self.rank = {}  
      
            for v in self.vertices:  
                self.make_set(v)  
      
        def add_edge(self, u, v, w):  
            self.edges.append((w, u, v))  
      
        def make_set(self, v):  
            self.parent[v] = v  
            self.rank[v] = 0  
      
        def find(self, v):  
            if self.parent[v] != v:  
                self.parent[v] = self.find(self.parent[v])  
            return self.parent[v]  
      
        def union(self, u, v):  
            root1 = self.find(u)  
            root2 = self.find(v)  
      
            if root1 != root2:  
                if self.rank[root1] > self.rank[root2]:  
                    self.parent[root2] = root1  
                else:  
                    self.parent[root1] = root2  
                    if self.rank[root1] == self.rank[root2]:  
                        self.rank[root2] += 1  
      
        def kruskal(self):  
            minimum_spanning_tree = set()  
      
            # Sort edges by weight using priority queue  
            edge_queue = queue.PriorityQueue()  
            for edge in self.edges:  
                edge_queue.put(edge)  
      
            # Iterate through edges in priority queue and add to MST  
            while not edge_queue.empty():  
                weight, u, v = edge_queue.get()  
      
                if self.find(u) != self.find(v):  
                    self.union(u, v)  
                    minimum_spanning_tree.add((u, v, weight))  
      
            return minimum_spanning_tree  
    # Create a graph with 5 vertices  
    g = Graph(list(range(len(adjacency_matrix))))
    
    vertex_edges = []
    for i in range(len(adjacency_matrix)):
        for j in range(i + 1, len(adjacency_matrix)):
            if adjacency_matrix[i][j] != float('inf'):
                vertex_edges.append((i, j, adjacency_matrix[i][j]))
    vertex_edges.sort(key=lambda x: x[2])
      
    # Add edges to the graph  
    for edge in vertex_edges:
        g.add_edge(*edge)  
      
    return g.kruskal()


def print_matrix(matrix):
    """Help function for matrix visualisation"""
    print('[' + ',\n'.join(['[' + ', \t'.join([str(matrix[i][j]) for j in range(dimension)]) + ']' for i in range(dimension)]) + ']')


if __name__ == '__main__':
    print("Description of function kruskal: ", kruskal.__doc__, end='\n\n')
    iterations_count = 100
    dimension = 50
    max_distance = 200
    edge_probability = 0.5

    for i in range(1, iterations_count+1):
        if i % 10 == 0:
            print(f"Iteration {i}/{iterations_count}")

        # generate matrix
        matrix = [[randint(1, max_distance) if edge_probability > uniform(0, 1) else 0
                   for _ in range(dimension)] for _ in range(dimension)]
        for i in range(dimension):
            for j in range(i, dimension):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')
                matrix[j][i] = matrix[i][j]
                matrix[i][i] = 0
        
        # algorithm test
        assert kruskal(matrix) == test(matrix)

    print("\nTests passed!")
