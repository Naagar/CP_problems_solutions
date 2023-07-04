# Single Source Shortest Path Problem

class graph:
    def __init__(self, g_dist=None):
        if g_dist is None:
            g_dist = {}
        self.g_dist =g_dist

    def bfs(self, start, end):
        queue = []
        queue.append([start])

        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            
            for adjcent in self.g_dist.get(node, []):
                new_path =list(path)
                new_path.append(adjcent)
                queue.append(new_path)
custom_dist = {'a': ['b','c'],
                'b' : ['d', 'g'],
                'c' : ['d', 'e'],
                'd' : ['f'],
                'e' : ['f'],
                'g' : ['f'], 
                }
g = graph(custom_dist)
print(g.bfs('a', 'e'))