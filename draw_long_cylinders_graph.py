from emulator import *
from network import Network
from time import sleep
import math
import multiprocessing
import random
import time

# make a network and draw it
network = Network()

f = open("../modeling/graph.data.py")
data = eval(f.read())

node_by_id = {}

for point_id, point in data["nodes"].items():
  node = network.add_node( *point )
  node_by_id[point_id] = node

edge_by_id = {}

for edge_id, edge_pair in data["edges"].items():
  node = network.add_node( *point )
  n1, n2 = edge_pair
  network.add_edge( node_by_id[n1], node_by_id[n2], (255,0,0))

# single-threaded, for now.
display = Emulator(network, False)
external_run(display.queue, display.network)
