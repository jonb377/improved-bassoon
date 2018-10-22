import os
import numpy
from lazylist import LazyList

# Allow the user to define a factorial function
os.system('vim _fact_gen.py')
exec(open('_fact_gen.py').read())

facts = LazyList(fact_gen())  # A list of the factorials

# The simultaneous p-ordering.
a = [1]  # a0 = 1
for i in range(1, 10):
    '''
    pol: The polynomial we need to solve: (a_i - a0) ... (a_i - a_i-1)
    '''
    pol = [1]
    for ai in a:
        newpol = [0] * (len(pol) + 1)
        for j in range(len(pol)):
            newpol[j] += pol[j]
            newpol[j + 1] -= pol[j] * ai
        pol = newpol
    pol[-1] -= facts[i]
    for root in numpy.roots(pol):
        if root.imag == 0:
            a.append(round(root.real, 4))
            break
print(a)
