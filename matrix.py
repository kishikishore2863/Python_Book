import numpy as np
m=np.array ([
    [0,1,0,1],
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0]
])

a = m@m


b= a@m
print(b)