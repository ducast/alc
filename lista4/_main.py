from broyden import *
from inverseInterpolation import *
from functionAdjustment import *
from newtonMultiDim import *
from math import *
from rootBisect import *
from rootNewton import *
from rootSecant import *

def f1(X):
    return X[0] - X[1] + 2

def f2(X):
    return exp(X[0]) + X[1] - 6

f = [f1,f2]
x0 = [1.5, 1.0]
max_it = 10000
tol = 10**(-3)

print ('\n')
newtonMultiDim(f,x0,max_it,tol)
print ('\n')
broyden(f,x0,max_it,tol)

# def f1(x):
#     return exp(-x) - x/2.0
#
# a=0.5
# b=2
# tol = 10**(-3)
# max_it = 100
#
# rootBisect(f1,a,b,tol)
# print ('\n')
# rootNewton(f1,a,max_it,tol)
# print ('\n')
# rootSecant(f1,a,max_it,tol)

#
# def ex1(x):
#     return log(cosh(x*sqrt(9.806*0.00341)))-50
#
# def ex2(x):
#     return 4*cos(x)-exp(2*x)
#
# ### Exercicio 1
#
# # Raiz por Interpolação Inversa
# f, x0, max_it, tol = ex1, [0,1,2], 10000, 10**(-4)
# inverseInterpolation(f,x0,max_it,tol)
#
# # Raiz por Bisseção
# f, a, b, tol = ex1, -10, 10, 10**(-4)
# rootBisect(t,a,b,tol)
#
# # Raiz por Newton
# f, x0, max_it, tol = ex1, 10, 10000, 10**(-4)
# rootNewton(t,x0,max_it,tol)
