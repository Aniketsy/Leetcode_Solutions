🧩 Sample Problem Statement:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges, 
return the number of connected components in the graph.

######## Brute Force Approach --- Adjacency Matrix + DFS  ###############  T.C = O(n^2) , S.C = O(n^2)

"First, I’d try the brute-force approach using an adjacency matrix and DFS. Although not space-efficient, it helps to visualize the problem."
Logic:
   Build an n x n matrix to represent the graph.

   For every node not visited, run DFS and mark all reachable nodes.

  Count how many times DFS is initiated — this equals the number of components.

Code :
def countComponents(n, edges):
    # Step 1: Create an adjacency matrix of size n x n initialized with 0
    adj = [[0]*n for _ in range(n)]
    
    # Step 2: Fill the adjacency matrix for undirected graph
    for u, v in edges:
        adj[u][v] = adj[v][u] = 1  # Mark both directions since the graph is undirected

    # Step 3: Initialize a visited array to keep track of visited nodes during DFS
    visited = [False] * n

    # Step 4: Define a DFS function to traverse all nodes in a connected component
    def dfs(node):
        visited[node] = True  
        for neighbor in range(n):  
            if adj[node][neighbor] == 1 and not visited[neighbor]:
                dfs(neighbor)

    # Step 5: Count connected components
    count = 0  
    for i in range(n):
        if not visited[i]:  # If node i hasn't been visited, it's a new component
            dfs(i)  # Perform DFS to visit all nodes in this component
            count += 1  
   
    return count

################## Improved Approach ------ Adjacency List + DFS ####################  T.C = O(n+E), S.C = O(n+E)

from collections import defaultdict

def countComponents(n, edges):
    # Step 1: Create an adjacency list using defaultdict
    graph = defaultdict(list)
   
    for u, v in edges:
        graph[u].append(v)  # Add v to u's adjacency list
        graph[v].append(u)  # Add u to v's adjacency list (because it's an undirected graph)
   
    visited = set()

    def dfs(node):
        for neighbor in graph[node]:  
            if neighbor not in visited:
                visited.add(neighbor)  
                dfs(neighbor)         

    count = 0  # Initialize component count
    for i in range(n):
        if i not in visited:  
            visited.add(i)    
            dfs(i)           
            count += 1        
          
    return count

#################### Optimal Approach ------Union-Find(Disjoint Set Union ) T.C = O(E * alpha(N)) , S.C = O(N)

def countComponents(n, edges):
    # Step 1: Initialize each node to be its own parent (self-loop)
    parent = [i for i in range(n)]  # Initially, every node is its own component

    # Step 2: Define the 'find' function with path compression
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression for optimization
        return parent[x]

    # Step 3: Define the 'union' function to merge two sets
    def union(x, y):
        rootX, rootY = find(x), find(y)  # Find roots of both nodes
        if rootX != rootY:
            parent[rootY] = rootX  # Merge the two components by updating the root

    # Step 4: Apply union for each edge
    for u, v in edges:
        union(u, v)

    # Step 5: Count unique roots — each unique root is a separate connected component
    return len(set(find(i) for i in range(n)))


#############################################################################

🗣️ How to Wrap Up Your Answer in the Interview:
"So, I began with a brute-force matrix-based DFS, which is space-heavy. 
Then I moved to an adjacency list for better efficiency. 
Finally, I used Union-Find for optimal time complexity, especially useful when the graph is large or changes dynamically.
The final solution gives us the best trade-off between simplicity and performance."



