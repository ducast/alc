from math import *
from numpy import np
from gaussWeights import *

def getWeights(degree):
    return gaussWeights[degree]

def gaussianQuadrature(f,a,b,n):
    print ("==== Integração por Quadratura de Gauss ====")

    # Intervalo
    L = b-a

    area = 0
    for i in range(n):

        # Definição dos pesos
        W = gaussWeights(n)
        w1 = W[i][0]
        w2 = W[i][1]

        x = (a+b + w2*(L))/2.0
        area += f(x)*w1

    area *= (L/2.0)

    print ("Resultado = ",area)
    return area


def f1(x):
    return exp(-x**2)

def f2(x):
    return 2 + x + 2 * x**2

a = 1
b = 3
n = 7

gaussianQuadrature(f1,a,b,n)
