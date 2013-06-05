from emulator import *
from network import Network
from time import sleep
import math

# make a network and draw it
network = Network()

f = open("../modeling/curve_endpoints.txt")
data = eval(f.read())

def distance_between(p1, p2):
  return math.sqrt(sum( map( lambda(s):s*s, map( lambda(x,y):x-y, zip(p1, p2) ) ) ))

def how_long(c):
  return distance_between(c[0], c[1])

def mean(lst):
  return float(sum(lst))/len(lst) if len(lst) > 0 else float('nan')

# kludge to get the model sorta near the origin
x_trans = 10
y_trans = -150

n1 = network.add_node( 0, 0, 0 )

cylinders = []
for c in data:
  x = how_long(c)
  if x > 17:
    cylinders.append(c)

neighborhoods = []
neighborhood_of_point = {}
for c in cylinders:
  for c_point in c:
    found_neighborhood = None
    for neighborhood in neighborhoods:
      if found_neighborhood:
        break
      for neighbor in neighborhood:
        if distance_between(c_point, neighbor) < 3:
          found_neighborhood = neighborhood
          break
    if not found_neighborhood:
      found_neighborhood = []
      neighborhoods.append(found_neighborhood)
    found_neighborhood.append(c_point)
    neighborhood_of_point[ tuple(c_point) ] = found_neighborhood

neighbor_centers = []
for neighborhood in neighborhoods:
  neighbor_centers.append([mean(axis) for axis in zip(*neighborhood)])

nodes = []
for center in neighbor_centers:
  nodes.append(network.add_node( center[0] - x_trans, center[1] - y_trans, center[2] ))

for c in cylinders:
  n = [nodes[neighborhoods.index(neighborhood_of_point[tuple(cp)])] for cp in c]
  network.add_edge( n[0], n[1], (255,0,0) )

print("ok")

# single-threaded, for now.
display = Emulator(network, False)
external_run(display.queue, display.network)
