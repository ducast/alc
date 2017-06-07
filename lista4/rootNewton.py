from math import *
import numdifftools as nd

def rootNewton(f,x0,max_it,tol):
    print ("==== Método de Newtown para Raízes ====")
    for it in range(max_it):
        x = x0 - f(x0) / nd.Derivative(f)(x0)
        tolk = abs(x - x0)
        if tolk < tol:
            print ("Convergiu para %d iterações.\nXi = "%(it+1),x)
            return x
        x0 = x
    print ("Não convergiu para %d iterações.\nXk = "%(it+1),x)

# def f1(x):
#     return x**2-4*cos(x)
#
# f=f1
# x0 = 10
# max_it = 10000
# tol = 10**(-4)
#
# rootNewton(f1,x0,max_it,tol)
