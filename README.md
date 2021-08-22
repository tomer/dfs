# DFS Algorithm implementation in Python

## Usage

From the command line. Use `--input` to specify a different graph file.

```
usage: graph.py [-h] [--input INPUT] [--graphviz]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Graph input file
  --graphviz            Format graph data for Graphviz. HINT: pipe to `dot
                        -Tsvg | display`
```

**Graphical visualization** of the graph is provided by graphviz, and can be displayed using the command below if the `graphviz` and `imagemagick` packages are installed.

```
$ ./graph.py --input graph.json --graphviz | graphviz -Tsvg | display
```

## Tests

This repository provides tests created for the Pytest testing framework.
