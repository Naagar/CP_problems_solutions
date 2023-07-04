# graph.py
# BFS: frist near neighbours, then second neighbours and so on. QUEUE
# DFS: traversing the graph data str and explore as far as possible before backtracking STACK
''' Algo.
    push any string vertex 
        while tack is not empty
            p = pop()
            if p is unvisited
                mark it visited
                push all adjacent
                unvisited vertices of p
'''
class graph:
    def __init__(self, g_dict=None):
        if g_dict is None:
            g_dict = {}
        self.g_dict = g_dict
    def add_edge(self, vertex, edge):
        self.g_dict[vertex].append(edge)
    def bfs(self, vertex):
        visited = [vertex]
        queue   = [vertex]
        while queue:
            de_vertex = queue.pop(0)
            print(de_vertex)
            for adjacent_vertex in self.g_dict[de_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    queue.append(adjacent_vertex)
    def dfs(self, vertex):
        visited = [vertex]
        stack   = [vertex]
        while stack:
            pop_vertex = stack.pop()
            print(pop_vertex)
            for adjacent_vertex in self.g_dict[pop_vertex]:
                if adjacent_vertex not in visited:
                    visited.append(adjacent_vertex)
                    stack.append(adjacent_vertex)


cust_dict = {'a': ['b','c'],
             'b':['a','d', 'e'],
             'c': ['a', 'e'],
             'd': ['b', 'e', 'f'],
             'e': ['d', 'f', 'c'],
             'f': ['d', 'e']
                 }
graph = graph(cust_dict)
graph.dfs('a')