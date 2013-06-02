from emulator import *
from network import Network
from time import sleep

# make a network and draw it
network = Network()
n1 = network.add_node( 20, 20, 20 )
n2 = network.add_node( 25, 40, 0 )
network.add_edge( n1, n2, (255,0,0) )
display = Emulator(network)

# wait a bit, modify the network some way, and pass the updated network into the
# visualizer. eventually we will want to pass in the update data in some better/different
# format (e.g. as a serial stream of RGB values that are mapped onto the network
# structure already within the visualizer) rather than re-drawing the whole network every time.
sleep(1)
n3 = network.add_node( 5, 0, 40 )
network.add_edge( n1, n3, (0,255,0) )
display.update(network)