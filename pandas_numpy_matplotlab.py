import numpy as np
import random as random
import matplotlib.pyplot as plt
import pandas as pd

i=0
c = []
while i< 10000:
  j=0
  b = []
  while j< 13:
    a = random.randint(0, 10000)
    b.append(a)
    j += 1
  # print(b)
  i += 1
  c.append(b)
d = np.array(c)
print(d.shape)
e = pd.DataFrame(c)
f = d.shape
y = 0
# while f[1] > y:
  
plt.plot(c)
plt.show()
e
