from collections import defaultdict
from copy import deepcopy
from graphviz import Digraph
import uuid

input = open("input.txt").read().split("\n\n")
wires_in = ([wire.split(": ") for wire in input[0].split("\n")])

instructions = [instruction.replace(" ->", "").split(" ") for instruction in input[1].split("\n")]

wires = defaultdict(int)

for wire in wires_in:
    wires[wire[0]] = int(wire[1])

dot = Digraph()

for wire in wires:
    dot.node(wire)

for instruction in instructions:
    node_id = str(uuid.uuid4()) 
    dot.node(node_id, instruction[1], shape='rectangle')
    if instruction[0] < instruction[2]:
        dot.edge(instruction[0], node_id)
        dot.edge(instruction[2], node_id)
    else:
        dot.edge(instruction[2], node_id)
        dot.edge(instruction[0], node_id)
    dot.edge(node_id, instruction[3])

dot.render('output_graph', format='png')  # Saves as output_graph.png
print(dot.source) 




