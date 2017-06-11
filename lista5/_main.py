from gaussianQuadrature import *
from polinomialIntegration import *

# Parâmetros
def f1(x):
    return x**3/4 + x/2.0

a = 0
b = 4
n = 4
# Escolha do método [polinomialIntegration, gaussianQuadrature]
# method = polinomialIntegration
#
# method(f1,a,b,n)
polinomialIntegration(f1,a,b,n)

n=2
gaussianQuadrature(f1,a,b,n)
