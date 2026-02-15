from src.dfs import Graph


def test_dfs_order():
    g = Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(2, 4)
    g.add_edge(2, 5)

    result = g.dfs(1)
    assert result == [1, 2, 4, 5, 3]


def test_iteration_after_dfs():
    g = Graph()
    g.add_edge("A", "B")
    g.add_edge("A", "C")
    g.add_edge("B", "D")

    order = g.dfs("A")
    assert list(g) == order
