import networkx as nx

class Node:
    def __init__(self, x, y, z):
        self.coords = (x, y, z)
        
class Network:
    """
    Right now this is just a wrapper for NetworkX that doesn't do anything useful
    """
    def __init__(self):
        self.G=nx.DiGraph()
        
    def add_node(self, x, y, z):
        node = Node(x,y,z)
        self.G.add_node(node)
        return node
        
    def add_edge(self, led1, led2, rgb):
        self.G.add_edge(led1, led2, color = rgb)