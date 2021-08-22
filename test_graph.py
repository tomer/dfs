from graph import Graph
import json


def test_graph_dump():
    data = {0: [1], 1: [2], 2: [3], 3: [1]}
    g = Graph(data)
    assert g.dump() == data


def test_graph_dump_graphviz():
    data = {0: [1], 1: [2], 2: [3], 3: [1]}
    g = Graph(data)
    assert 'digraph g {\n  0 -> 1\n  1 -> 2\n  2 -> 3\n  3 -> 1\n}' == g.dump_graphviz()


def test_graph_circles():
    g = Graph({1: [2], 2: [3], 3: [4], 4: [1]})
    assert g.find_circles() == [{1: 2, 2: 3, 3: 4, 4: 1}]


def test_graph_multiple_circles():
    g = Graph({1: [2], 2: [3, 2, 1], 3: [4], 4: [1]})
    assert g.find_circles() == [{4: 1, 1: 2, 2: 3, 3: 4}, {2: 2}, {2: 1, 1: 2}]


def test_graph_circles_from_json():
    with open('graph.json', 'r') as fh:
        g = Graph(json.load(fh))

    assert g.find_circles() == [{'quux': 'bar', 'bar': 'quux'}]
