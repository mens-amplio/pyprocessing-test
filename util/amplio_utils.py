import pyprocessing as pp
from random import random


def drawLEDs(network):
    for n in network.G.nodes_iter():
        pp.pushMatrix()
        pp.noStroke()
        pp.translate(*n.coords)
        pp.fill(pp.color(100, 100, 100)) #all nodes are grey for now
        #pp.sphere(1)
        pp.popMatrix()
    pp.strokeWeight(3)
    for e in network.G.edges_iter(data=True):
        pp.pushMatrix()
        pp.stroke( pp.color(*e[2]['color']) )
        (x1, y1, z1) = e[0].coords
        (x2, y2, z2) = e[1].coords
        pp.line( x1, y1, z1, x2, y2, z2 )
        pp.popMatrix()
        
