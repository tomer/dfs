#!/usr/bin/env python3
from dataclasses import dataclass, field
from typing import Dict, List, Optional, OrderedDict, Set, Union

VertexNameType = Union[str, int]
VertexMapType = Dict[VertexNameType, VertexNameType]
VertexType = Dict[VertexNameType, List[VertexNameType]]


@dataclass
class DFS:
    white: List[VertexNameType] = field(
        default_factory=list)  # unvisited nodes
    gray: Set[VertexNameType] = field(default_factory=set)  # visiting nodes
    black: Set[VertexNameType] = field(default_factory=set)  # visited nodes
    travel: VertexMapType = field(
        default_factory=dict)  # Visiting map src->dst
    circles: List[VertexMapType] = field(default_factory=list)


class Graph:
    storage: VertexType = OrderedDict()

    def __init__(self, graph: Dict[VertexNameType, List[VertexNameType]]):
        # for name, edges in graph.items():
        #     vertex = Vertex()
        #     for child in edges:
        #         vertex.childs.add(child)
        #         #vertex.childs[child] = Edge()
        #     self.storage[name] = vertex
        self.storage = graph

    def dump(self) -> Dict[VertexNameType, List[VertexNameType]]:
        output: Dict[VertexNameType, List[VertexNameType]] = {}
        for name, childs in self.storage.items():
            output[name] = childs
        return output

    def dump_graphviz(self) -> str:
        output = 'digraph g {\n'
        for name, childs in self.storage.items():
            for child in childs:
                output += f'  {name} -> {child}\n'
        output += '}'
        return output

    def find_circles(self):
        buckets = DFS(white=list(self.storage.keys()))
        while buckets.white:
            current = buckets.white.pop()
            self.dfs(current, buckets)
        return buckets.circles

    def dfs(self, current: VertexNameType, buckets: DFS, parent: VertexNameType = None):
        buckets.gray.add(current)
        childs = self.storage[current]
        buckets.travel[parent] = current

        for child in childs:
            buckets.travel[current] = child
            if child in buckets.black:
                continue  # already visited, nothing to do
            elif child in buckets.gray:  # already visiting - circle detected
                circle = {current: child}
                next = child
                while next != current:
                    circle[next] = next = buckets.travel[next]
                buckets.circles.append(circle)

                del buckets.travel[current]

            elif child in buckets.white:  # Node not yet visited
                buckets.white.remove(child)
                self.dfs(child, buckets, parent=current)

        del buckets.travel[parent]

        buckets.gray.remove(current)
        buckets.black.add(current)


def main(argv: Optional[List[str]] = None) -> None:
    import argparse
    import json
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input', '-i', help='Graph input file', default='graph.json')
    parser.add_argument('--graphviz', action='store_true', default=False,
                        help='Format graph data for Graphviz. HINT: pipe to `dot -Tsvg | display`')
    args = parser.parse_args(argv)

    with open(args.input, 'r') as fh:
        graph = Graph(json.load(fh))

    if args.graphviz:
        print(graph.dump_graphviz())
    else:
        print(f'Input: {graph.dump()}')
        print(f'Circles: {graph.find_circles()}')


if __name__ == "__main__":
    main()
