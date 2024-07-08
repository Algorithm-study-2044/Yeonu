from collections import deque
class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        if source == destination:
            return True

        graph = defaultdict(list)
        
        for src, dst in edges:
            graph[src].append(dst)
            graph[dst].append(src)
        
        result = [False]
        visited = set()
        visited.add(source)
        queue = deque()
        queue.append(source)

        while queue:
            target = queue.pop()

            if target == destination:
                return True
            
            for item in graph[target]:
                if item in visited:
                    continue
                queue.append(item)
                visited.add(item)

        return result[0]

        