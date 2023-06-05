class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_matrix = [[0 for i in range(vertices)] for j in range(vertices)]
        
    def add_edge(self, u, v):
        self.adj_matrix[u][v] = 1
        self.adj_matrix[v][u] = 1
        
    def is_safe(self, vertex, path, pos):
        if self.adj_matrix[path[pos-1]][vertex] == 0:
            return False
        
        for i in range(pos):
            if path[i] == vertex:
                return False
            
        return True
    
    def ham_cycle_util(self, path, pos):
        if pos == self.vertices:
            if self.adj_matrix[path[pos-1]][path[0]] == 1:
                return True
            else:
                return False
            
        for v in range(1,self.vertices):
            if self.is_safe(v, path, pos):
                path[pos] = v
                if self.ham_cycle_util(path, pos+1):
                    return True
                path[pos] = -1
                
        return False
    
    def hamiltonian_cycle(self):
        path = [-1]*self.vertices
        path[0] = 0
        if not self.ham_cycle_util(path, 1):
            print("No solution exists")
            return False
        print(path)
        return True
