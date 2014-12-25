a = [-3,5,2,-10,7,8]

b = 'abc'

c = [2*s for s in a]
d = [s for s in a if s>=0]
e = [(x,y) for x in a for y in b if x >0]

import math
f = [(1,2),(3,4),(5,6)]
g = [math.sqrt(x*x + y*y) for (x,y) in f]
print g