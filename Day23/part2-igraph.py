from igraph import Graph

pairs = [tuple(line.strip().split("-")) for line in open("input.txt").read().split("\n")]
print(pairs[:10])

# Extract all unique nodes (vertices) from the edges
nodes = set()
for edge in pairs:
    nodes.update(edge)

# Create the graph
g = Graph()
g.add_vertices(list(nodes))
g.add_edges(pairs)

k = 0

while True:
    k += 1
    cliques = g.cliques(min=k, max=k)

    print(f"size: {k}, cliques: {len(cliques)}")

    if len(cliques) == 0:
        break

