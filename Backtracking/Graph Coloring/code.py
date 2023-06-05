class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        
    def is_safe(self, vertex, color, color_list):
        for i in range(self.vertices):
            if self.adj_matrix[vertex][i] == 1 and color_list[i] == color:
                return False
        return True
    
    def graph_color_util(self, num_colors, color_list, vertex):
        if vertex == self.vertices:
            return True
        
        for c in range(1, num_colors+1):
            if self.is_safe(vertex, c, color_list):
                color_list[vertex] = c
                if self.graph_color_util(num_colors, color_list, vertex+1):
                    return True
                color_list[vertex] = 0
                
    def graph_coloring(self, num_colors):
        color_list = [0]*self.vertices
        if not self.graph_color_util(num_colors, color_list, 0):
            return False
        print(color_list)
        return True
