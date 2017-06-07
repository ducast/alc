from taylor import *
from rkn import *


# Parâmetros
def f1(t,x0,x1):
    F = 2*sin(0.5*t) + sin(2*0.5*t) + cos(3*0.5*t)
    return F - x0 - 0.2*x1

x0 = 0
x1 = 0
a = 0
b = 100
delta = 0.1

# Escolha do método [taylor, rkn]
method = euler

method(f1,x0,x1,a,b,delta)
