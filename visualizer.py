import pyprocessing as pp
from util.arcball import ArcBall
from util.amplio_utils import drawLEDs

"""
Visualizer for LED effects for Mens Amplio project.
Uses Arcball class by Martin Prout for 3D rotation - see https://github.com/monkstone/pyprocessing-experiments
"""
X = 0
Y= 1
Z = 2
queue = None
network = None

def external_run(q, n):
    """
    Call this instead of calling run() directly when running this module in its own process
    """
    global queue
    queue = q
    global network
    network = n
    pp.run()

def setup():
    pp.size(600, 600)
    global arcball
    arcball = ArcBall(width/2.0, height/2.0, min(width - 20, height - 20) * 0.5)
    arcball.axis = -1
    
def set_values(input_network):
    global network
    network = input_network

def draw():
    pp.background(0x000000)
    pp.translate(width/2.0, height/2.0, -height/4.0)
    defineLights()
    update()
    pp.lights()
    try:
        data = queue.get_nowait()
        if data:
            set_values(data)
    except:
        pass
    drawLEDs(network)
    
def update():
    """
    wrap arcball update and rotation as a local function
    """
    theta,  x,  y,  z = arcball.update()
    pp.rotate(theta,  x,  y,  z)    

def mousePressed():
    arcball.mousePressed(pp.mouse.x, pp.mouse.y)
  
def mouseDragged():
    arcball.mouseDragged(pp.mouse.x, pp.mouse.y) 

def defineLights():
    pp.ambientLight(50, 50, 50)
    pp.pointLight(150, 100, 0, 200, -150, 0)
    pp.directionalLight(0, 102, 255, 1, 0, 0)
    pp.spotLight(255, 255, 109, 0, 40, 200, 0, -0.5, -0.5, pp.PI / 2, 2)

def keyPressed():
    """
    Important gotcha coming from regular processing
    key.char not key to compare key characters, fix axis
    of rotation by holding down key corresponding to axis
    """
    if (pp.key.char == 'x'):
        arcball.selectAxis(X)
    if (pp.key.char == 'y'):
        arcball.selectAxis(Y)
    if (pp.key.char == 'z'):
        arcball.selectAxis(Z)

def keyReleased():
    """
    Release axis constraint
    """
    arcball.selectAxis(-1)
    