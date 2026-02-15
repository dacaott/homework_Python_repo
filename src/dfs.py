class Graph:
    def init(self):
        self.adj = {}
        self._dfs_order = None  # порядок обхода для итерации

    def add_vertex(self, v):
        if v not in self.adj:
            self.adj[v] = []

    def add_edge(self, u, v):
        self.add_vertex(u)
        self.add_vertex(v)
        self.adj[u].append(v)
        self.adj[v].append(u)

    def dfs(self, start):
        visited = set()
        order = []

        def _dfs(v):
            visited.add(v)
            order.append(v)
            for nxt in self.adj[v]:
                if nxt not in visited:
                    _dfs(nxt)

        _dfs(start)
        self._dfs_order = order  # граф станет итерируемым в этом порядке
        return order

    def iter(self):
        # итерируем граф в порядке последнего DFS
        if self._dfs_order is None:
            raise RuntimeError(
                "Сначала нужно вызвать dfs(), чтобы определить порядок итерации"
            )
        return iter(self._dfs_order)
