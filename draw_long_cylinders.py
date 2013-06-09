from emulator import *
from network import Network
from time import sleep
import math
import multiprocessing
import random
import time

# make a network and draw it
network = Network()

f = open("../modeling/tree.data.py")
data_tree = eval(f.read())

origin = network.add_node( 0, 0, 0 )

def resize_array(ary, index):
  while len(ary) < index + 1:
    ary.append(None)

def draw_tree(tree, below, lights_array = []):
  lights_tree = []
  for (index,rod,children) in tree:
    ((x1,y1,z1),(x2,y2,z2)) = rod
    n1 = network.add_node( x1, y1, z1 )
    n2 = network.add_node( x2, y2, z2 )
    edge = ( n1, n2 )
    resize_array(lights_array, index)
    lights_array[index] = edge
    network.add_edge( n1, n2, (255, 0, 0) )
    network.add_edge( below, n1, (255, 255, 255) )
    child_lights = draw_tree(children, n2, lights_array)
    lights_tree.append( (edge, rod, child_lights) )
  return lights_tree, lights_array

lights_tree, lights_array = draw_tree(data_tree, origin)

def select_light(ls, numbers):
  index = numbers[0]
  if len(ls) <= index:
    return None
  if len(numbers) > 1:
    return select_light(ls[index][2], numbers[1:])
  else:
    return ls[index][0]

light_number = select_light(data_tree, [1,1])
light = lights_array[light_number]
if light:
  network.add_edge(light[0], light[1], (0,100,255) )

print("ok")

# single-threaded, for now.
display = Emulator(network, False)
external_run(display.queue, display.network)
