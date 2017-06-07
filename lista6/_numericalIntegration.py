from euler import *
from rungeKutta2 import *
from rungeKutta4 import *

# Parâmetros
def f1(t,fx):
    return -2 * t * fx**2

x0 = 1
a = 0
b = 2
delta = 0.1

# Escolha do método [euler,rungeKutta2,rungeKutta4]
method = euler

method(f1,x0,a,b,delta)
