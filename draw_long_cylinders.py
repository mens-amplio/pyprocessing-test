from emulator import *
from network import Network
from time import sleep
import math

# make a network and draw it
network = Network()

f = open("../modeling/cylinder_endpoints.txt")
data = eval(f.read())

def how_long(c):
  return math.sqrt(sum( map( lambda(s):s*s, map( lambda(x,y):x-y, zip(c[0], c[1]) ) ) ))

# kludge to get the model sorta near the origin
x_trans = 10
y_trans = -150

n1 = network.add_node( 0, 0, 0 )

for c in data:
  x = how_long(c)
  if x > 17:
    n1 = network.add_node( c[0][0] - x_trans, c[0][1] - y_trans, c[0][2] )
    n2 = network.add_node( c[1][0] - x_trans, c[1][1] - y_trans, c[1][2] )
    network.add_edge( n1, n2, (255,0,0) )

print("ok")

# single-threaded, for now.
display = Emulator(network, False)
external_run(display.queue, display.network)
