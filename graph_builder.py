import networkx as nx

def build_graph(objects, links):
    g = nx.DiGraph()
    for o in objects: g.add_node(o['name'])
    for a, b in links: g.add_edge(a, b)
    return g

def find_cycles(g):
    return list(nx.simple_cycles(g))

def orphans(g):
    return [n for n in g.nodes if g.in_degree(n) == 0]
