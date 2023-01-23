# graph related problems

from typing import List, Optional
from collections import defaultdict, deque
from graph_graph import show_graph, to_adjacency_list, dfs_print, bfs_print


# graph = [[0, 1], [1, 2], [2, 0]]
# graph = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        """
        1971. Find if Path Exists in Graph
        """

        def to_adjacency_list(edges):
            graph = defaultdict(list)
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
            return dict(graph)

        graph = to_adjacency_list(edges)

        visited = {source}
        q = deque([source])
        while q:
            current = q.popleft()
            # print(current)
            if current == destination:
                return True
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
        return False


# graph = {
#     'f': ['g', 'i'],
#     'g': ['h'],
#     'h': [],
#     'i': ['g', 'k'],
#     'j': ['i'],
#     'k': []
# }

n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

n = 6
edges = [[0, 1], [0, 2], [3, 5], [5, 4], [4, 3]]
source = 0
destination = 5

edges = [[4, 3], [1, 4], [4, 8], [1, 7], [6, 4], [4, 2], [7, 4], [4, 0], [0, 9], [5, 4]]
source = 3
destination = 7

s = Solution()
print(s.validPath(n, edges, source, destination))


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        """
        323 Number of Connected Components in an Undirected Graph
        """

        def build_graph(edges):
            graph = defaultdict(list)
            for e in edges:
                graph[e[0]].append(e[1])
                graph[e[1]].append(e[0])
            return dict(graph)

        def dfs(graph, src, visited):
            if src in visited:
                return False
            visited.add(src)
            for neighbor in graph[src]:
                dfs(graph, neighbor, visited)
            return True

        visited = set()
        count = 0

        graph = build_graph(edges)
        for node in graph:
            if dfs(graph, node, visited):
                count += 1
        return count


n, edges = 5, [[0, 1], [1, 2], [3, 4]]
# graph = to_adjacency_list(edges)
# print(graph)
# show_graph(edges)
s = Solution()
print(s.countComponents(n, edges))


class Solution:
    def largest_component(self, graph: dict) -> int:
        def dfs(graph, src, visited):
            if src in visited:
                return 0
            visited.add(src)
            size = 1
            for neighbor in graph[src]:
                size += dfs(graph, neighbor, visited)
            return size

        visited = set()
        lgst = 0
        for node in graph:
            lgst = max(lgst, dfs(graph, node, visited))
        return lgst


graph = {
    0: [8, 1, 5],
    1: [0],
    5: [0, 8],
    8: [0, 5],
    2: [3, 4],
    3: [2, 4],
    4: [3, 2]
}

# graph = {
#     3: [],
#     4: [6],
#     6: [4, 5, 7, 8],
#     8: [6],
#     7: [6],
#     5: [6],
#     1: [2],
#     2: [1]
# }

s = Solution()
print(s.largest_component(graph))


# show_graph(graph)

class Solution:
    def shortest_path(self, edges, node_A, node_B):
        """
        """
        graph = to_adjacency_list(edges)
        q = deque([(node_A, 0)])
        visited = {node_A}

        while q:
            current, distance = q.popleft()
            if current == node_B:
                return distance
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append((neighbor, distance + 1))
        return -1

edges = [
    ['w', 'x'],
    ['x', 'y'],
    ['z', 'y'],
    ['z', 'v'],
    ['w', 'v']
]
src, dst = 'w', 'y'

s = Solution()
print(s.shortest_path(edges, src, dst))

graph = to_adjacency_list(edges)
print(graph)
show_graph(graph)
