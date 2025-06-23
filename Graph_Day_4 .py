                             Problem ---- Number Of Provinces (Leetcode)

There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Example 1:

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:

Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3

############################################# DFS ----Solution ###################################
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected [city][neighbor] ==1 and not visited[neighbor]:
                    dfs(neighbor)


        n = len(isConnected)
        visited = [False]*n
        provinces = 0
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces +=1

        return provinces


###################################### BFS ----Solution #############################################
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False]*n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                queue = deque()
                queue.append(city)
                visited[city] = True

                while queue:
                    current = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[current][neighbor] and not visited[neighbor]:
                            queue.append(neighbor)
                            visited[neighbor] = True


                provinces +=1

        return provinces
