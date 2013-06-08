from emulator import *
from network import Network
from time import sleep
import math

# make a network and draw it
network = Network()

f = open("../modeling/tree.data.py")
data = eval(f.read())

origin = network.add_node( 0, 0, 0 )

def draw_tree(tree, below):
  roots = []
  for (rod,children) in tree:
    ((x1,y1,z1),(x2,y2,z2)) = rod
    n1 = network.add_node( x1, y1, z1 )
    n2 = network.add_node( x2, y2, z2 )
    roots.append(n1)
    network.add_edge( n1, n2, (255, 0, 0) )
    network.add_edge( below, n1, (0, 255, 255) )
    child_nodes = draw_tree(children, n2)
  return roots

draw_tree(data, origin)

#network.add_edge( n[0], n[1], (255,0,0) )

print("ok")

# single-threaded, for now.
display = Emulator(network, False)
external_run(display.queue, display.network)
