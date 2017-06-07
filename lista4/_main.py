from broyden import *
from inverseInterpolation import *
from linearRegression import *
from newtonMultiDim import *
from rootBisect import *
from rootNewton import *
from rootSecant import *

def ex1(x):
    return log(cosh(x*sqrt(9.806*0.00341)))-50

def ex2(x):
    return 4*cos(x)-exp(2*x)

### Exercicio 1

# Raiz por Interpolação Inversa
f, x0, max_it, tol = ex1, [0,1,2], 10000, 10**(-4)
inverseInterpolation(f,x0,max_it,tol)

# Raiz por Bisseção
f, a, b, tol = ex1, -10, 10, 10**(-4)
rootBisect(t,a,b,tol)

# Raiz por Newton
f, x0, max_it, tol = ex1, 10, 10000, 10**(-4)
rootNewton(t,x0,max_it,tol)

# Raiz por Secante
f, x0, max_it, tol = 
