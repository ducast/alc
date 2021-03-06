from math import *
import numpy as np

def polinomialIntegration(f,a,b,n):
    print ("==== Integração Polinomial ====")

    # Evitar divisão por zero no caso n=1
    try:
        deltaX = (b-a)/(n-1)
    except:
        area = (b-a) * f( (a+b)/2.0 )
        print ("Resultado = ",area)
        return area

    # Preenchimento da lista X e do vetor B
    X = []
    vectorB = []
    for i in range(n):
        x = a + deltaX*i
        B = (b**(i+1) - a**(i+1)) / (i+1.0)

        X.append(x)
        vectorB.append(B)

    # Cálculo da matriz de Vandermonde
    X = np.array(X)
    vanderMatrix = np.transpose(np.vander(X, increasing=True))

    # Solução da equação V*W = B
    W = np.linalg.solve(vanderMatrix, vectorB)

    # Somatório das áreas embaixo do gráfico (integral)
    area = 0
    for i in range(len(W)):
        area += W[i] * f(X[i])

    print ("Resultado = ",area)


# def f1(x):
#     return exp(-x**2)
#
# a = 0
# b = 1
# n = 3
#
# polinomialIntegration(f1,a,b,n)
