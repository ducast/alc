from gaussianQuadrature import *
from polinomialIntegration import *

# Parâmetros
def f1(t,fx):
    return -2 * t * fx**2

a = 0
b = 2
n = 2

# Escolha do método [polinomialIntegration, gaussianQuadrature]
method = polinomialIntegration

method(f1,x0,a,b,delta)
