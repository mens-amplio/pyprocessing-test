from network import Network
import multiprocessing
from visualizer import * # using any other import syntax breaks pyprocessing, booo

class Emulator:
    """
    An emulator that plots a visualization of the LEDs within 
    pyprocessing rather than pushing data to an LED strip
    """
    def __init__(self, network, threaded = True):
        self.network = network
        
        # launch pyprocessing sketch in separate process so its event loop won't block here
        self.queue = multiprocessing.Queue()
        if threaded:
          self.display_process = multiprocessing.Process(target=external_run, args=(self.queue,self.network))
          self.display_process.start()        
        
    def update(self, vals):
        # send values to pyprocessing process through queue
        self.queue.put(vals)
        
    def close(self):
        self.display_process.terminate()

        
        
