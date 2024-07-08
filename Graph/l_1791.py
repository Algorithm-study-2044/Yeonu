class Solution(object):
    def findCenter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = defaultdict(int)
        for src, dst in edges:
            graph[src] += 1
            graph[dst] += 1
        n = len(graph.keys())
        for key, item in graph.items():
            if item == n-1:
                return key
                
        