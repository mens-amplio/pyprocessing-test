import math
import pyprocessing as processing

f = open("../modeling/cylinder_endpoints.txt")
data = eval(f.read())

def how_long(c):
  return math.sqrt(sum( map( lambda(s):s*s, map( lambda(x,y):x-y, zip(c[0], c[1]) ) ) ))

processing.size(1200, 800)

processing.translate(600, 550, 300);

for c in data:
  x = how_long(c)
  if x > 17:
    processing.line(c[0][0], c[0][1], c[0][2], c[1][0], c[1][1], c[1][2])
    processing.stroke(0);

print("ok")

processing.run()
