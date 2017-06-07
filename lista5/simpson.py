from polinomialIntegration import *

def simpson(f,a,b):
    print ("==== Integração por Simpson ====")

    mid_point = polinomialIntegration(f,a,b,1)
    trapezoid = polinomialIntegration(f,a,b,2)

    area = (2*mid_point + trapezoid)/3.0

    print ("Resultado = ",area)
    return area

def f1(x):
    return exp(-x**2)

a = 0
b = 20

simpson(f1,a,b)
